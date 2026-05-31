import atexit

from modules.frontend_template import *
from modules.empty_folders import ask_common_vanilla_frontend
from modules.empty_files import ask_gh_pages


def main() -> None:
    ask_frontend_template()
    ask_common_vanilla_frontend()
    ask_gh_pages()


if __name__ == '__main__':
    main()


@atexit.register
def program_exit():
    print("Exited program")
