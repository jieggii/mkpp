import pathlib
import re

from mkpp import cli

_PACKAGE_NAME_REGEX = r"^[a-z0-9\_]+$"  # https://pep8.org/#package-and-module-names


def main():
    args = cli.args.parse_args()

    include = [f"{name}.py" for name in args.include] if args.include else []
    include.append("__init__.py")
    if args.executable:
        include.append("__main__.py")

    include = sorted(include)

    for package in args.packages:
        path = pathlib.Path(package)
        name = path.name

        if args.no_pep8 is False:
            if not re.fullmatch(_PACKAGE_NAME_REGEX, name):
                cli.log.error(
                    f"{name} ({path}): package name does not match PEP8 naming standards "
                    "(https://pep8.org/#package-and-module-names). "
                    "Use '--no-pep8' flag to disable this check",
                    fatal=True,
                )

        try:
            path.mkdir(parents=args.parents, exist_ok=args.parents)
            for file in include:
                file_path = path.joinpath(pathlib.Path(file))
                file_path.touch(exist_ok=True)
            if args.verbose:
                cli.log.info(
                    f"{name} ({path}): was successfully created (children: {', '.join(include)})"
                )

        except FileExistsError:
            raise cli.log.error(f"{name} ({path}): already exists", fatal=True)

        except FileNotFoundError:
            cli.log.error(f"{name} ({path}): some of the parents don't exist", fatal=True)

        except PermissionError:
            cli.log.error(f"{name} ({path}): permission denied", fatal=True)

        except Exception as err:
            cli.log.error(f"{name} ({path}): unexpected error: {err}", fatal=True)


if __name__ == "__main__":
    main()
