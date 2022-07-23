from setuptools import setup, find_packages

with open("requirements.txt") as requirement_file:
    requirements = requirement_file.read().split()

setup(
name="Python",
description="A simple package.",
version="1.0.0",
author="Name",
author_email="Name@domain.com",
install_requires=requirements,
)
