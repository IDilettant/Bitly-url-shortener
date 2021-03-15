# Bitly url shortener

It's console utility which takes a link as input and converts it to a short link(bitlink) with [bit.ly](https://bitly.com). 
If a bitlink is entered, it returns the total number of clicks on it.

### How to install

Sign in to the [bit.ly](https://bitly.com) and generate your [Generic Access Token](https://app.bitly.com/Bl32e0RkxyE/onboard/).
Then in project root create ".env" file and write:
```
BITLINK_TOKEN=[your API token]
```

It's recommended to use [pyenv](https://github.com/pyenv/pyenv) to isolate the project.
Python3 and [poetry](https://python-poetry.org/) should be already installed. Then use poetry to install dependencies:

```Python3
poetry install
``` 

### How to use

```
python3 main.py [-h] url [url ...]
```

[![asciicast](https://asciinema.org/a/ALt64cC8beZEw8NE2BpoMoU73.svg)](https://asciinema.org/a/ALt64cC8beZEw8NE2BpoMoU73)

### Project Goals

The code was written as part of exploring the capabilities of the standard library and API protocols.
