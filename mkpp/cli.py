import argparse

from mkpm import __version__


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
        help="ignore PEP8 module naming standards",
    )
    parser.add_argument("modules", nargs="+", type=str, help="module(s) to be created")
    module_settings = parser.add_argument_group("module settings")
    module_settings.add_argument(
        "-a",
        "--add",
        nargs="*",
        type=str,
        help="additional *.py files to be created inside module(s)",
    )
    module_settings.add_argument(
        "-e",
        "--executable",
        action="store_true",
        help='create executable module(s) (same as "--add __main__")',
    )

    return parser.parse_args()
