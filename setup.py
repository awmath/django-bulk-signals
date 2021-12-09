# -*- coding: utf-8 -*-
import os
from distutils.core import setup

from setuptools import find_packages

# User-friendly description from README.md
current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(current_directory, "README.md"), encoding="utf-8") as f:
        long_description = f.read()
except Exception:
    long_description = ""

from bulk_signals import __version__

setup(
    # Name of the package
    name="django-bulk-signals",
    # Packages to include into the distribution
    packages=find_packages(".", exclude=["tests"]),
    # Start with a small number and increase it with
    # every change you make https://semver.org
    version=__version__,
    # Chose a license from here: https: //
    # help.github.com / articles / licensing - a -
    # repository. For example: MIT
    license="MIT",
    # Short description of your library
    description="A product aggregation function to a postgres database and makes it available with django",
    # Long description of your library
    long_description=long_description,
    long_description_content_type="text/markdown",
    # Your name
    author="Axel Wegener",
    # Your email
    author_email="pypi@sparse-space.de",
    # Either the link to your github or to your website
    url="https://github.com/awmath/django-bulk-signals",
    # Link from which the project can be downloaded
    download_url="https://github.com/awmath/django-bulk-signals",
    # List of keywords
    keywords=["django"],
    # List of packages to install with this one
    install_requires=["django>3"],
    python_requires=">=3",
    # https://pypi.org/classifiers/
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
