import subprocess as sp
from subprocess import CompletedProcess


def sp_run(cmd: str, capture: bool = False):
    if capture:
        result = sp.run([cmd],
            text=True, shell=True,
            capture_output=True
        )
        return result
    else:
        sp_run([cmd], text=True, shell=True)


def handle_sp_errors(comp_process: CompletedProcess[str],
    success_msg: str, err_msg: str) -> None:

    if not comp_process.stderr:
        print(success_msg)
    else:
        print(err_msg)

    print(comp_process.stderr)
