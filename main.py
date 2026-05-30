import questionary
import subprocess
import atexit


use_frontend_template = questionary.confirm("Use Sane Vanilla CSS template? ").ask()

if use_frontend_template:
    print("Attempting to clone template...")
    successful_clone = subprocess.run(
        ['git clone --progress https://github.com/placewith5s/sane-vanilla-css | grep -q "Cloning into"'],
        text=True, shell=True,
        capture_output=True
    )

    if not successful_clone.stderr:
        print("Cloned template")
    else:
        print("Could not clone template!")

    print(successful_clone.stderr)


@atexit.register
def program_exit():
    print("Exited program")
