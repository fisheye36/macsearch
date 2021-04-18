# Description

`macsearch` is a simple tool that returns manufacturer name of a network device, given its MAC address.

It uses web API provided by https://macaddress.io/.

# Usage

## Standard installation

Using Python, preferably in a virtual environment:

```shell
$ python -m macsearch 44:38:39:ff:ef:57 --api-key "${MACSEARCH_API_KEY}"
Company that manufactured the device with MAC address 44:38:39:ff:ef:57 is:
Cumulus Networks, Inc
```

Actually, when environment variable `MACSEARCH_API_KEY` is set, you don't need to provide it explicitly. On the other
hand, when provided, it will supersede the value set by that environment variable.

### Help

To see parameters and options available when running the tool:

```shell
python -m macsearch --help
```

## `setup.py` installation

When installed using `setup.py` script, `macsearch` command is accessible in your `PATH`:

```shell
macsearch 44:38:39:ff:ef:57 --api-key "${MACSEARCH_API_KEY}"
```

## Using Docker

After building Docker image, use it like that:

```shell
docker run --env MACSEARCH_API_KEY="${MACSEARCH_API_KEY}" macsearch-container macsearch 44:38:39:ff:ef:57
```

# Installation

## Local installation

After cloning this repository and ensuring you have your virtual environment set up, install all dependencies:

```shell
pip install -U pip setuptools
pip install -r requirements.txt
```

You can run the tool now using either `python -m macsearch` or `python macsearch/main.py`.

Alternatively and more conveniently you can leverage `setup.py` script:

```shell
pip install -U pip setuptools
pip install . # optionally add -e to be able to directly edit source code and see changes immediately
```

This will allow you to directly use `macsearch`, assuming you have your virtual environment active.

## Using Docker

First, you need to build your image. If you want to embed the API key into the image, you can use `--build-arg` to set
environment variable that will be available when container is run:

```shell
docker build -t macsearch-container --build-arg MACSEARCH_API_KEY_ARG="${MACSEARCH_API_KEY}" .
```

Be careful with that approach because anyone with access to this image could potentially see your API key. To be more
secure, build the image without API key embedded in it:

```shell
docker build -t macsearch-container
```

Keep in mind that you will have to pass it every time you want to run the container, either by using `--api-key` option
that is exposed by `macsearch` tool itself, or `--env MACSEARCH_API_KEY="${MACSEARCH_API_KEY}" exposed by Docker.

# Security considerations

Apart from the fact that you should protect your API key, the tool itself should not pose any security threats, since
all it does is a simple HTTPS GET request.
