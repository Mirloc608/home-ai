import subprocess


async def run_shell(command: str):
    result = subprocess.getoutput(command)
    return {"output": result}
