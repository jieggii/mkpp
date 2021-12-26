from sys import stderr, stdout


def info(message: str):
    print(message, file=stdout)


def error(message: str, fatal: bool = False):
    prefix = "Fatal" if fatal else "Error"
    print(f"{prefix}: {message}", file=stderr)
    if fatal:
        exit(1)
