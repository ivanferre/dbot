# Dockerize Read Me

Journal on making a Docker container for the dbot app.

When building the container, `pip3` ends with error due to missing references. Probable cause is depicted in the following article: [Handling modules on PyPI that are now in the standard library?](https://discuss.python.org/t/handling-modules-on-pypi-that-are-now-in-the-standard-library/27071/1)

It's the same problem in local Ubuntu and in AWS EC2 Ubuntu, just different dependency.

Let's try update python. We follow the procedure from [How to upgrade to Python 3.11 on Ubuntu 20.04 and 22.04 LTS](https://www.itsupportwale.com/blog/how-to-upgrade-to-python-3-11-on-ubuntu-20-04-and-22-04-lts/)

Now we use python3.11.4.

Note: **We must change the reference in the Dockerfile accordingly !!!**

The problem was we were referencing in Dockerfile a non-existent python3.12 library.

Python containers repository: <https://hub.docker.com/_/python>

New problem:

    ERROR: failed to solve: python3.11.4-alpine3.18: pull access denied, repository does not exist or may require authorization: server message: insufficient_scope: authorization failed

New spec for Python in Dockerfile: `FROM python:3`
It works!

Quotes:

> Stop wasting time defending your problems and work on addressing them instead. -Celestine Chua

> There is little success where there is little laughter. -Andrew Carnegie

Right now, the discord bot is running in a Docker container in a AWS EC2 instance.
