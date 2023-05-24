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

import tiktoken  # IMPORTANT: Used to count tokens.
from random import choices  # IMPORTANT: Used for creating random blocks

from utils.logger import (
    log,
    error,
)  # MEDIUM: Used to log messages if --verbose/-v is used as well as errors.
from utils.argument_parser import (
    parse_args,
)  # IMPORTANT: Parses arguments, available in utils folder.
from utils.model_to_context_length import (
    model_to_context_length,
)  # MEDIUM: Used to get the context length of a model, can be specified using --context-length/-l

log("Loaded log, error and model_to_context_length", 2)

# If you have a Python version above 2.6 and are facing issues with this check, feel free to remove/comment out the code from here...
from sys import version_info

if version_info.major < 3 or version_info.minor < 6:
    error(
        "This script does not work with Python versions lower than 2.6. Install a newer version of Python at https://www.python.org/downloads/"
    )
# ... to here

log("Python version check complete", 2)

args = parse_args()

enc = tiktoken.encoding_for_model(args.model)

context_length = (
    args.context_length if args.context_length else model_to_context_length(args.model)
)

log(
    "model={}, check={}, context_length={}".format(
        args.model, args.check, context_length
    ),
    2,
)

prompt = args.prompt.replace("{separator}", args.separator).replace("{block_length}", str(args.block_length))

blocks = []

tokens_remaining = True

while tokens_remaining:
    new_blocks = [
        "".join(choices(args.charset, k=args.block_length))
        for _ in range(args.blocks_per_iteration)
    ]
    blocks.extend(new_blocks)
    if args.old:
        prompt = prompt + "{}{}".format(args.separator, args.separator.join(new_blocks))
        num_of_tokens = len(enc.encode(prompt))
    else:
        num_of_tokens = len(enc.encode(prompt + args.separator.join(blocks)))
    log("Block #{}: {} tokens".format(str(len(blocks)), str(num_of_tokens)), 1)
    tokens_remaining = num_of_tokens < context_length

if not args.old:
    prompt = prompt + args.separator.join(blocks)
print(
    "Prompt ({} characters, {} tokens, {} blocks)".format(
        len(prompt), len(enc.encode(prompt)), len(blocks)
    )
)
print(prompt)

print("First block = {} and last block = {}".format(blocks[0], blocks[-1]))

if args.check:
    from utils.block_search import (
        block_search,
    )  # MEDIUM: Used to search for index of the last block the AI sees using --check/-x

    block_search(blocks)
