from core.execution.result import ExecutionResult, StepResult
from core.execution.tool_router import execute_tool
from core.execution.policies import validate_step


async def execute_plan(plan: dict) -> ExecutionResult:

    results = []
    state = {}

    for step in plan["steps"]:

        if not validate_step(step):
            return ExecutionResult(
                success=False,
                step_results=results,
                failed_step=step["id"]
            )

        try:
            if step["type"] == "analyze":
                output = f"analyzed: {step['input']}"
            else:
                output = await execute_tool(step["type"], step.get("input", {}))

            results.append(StepResult(
                step_id=step["id"],
                success=True,
                output=output
            ))

            state[step["id"]] = output

        except Exception as e:
            results.append(StepResult(
                step_id=step["id"],
                success=False,
                error=str(e)
            ))

            return ExecutionResult(
                success=False,
                step_results=results,
                failed_step=step["id"]
            )

    return ExecutionResult(
        success=True,
        step_results=results
    )
