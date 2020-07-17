import os
import re

import colorama
from termcolor import cprint

from mkpm import cli

MODULE_NAME_REGEX = r"^[a-z0-9\_]+$"  # https://pep8.org/#package-and-module-names


def main() -> None:
    colorama.init()
    args = cli.parse_args()

    for i, module_path in enumerate(args.modules):
        module_name = os.path.basename(
            module_path
        )  # path.basename returns None if there is a `/` in the end of the module_path, so we also need to implement
        # this case:
        if not module_name:
            module_name = os.path.basename(module_path[0:-1])

        if not args.ignore_pep8:
            if not re.fullmatch(MODULE_NAME_REGEX, module_name):
                cprint(
                    f'Error: name "{module_name}" does not match PEP8 standards ('
                    f"https://pep8.org/#package-and-module-names). "
                    f"Use --ignore-pep8 flag to skip this check",
                    color="red",
                    attrs=["bold"],
                )
                continue

        if os.path.exists(module_path):
            cprint(f"Error: {module_path} already exists", color="red", attrs=["bold"])
            continue

        if args.add:
            args.add.append("__init__")

        else:
            args.add = ["__init__"]

        if args.executable:
            args.add.append("__main__")

        args.add = list(set(args.add))

        try:
            os.mkdir(module_path)

        except PermissionError:
            cprint(
                f"Error: could not create {module_path}. Permission denied",
                color="red",
                attrs=["bold"],
            )
            continue

        except Exception as unimplemented_error:
            cprint(f"Error: unimplemented error {unimplemented_error}", color="red", attrs=["bold"])
            continue

        for file_name in args.add:
            file_path = os.path.join(module_path, f"{file_name}.py")
            open(file_path, "w").close()
            cprint(f"\tCreated {file_path}", color="white")

        cprint(f"Module {module_path} was created", color="white", attrs=["bold"])


main()
