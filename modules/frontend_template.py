from subprocess import CompletedProcess
import questionary

from modules.sp_helper import *


def handle_sp_errors(comp_process: CompletedProcess[str],
    success_msg: str, err_msg: str) -> None:

    if not comp_process.stderr:
        print(success_msg)
    else:
        print(err_msg)


def ask_frontend_template() -> None:
    use_frontend_template = questionary.confirm("Use Sane Vanilla CSS template? ").ask()

    if use_frontend_template:
        print("Attempting to clone template...")
        clone_template_output = sp_run(
            'git clone --progress https://github.com/placewith5s/sane-vanilla-css | grep -q "Cloning into"',
            capture=True
        )

        handle_sp_errors(
            clone_template_output,
            success_msg="Cloned template",
            err_msg="Could not clone template!"
        )
