# Zeebe python worker template

A template for Zeebe job workers in python.

## How to use

Simply press the `Use this template` button in the upper right corner and follow the steps.

## Configuration

Configuration is handled using python's builtin `configparser` library and `.ini` files.

The default configuration is stored in `/src/config/worker.ini`. You can either edit this file or change the location with the `CONFIG_FILE_LOCATION` environment variable.

## Docker

To build your docker image: 
```shell script
$ docker build . -t <image_name>:<image_tag> 
```

## Zeebe

The connection to zeebe is made using the [`pyzeebe`](https://github.com/JonatanMartens/pyzeebe) library

## Logging

Logging is done using [`loguru`](https://github.com/Delgan/loguru).

## Tests

Tests are done using `pytest`. They are performed automatically when pushing to: `master`, `development`, `feature/*`, `bugfix/*`, `maintenance/*` branches.

## Python version

The python version used here is 3.8, but 3.5 plus should work if desired (as this is what `pyzeebe` supports)