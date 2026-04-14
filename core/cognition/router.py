from core.cognition.planner import Planner
from core.cognition.replanner import Replanner
from core.execution.executor import execute_plan
from memory.rag import retrieve_context


planner = Planner()
replanner = Replanner()


async def route_task(payload: dict):

    task = payload.get("task", "")
    max_retries = payload.get("max_retries", 2)

    # 1. initial context
    context_chunks = await retrieve_context(task)
    context_text = "\n".join([c["text"] for c in context_chunks])

    # 2. initial plan
    plan = await planner.create_plan(task, context_text)

    attempt = 0

    while attempt <= max_retries:

        result = await execute_plan(plan.model_dump())

        if result.success:
            return {
                "status": "success",
                "plan": plan.model_dump(),
                "result": result
            }

        # 3. failure → replan
        plan = await replanner.replan(
            task=task,
            plan=plan.model_dump(),
            result=result
        )

        attempt += 1

    return {
        "status": "failed",
        "final_plan": plan.model_dump(),
        "last_result": result
    }
