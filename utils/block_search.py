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


def get_block_input(blocks: list):
    """
    Asks the user for input until a valid block is entered.
    """
    try:
        index = int(
            blocks.index(input("Type the last block the AI sees to look for here: "))
            + 1
        )
    except:
        index = None
    while index == None:
        print("Sorry, that wasn't valid. Input is CaSe-SeNsItIvE.")
        try:
            index = int(
                blocks.index(
                    input("Type the last block the AI sees to look for here: ")
                )
                + 1
            )
        except:
            index = None
    return index


def block_search(blocks: list):
    """
    Gets user input using `get_block_input(blocks)` and prints statistics.
    """
    searched_block_index = get_block_input(blocks)
    print(
        "{},{},{}%".format(
            searched_block_index, len(blocks), searched_block_index / len(blocks) * 100
        )
    )
