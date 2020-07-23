import argparse

from mkpp import __version__


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="mkpp",
        description="A simple tool for creating Python packages. For lazies.",
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {__version__} by jieggii",
        help="show version information and exit",
    )
    parser.add_argument(
        "-i",
        "--ignore-pep8",
        action="store_true",
        help="ignore PEP8 package naming standards",
    )
    parser.add_argument("packages", nargs="+", type=str, help="package(s) to be created")
    package_settings = parser.add_argument_group("package settings")
    package_settings.add_argument(
        "-a",
        "--add",
        nargs="*",
        type=str,
        help="additional *.py files to be created inside package(s)",
    )
    package_settings.add_argument(
        "-e",
        "--executable",
        action="store_true",
        help='create executable package(s) (same as "--add __main__")',
    )

    return parser.parse_args()
