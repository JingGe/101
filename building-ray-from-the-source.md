# Building Ray from the Source on Mac

The official document about this topic could be found at: [https://ray.readthedocs.io/en/latest/installation.html\#building-ray-from-source](https://ray.readthedocs.io/en/latest/installation.html#building-ray-from-source)

As I followed the introduction, I have run into many problems. This document will note down everything as I built the Ray from the source.

## Install Python

First of all, go to App Store, download Xcode and install it.

Then install the Homebrew:

> $ /usr/bin/ruby -e "$\(curl -fsSL [https://raw.githubusercontent.com/Homebrew/install/master/install](https://raw.githubusercontent.com/Homebrew/install/master/install)\)"

Update the PATH:

> export PATH="/usr/local/opt/python/libexec/bin:$PATH"

Install python, pip should be installed together automatically:

> brew install python

## Setup Python Virtual env

Install the virtualenv:

> pip3 install virtualenv

Create a dir for python virtual env:

> mkdir pythonvenv
>
> cd pythonvenv

Within the dir, create the venv. At the time of this writing, Ray just released 0.8.0, The source is built with python 3.6:

> virtualenv --no-site-packages --python=python3.6 venv\_github\_ray\_36

Activate the venv. BTW, the command for stopping the virtual env is "deactivate"

> source ./venv\_github\_ray\_36/bin/activate





