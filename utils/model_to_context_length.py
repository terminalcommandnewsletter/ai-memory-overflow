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


def model_to_context_length(model: str):
    """
    Gets the context length for a model based on a list of prefixes.
    """
    prefixes = {
        32768: ["gpt-4-32k"],
        8192: ["gpt-4"],
        8001: ["code-davinci-"],
        4097: [
            "text-davinci-",
        ],
        4096: ["gpt-3.5-turbo"],
        2049: ["text-", "davinci", "curie", "babbage", "ada"],
        2048: ["code-cushman-"],
    }
    for l in prefixes.keys():
        for p in prefixes[l]:
            if model.startswith(p):
                return l
    print(
        "Error: no context length found for model. Check model specified or specify a context length manually using the -l/--context-length option."
    )
    print("exiting with error code 1...")
    exit(1)
