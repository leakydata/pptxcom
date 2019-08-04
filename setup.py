from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["pywin32>=223"]

setup(
    name="pptxcom",
    version="0.0.1",
    author="Nathan Jones",
    author_email="leakydata@gmail.com",
    description="A package to interact with MS Office PowerPoint COM objects",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/leakydata/pptxcom",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
