#!/usr/bin/env python

from setuptools import setup

setup(
    name="iptocc",
    packages=[
        "iptocc",
    ],
    package_data={
        "iptocc": [
            "*.db",
            "*.csv",
        ],
    },
    python_requires='>=3.9',
    install_requires=["pandas", "zstandard"],
)
