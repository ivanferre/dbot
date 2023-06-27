# Dockerize Read Me

Journal on making a Docker container for the dbot app.

When building the container, `pip3` ends with error due to missing references. Probable cause is depicted in the following article: [Handling modules on PyPI that are now in the standard library?](https://discuss.python.org/t/handling-modules-on-pypi-that-are-now-in-the-standard-library/27071/1)

It's the same problem in local Ubuntu and in AWS EC2 Ubuntu, just different dependency.

Let's try update python. We follow the procedure from [How to upgrade to Python 3.11 on Ubuntu 20.04 and 22.04 LTS](https://www.itsupportwale.com/blog/how-to-upgrade-to-python-3-11-on-ubuntu-20-04-and-22-04-lts/)

Now we use python3.11.4.
