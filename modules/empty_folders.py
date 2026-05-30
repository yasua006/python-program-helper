import questionary

from modules.sp_helper import *


def ask_common_vanilla_frontend() -> None:
    agree = questionary.confirm("Add common empty vanilla frontend folders? (does not include public / static folder!) ").ask()

    if agree:
        print("Attempting to add common empty vanilla frontend folders...")
        add_empty_output = sp_run(
            "mkdir images modules",
            capture=True
        )

        handle_sp_errors(
            add_empty_output,
            success_msg="Added images and modules folders",
            err_msg="Could not add images or modules folder!"
        )
