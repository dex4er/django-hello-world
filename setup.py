#!/usr/bin/env python3

import ast
import configparser
import setuptools

config = configparser.ConfigParser()
config.read('Pipfile')

setuptools.setup(
    install_requires='\n'.join([f'{k} == {ast.literal_eval(v)}'.replace(' == *', '') for k, v in config['packages'].items()])
)
