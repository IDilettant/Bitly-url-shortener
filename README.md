# Bitly url shorterer

It's console utility which takes a link as input and converts it to a short link(bitlink) with bit.ly. 
If a bitlink is entered, it returns the total number of clicks on it.

### How to install

Sign in to the bit.ly and generate your [Generic Access Token](https://app.bitly.com/Bl32e0RkxyE/onboard/).
Then in project root create ".env" file and write:
```
BITLINK_TOKEN=[your API token]
```

Python3 and poetry should be already installed. Then use poetry to install dependencies:

```Python3
poetry install
```
It's recommended to use [pyenv](https://github.com/pyenv/pyenv) to isolate the project 

### Project Goals

The code was written as part of exploring the capabilities of the standard library and API protocols
