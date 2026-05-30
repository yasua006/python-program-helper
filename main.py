import atexit

from modules.frontend_template import *
from modules.empty_folders import ask_common_vanilla_frontend, ask_common_flask_folders


def main() -> None:
    ask_frontend_template()
    ask_common_vanilla_frontend()
    ask_common_flask_folders()


if __name__ == '__main__':
    main()


@atexit.register
def program_exit():
    print("Exited program")
