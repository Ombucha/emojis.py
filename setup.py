from pathlib import Path

from setuptools import setup

HERE = Path(__file__).resolve().parent
README = (HERE / "README.rst").read_text()

setup(
    name = "emojis.py",
    version = "1.1.0",
    description = "A basic emoji manipulator for Python.",
    package_data = {"emojis.py": ["database/*.json"]},
    long_description = README,
    long_description_content_type = "text/x-rst",
    url = "https://github.com/Ombucha/emojis.py",
    author = "Omkaar",
    author_email = "omkaar.nerurkar@gmail.com",
    license = "MIT",
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    python_requires='>= 3.8.0',
    packages = ["emojis"],
    include_package_data = True
)
