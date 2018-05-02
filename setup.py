#!/usr/bin/env python


import os
from setuptools import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = "pylcdui",
    version = "0.5.8",
    description = "Library for CrystalFontz and Matrix-Orbital LCD displays",
    author = "mike wakerly",
    author_email = "opensource@hoho.com",
    url = "http://code.google.com/p/pylcdui/",
    packages = [
      'lcdui',
      'lcdui.core',
      'lcdui.ui',
      'lcdui.devices',
    ],
)
