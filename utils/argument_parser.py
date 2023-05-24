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

import argparse

parser = argparse.ArgumentParser(
    description="Generate prompts longer than context length for a model using OpenAI's tiktoken library.",
    add_help=True,
)
parser.add_argument(
    "--model",
    "-m",
    help="model to be used e.g. gpt-3.5-turbo, gpt-4",
    type=str,
    required=True,
)
parser.add_argument(
    "--context-length", "-l", help="context length for model", type=int, required=False
)
parser.add_argument(
    "--separator",
    "-s",
    help="separator of blocks",
    type=str,
    required=False,
    default="-",
)
parser.add_argument(
    "--block-length",
    "-b",
    help="length of each block",
    type=int,
    required=False,
    default=5,
)
parser.add_argument(
    "--prompt",
    "-p",
    help="prompt before blocks. Use {separator} to use separator in prompt.",
    type=str,
    required=False,
    default="Block = {block_length} alphanumeric characters joined with a `{separator}`. Provide me the first block and last block without truncation from this list:",
)
parser.add_argument(
    "--charset",
    "-c",
    help="character set used for blocks",
    type=str,
    required=False,
    default="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
)
parser.add_argument(
    "--old",
    "-u",
    help="method which adds the separator before the first one rather than joining blocks together, used in initial analysis",
    action="store_true",
    required=False,
    default=False,
)
parser.add_argument(
    "--verbose",
    "-v",
    help="log every block with the number of tokens used",
    action="count",
    required=False,
    default=0,
)
parser.add_argument(
    "--check",
    "-x",
    help="interactive checker to check position of block in list of blocks",
    action="store_true",
    required=False,
    default=False,
)
parser.add_argument(
    "--blocks-per-iteration",
    "-n",
    help="number of blocks in one iteration. Increases prompt generation speed, but reduces accuracy (because of a larger number of blocks after the context length).",
    type=int,
    required=False,
    default=1,
)

args = parser.parse_args()


def parse_args():
    return args
