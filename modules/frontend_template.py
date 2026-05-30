import questionary

from modules.sp_helper import *


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
