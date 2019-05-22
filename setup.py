#!/usr/bin/env python3

import configparser
import setuptools

config = configparser.ConfigParser()
config.read("Pipfile")

setuptools.setup(install_requires="\n".join([k for k in config["packages"].keys()]))
