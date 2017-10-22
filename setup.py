import pathlib
import re

from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent
readme_file = here / "README.rst"
source_file = here / "src" / "rr" / "pretty.py"
version_match = re.search(r"__version__\s*=\s*(['\"])(.*)\1", source_file.read_text())
if version_match is None:
    raise Exception("unable to extract version from {}".format(source_file))
version = version_match.group(2)

setup(
    name="rr.pretty",
    version=version,
    description="Helpers for the creation of nicer repr() and str() representations.",
    long_description=readme_file.read_text(),
    url="https://github.com/2xR/rr.pretty",
    author="Rui Jorge Rei",
    author_email="rui.jorge.rei@googlemail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
)
