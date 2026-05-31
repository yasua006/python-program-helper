import questionary

from modules.sp_helper import *


def ask_gh_pages() -> None:
    agree = questionary.confirm("Will part of your frontend be on Github Pages? ").ask()

    if agree:
        ask_nojekyll_()


def ask_nojekyll_() -> None:
    agree = questionary.confirm("Will you use jekyll? ").ask()

    if agree:
        print("Attempting to add .nojekyll file...")
        add_empty_output = sp_run(
            "touch .nojekyll",
            capture=True
        )

        handle_sp_errors(
            add_empty_output,
            success_msg="Added .nojekyll file",
            err_msg="Could not add .nojekyll file!"
        )
