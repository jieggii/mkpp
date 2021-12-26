# mkpp
Simple tool for creating Python packages. For lazies.
[![asciicast](https://asciinema.org/a/XDgcUhOMcB2WQZnmnc0HLD70u.svg)](https://asciinema.org/a/XDgcUhOMcB2WQZnmnc0HLD70u)

## Installation
**mkpp** can be easily installed via **pip**:

`pip install mkpp`

## Usage
`mkpp [--help] [--verbose] [--version] [--parents] [--no-pep8] [--include [FILES]] [--executable] packages [PACKAGES]`

## Examples
* `mkpp --executable mypackage1 ~/code/projects/mypackage2 some-dir/mypackage3 --include config`
* `mkpp app --executable`
* `mkpp --executable prog --include utils cli`
