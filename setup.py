from cx_Freeze import setup, Executable
import setuptools
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="COVID_Classifier",
    version="1.0",
    author="Khang Thai Bao",
    author_email="Minatozaki0911@users.noreply.github.com",
    description="COVID-19 Classifier using CNN desktop Application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Minatozaki0911/summerIntern203",
    
    executable = [Executable(script="mainUI.py", targetName="COVID Classifier.exe", icon="Image/covid 19.ico")],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "SourceCode"},
    packages=setuptools.find_packages(where="SourceCode"),
    python_requires=">=3.6",
)
