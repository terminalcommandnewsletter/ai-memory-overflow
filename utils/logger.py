# AI Memory Overflow: Generate prompts longer than context length for a model using OpenAI's tiktoken library.

# Copyright (C) 2023 terminalcommandnewsletter

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from utils.argument_parser import parse_args

verbosity_level = parse_args().verbose


def log(message: str, min_verbosity: int):
    """
    Logs `message` prefixed with `LOG: ` if the verbosity is higher than `min_verbosity`
    """
    if verbosity_level >= min_verbosity:
        print("LOG: {}".format(message))


def error(message: str):
    """
    Prints `message` prefixed with `ERROR: ` followed by `exiting with error code 1...` and then exits with error code 1.
    """
    print("ERROR: " + message)
    print("exiting with error code 1...")
    exit(1)
