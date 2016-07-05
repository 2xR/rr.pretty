from setuptools import setup, find_packages
import pkgutil


with open("README.rst", "rt") as readme_file:
    readme = readme_file.read()

setup(
    name="rr.pretty",
    version=pkgutil.get_data("rr.pretty", "VERSION").decode("utf-8").strip(),
    description="Helpers for creation of nicer repr() and str().",
    long_description=readme,
    url="https://github.com/2xR/rr.pretty",
    author="Rui Jorge Rei",
    author_email="rui.jorge.rei@googlemail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    package_data={"": ["LICENSE", "VERSION"]},
    install_requires=["future~=0.15.2"],
)
