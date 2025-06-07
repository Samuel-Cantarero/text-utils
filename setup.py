from setuptools import setup, find_packages

setup(
    name="text_utils",
    version="0.1.0",
    packages=find_packages(include=["text_utils_program"]),
    install_requires=[],
    author="Antonio Samuel Cantarero Malagón",
    author_email="ascm1980@gmail.com",
    description="Text Utilities for Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Samuel-Cantarero/text_utils",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6")