import argparse

from mkpp import __version__


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="mkpp",
        description="mkpp - make Python packages",
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="print a message for each created package",
    )
    parser.add_argument(
        "-p",
        "--parents",
        action="store_true",
        help="no error if existing, make parent directories as needed",
    )
    parser.add_argument(
        "-8",
        "--no-pep8",
        action="store_true",
        help="disable PEP8 package name check",
    )
    parser.add_argument("packages", nargs="+", type=str, help="packages to be created")

    package_settings = parser.add_argument_group("package settings")
    package_settings.add_argument(
        "-i",
        "--include",
        nargs="*",
        type=str,
        help="additional *.py files to be created inside package (no extension needed)",
    )
    package_settings.add_argument(
        "-e",
        "--executable",
        action="store_true",
        help="make executable package (same as '--include __main__')",
    )

    return parser.parse_args()
