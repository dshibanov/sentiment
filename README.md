# Parse twitter for text messages

## Deploy


### 0 install tools
    - gh
        https://cli.github.com/

    - pyenv
        https://realpython.com/intro-to-pyenv/
        https://github.com/pyenv/pyenv

    - poetry
        https://python-poetry.org/docs/


### 1 clone repo

```
gh repo clone dshibanov/sentiment
```

### 2 create env

```
poetry env use (pyenv local)
```

### 3 install packages

```
poetry install
```

### 4 run 

```
poetry run python sentiment/parse_twitter.py
```




