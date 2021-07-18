import setuptools,platform
from setuptools.command.develop import develop
from setuptools.command.install import install
from subprocess import check_call
import time,sys

class PreDevelopCommand(develop):
    """Pre-installation for development mode."""
    def run(self):
        if platform.system() == "Windows":
            print("Niram Module Not support Windows Command Line!")
            sys.exit(2)
        else:
            print("Started Installing Niram Module...")
            print("------------------------\nDeveloper : Aswanth Vc\nMaintenance: ABAM \n------------------------")
            time.sleep(4)
        install.run(self)

class PreInstallCommand(install):
    """Pre-installation for installation mode."""
    def run(self):
        if platform.system() == "Windows":
            print("Niram Module Not support Windows Command Line!")
            sys.exit(2)
        else:
            print("Started Installing Niram Module...")
            print("------------------------\nDeveloper : Aswanth Vc\nMaintenance: ABAM \n------------------------")
            time.sleep(4)
        install.run(self)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    cmdclass={
        'develop': PreDevelopCommand,
        'install': PreInstallCommand,
    },
    name="Niram", # Replace with your own username
    version="1.0.4",
    author="Aswanth Vc",
    author_email="no-mail@mail.no",
    description="Simple python module to colour text",
    keywords=["colours","change coloure","terminal colour","python colours","pip colours","change colour in terminal","vhange text colour in python"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aswanthabam/Niram",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)