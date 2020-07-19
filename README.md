# mkpp
A simple tool for creating Python packages. For lazies.
![preview](https://imgur.com/vGgTAkS.jpg)

## Installation
mkpp can be easily installed via pip:
`pip install mkpp`

## Usage
`mkpp [--help] [--version] [--ignore-pep8] [--executable] modules [modules ...] [--add [FILE [FILE ...]]]`

## Examples
* `mkpp --executable my_package1 ~/Projects/Python/my_package2 some-dir/my_package3 --add config`
* `mkpp app`
* `mkpp --executable program1`
* `mkpp app --add config utils`
