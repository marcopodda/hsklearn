# hsklearn

Hydra for scikit-learn

## Setup

Install dependencies with poetry:

```console
$ poetry install --only-root
```

Populate `.env` file with directories:

```console
$ echo "CONFIG_ROOT=./config" > .env
$ echo "DATA_ROOT=path/to/data/folder" >> .env
$ echo "EXPERIMENTS_ROOT=path/to/experiments/folder" >> .env
```

Optional:

1. Install dev dependencies

```console
$ poetry install --with dev-dependencies
```

2. Install pre-commit hooks

```console
$ pre-commit install
```
