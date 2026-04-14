def build_failure_context(plan: dict, result) -> str:
    """
    Turns execution failure into structured replan input.
    """

    failed_step = result.failed_step

    failed_steps = [
        r for r in result.step_results
        if not r.success
    ]

    return f"""
Execution failed.

FAILED STEP:
{failed_step}

PLAN:
{plan}

STEP RESULTS:
{[
    {
        "step_id": r.step_id,
        "success": r.success,
        "error": r.error,
        "output": r.output
    }
    for r in result.step_results
]}
"""
