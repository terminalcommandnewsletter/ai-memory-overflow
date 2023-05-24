<div align="center">

  # AI Memory Overflow
  <i>A project by [@tercmd (on Twitter)](https://twitter.com/tercmd)</i>

  <!-- ![Stars for the AI Memory Overflow repo](https://img.shields.io/github/stars/terminalcommandnewsletter/ai-memory-overflow?style=for-the-badge&logo=github) -->
  
  Understanding the memory context of AI models by testing prompt lengths exceeding their context limits. [Contributions welcome!](./CONTRIBUTING.md)

</div>

## Table of Contents
- [Testing ChatGPT](#testing-chatgpt)
  - [Test Circumstances](#test-circumstances)
  - [So, how does ChatGPT perform over a hundred tests?](#so-how-does-chatgpt-perform-over-a-hundred-tests)
- [Try it yourself!](#try-it-yourself)
- [Final Test Results](#final-test-results)

## Testing ChatGPT
### Test Circumstances
The `gpt-3.5-turbo` model has a context length of 4096 tokens. The prompt, larger than 4096 tokens, consisted of blocks (5 characters separated by `-`) and asked the AI model to provide the first and last block in the list. With a context length of 4096 tokens, each prompt averaged 973.33 blocks.

### So, how does ChatGPT perform over a hundred tests?

![A line graph titled "% Blocks Remembered" with the subtitle "Prompt > 4097 tokens, 100 tests." The graph shows the percentage of blocks remembered by the ChatGPT model over 100 tests. The line hovers around 78%-79% with occasional dips below 50% and one drop below 20%.](img/gpt-3.5-turbo_memory_4096_tokens.svg)

[Can't view the image? Click here!](./img/gpt-3.5-turbo_memory_4096_tokens.png)

At most, ChatGPT retains context for 79.45% of blocks.

It must be noted that these results only pertain to the `gpt-3.5-turbo` model. Additionally, the test results do not account for instances when ChatGPT responded with code instead of a direct response.

In instances where the model responded with blocks not present in the list, I either retested the prompt in a new conversation, or tested with a new prompt when ChatGPT attempted to fill in the remaining characters and provided an invalid block.

In cases it responded with a truncated block or with a block with incorrect capitalization, the correct, complete version of the block was considered.

Also, with a context length of 3000 tokens (lower than 4096 tokens), ChatGPT remembers context for all blocks, responding with the correct first and last block every time.

## Try it yourself!
To run a test on a model (by OpenAI, as this uses their library `tiktoken`), follow these steps:

1. Install requirements using `pip install tiktoken`.

2. Clone this repo into a folder (`git clone https://github.com/terminalcommandnewsletter/ai-memory-overflow.git`) as the script requires files in `utils/` to run.

3. In the terminal, run `python test.py -m [MODEL]`. Requires Python 2.6 or later.

To see all options, run `python test.py -h`.

Use the `--old`/`-u` flag to use the same concatenation used in the testing (not perfect, since it adds the separator at the beginning).

Also, to check the index of a block, use the `--check`/`-x` flag which will ask for the last block the AI sees and print the response as `"<block index>,<number of blocks>,<percentage blocks remembered>"`.

If you have tested any model extensively (not in the repo), you can [contribute to the repo](./CONTRIBUTING.md).

## Final Test Results
| Test Number | Model Tested | Context Length | Number of Characters per Block | Average (Mean) % Remembered | Lowest % Remembered | Highest % Remembered | Standard Deviation | Number of Tests | Tested by | Test data (without headers, format: `"last" block index,number of blocks,percentage remembered`) |
|-|-|-|-|-|-|-|-|-|-|-|
| 1 | gpt-3.5-turbo | 4096 tokens | 5 | 75.99% | 13.04% | 79.45% | 11.24% | 100 | [@terminalcommandnewsletter](https://github.com/terminalcommandnewsletter) | [Test data](./test-data/gpt-3.5-turbo-terminalcommandnewsletter.csv) |

## License
The license for this repo can be found in the [COPYING](./COPYING) file.

This program comes with ABSOLUTELY NO WARRANTY; for details, check [COPYING](./COPYING). This is free software, and you are welcome to redistribute it
under certain conditions; for details, check [COPYING](./COPYING).