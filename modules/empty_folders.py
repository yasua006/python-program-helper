import questionary

from modules.sp_helper import *


def ask_common_vanilla_frontend() -> None:
    agree = questionary.confirm("Add common empty vanilla frontend folders? (does not include public / static folder!) ").ask()

    if agree:
        print("Attempting to add common empty vanilla frontend folders...")
        add_empty_output = sp_run(
            "mkdir images icons css modules modules/js",
            capture=True
        )

        handle_sp_errors(
            add_empty_output,
            success_msg="Added common empty vanilla frontend folders",
            err_msg="Could not add common vanilla frontend folder(s)!"
        )
    else:
        ask_common_flask()


def ask_common_flask() -> None:
    agree = questionary.confirm("Add common empty Flask folders? ").ask()

    if agree:
        print("Attempting to add common Flask folders...")
        add_empty_output = sp_run(
            "mkdir images icons modules templates static static/js",
            capture=True
        )

        handle_sp_errors(
            add_empty_output,
            success_msg="Added common empty Flask folders",
            err_msg="Could not add common empty Flask folder(s)!"
        )
