from setuptools import setup
from setuptools import find_packages

with open("README.md", "r") as fh:
    long_desc = fh.read()

setup(
    name="valorant-ingame-twitch-chat",
    version="1.0",
    author="outrowender",
    description="A chat ",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/outrowender/valorant-ingame-twitch-chat",
    project_urls={
        "Bug Tracker": "https://github.com/outrowender/valorant-ingame-twitch-chat/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.0",
)
