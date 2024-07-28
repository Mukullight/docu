# Getting started

Nullval a state of the art package for treatment of null values and outliers. Below is the installation and the usage guide for the package.

Details about the package. [^1] 
Python, you can install nullval with [`pip`][pip] package manager
  [^1]:
    This package is useful financial and numerical data and for basic quant stuff. It can used as a wrapper around your api calls to type check if there is any bad data coming.


  [pip]: #with-pip


## Creating a python virtual environment

Before the installation of the package create a virtual environment with the supported python version 

we recommend using python version == 3.9.19

=== "command"
    ``` 
    conda create --name myenv python=3.9.19
    ``` 

replace myenv with the desired name of your virtual environment

after te virtual environment is created activate the virtual environment using the command


=== "command"
    ``` 
    conda activate myenv
    ``` 


if you are using colab or other online based jupter notebooks run the following command below


=== "command"
    ``` 
    !wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.11.0-Linux-x86_64.sh
    !chmod +x Miniconda3-py39_4.11.0-Linux-x86_64.sh
    !bash ./Miniconda3-py39_4.11.0-Linux-x86_64.sh -b -f -p /usr/local
    !rm Miniconda3-py39_4.11.0-Linux-x86_64.sh
    !conda update conda
    !conda create -n myenv python==3.9.19
    %%shell
    eval "$(conda shell.bash hook)"
    conda activate myenv
    ``` 






## Installation Guide

### with pip <small>recommended</small> { # with-pip data-toc-label="with pip" }

Nullval is published as a python package and can be installed using  [Python package] and can be installed with
`pip`, ideally by using a [virtual environment]. Open up a terminal and install
Material for MkDocs with:

=== "Command"

    ``` 
    pip install nullval
    ``` 

  [^2]:
    Note that improvements of existing features are sometimes released as new packages and version are being updated constantly based on the dependencies
    patch releases of the package maintainers

This will automatically install compatible versions of all dependencies:

Material for
MkDocs always strives to support the latest versions, so there's no need to
install those packages separately.

---

for more information please connect with me on linkedin in github 
# Connect with me

 ![LinkedIn](https://img.shields.io/badge/LinkedIn-%230A66C2.svg?style=for-the-badge&logo=LinkedIn&logoColor=white) --> [linkedin](https://www.linkedin.com/in/mukul-namagiri-434427190/)



---

!!! tip

    If you don't have prior experience with Python, we recommend reading
    [Using Python's pip to Manage Your Projects' Dependencies], which is a
    really good introduction on the mechanics of Python package management and
    helps you troubleshoot if you run into errors.

  [Python package]: https://pypi.org/project/nullval/
  [virtual environment]: https://realpython.com/what-is-pip/#using-pip-in-a-python-virtual-environment
  [Using Python's pip to Manage Your Projects' Dependencies]: https://realpython.com/what-is-pip/





### with git

Material for nullval can be directly used from [GitHub] by cloning the
repository into a subfolder of your project root which might be useful if you
want to use the very latest version:

```
git clone https://github.com/Mukullight/nullvalue
```

  [GitHub]: https://github.com/Mukullight/nullvalue
