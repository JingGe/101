# Building Ray from the Source on Mac

The official document about this topic could be found at: [https://ray.readthedocs.io/en/latest/installation.html\#building-ray-from-source](https://ray.readthedocs.io/en/latest/installation.html#building-ray-from-source)

As I followed the introduction, I have run into many problems. This document will note down everything as I built the Ray from the source.

## Checkout Ray

Chose a dir, for example ~/projects, and run:

> git clone [https://github.com/ray-project/ray.git](https://github.com/ray-project/ray.git)

## Install Bazel

Please refer to [https://docs.bazel.build/versions/master/install-os-x.html](https://docs.bazel.build/versions/master/install-os-x.html). It is easy enough to read. "Installing using binary installer" is recommended.

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

Check if virtual env is active:

> which python

The output should be something like: ~/projects/pythonvenv/venv\_github\_ray\_36/bin/python

## Preparing the build

Install some prerequisite tools:

> pip install cython==0.29.0 setuptools\_scm numpy six tensorflow==1.7.1 pyhocon

## Build Ray

Now use the same terminal and go the ray/python dir and run:

> pip install -e . --verbose

## Trouble Shooting

If you see errors like:

> ERROR: Could not find a version that satisfies the requirement tensorflow==1.7.1 \(from versions: 1.13.0rc1, 1.13.0rc2, 1.13.1, 1.13.2, 1.14.0rc0, 1.14.0rc1, 1.14.0, 1.15.0rc0, 1.15.0rc1, 1.15.0rc2, 1.15.0rc3, 1.15.0, 2.0.0a0, 2.0.0b0, 2.0.0b1, 2.0.0rc0, 2.0.0rc1, 2.0.0rc2, 2.0.0, 2.1.0rc0, 2.1.0rc1, 2.1.0rc2\) ERROR: No matching distribution found for tensorflow==1.7.1

Please check your python version. Maybe you are using python 3.7.





