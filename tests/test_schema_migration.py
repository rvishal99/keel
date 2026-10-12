from keel import repo
from keel.db import pool as db


async def test_apply_schema_dedupes_unacked_change_alerts_before_unique_index(db_pool):
    """The unique partial index on unacked change-alerts must not break ensure_schema on
    a deployment that already holds duplicates (created before the dedupe fix). The
    schema's DELETE removes them before the CREATE UNIQUE INDEX."""
    async with db_pool.acquire() as c:
        # simulate a pre-fix deployment: no unique index yet, duplicate unacked rows present
        await c.execute("DROP INDEX IF EXISTS alert_unacked_change_idx")
        await c.execute("TRUNCATE project, person, participant, decision, alert "
                        "RESTART IDENTITY CASCADE")
        pid = await repo.upsert_project(c, "demo")
        person = await repo.upsert_person(c, pid, "vasan", "h")
        part = await repo.upsert_participant(c, pid, person, "cc", "deep", "s1", [])
        d = await repo.insert_decision(c, project_id=pid, statement="x", rationale="r",
                                       scope_tags=["api:orders"], owner_person_id=person,
                                       source_participant_id=part)
        for _ in range(3):  # raw inserts bypass the ON CONFLICT dedupe
            await c.execute(
                "INSERT INTO alert (project_id, target_participant_id, target_person_id, "
                "kind, ref_id) VALUES ($1,$2,$3,'change',$4)", pid, part, person, d["id"])
        assert await c.fetchval("SELECT count(*) FROM alert") == 3

        # apply_schema runs the DELETE then CREATE UNIQUE INDEX — must succeed, not raise
        await db.apply_schema(c)

        assert await c.fetchval("SELECT count(*) FROM alert") == 1  # deduped
        assert await c.fetchval(
            "SELECT 1 FROM pg_indexes WHERE indexname='alert_unacked_change_idx'") == 1
