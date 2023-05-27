from setuptools import setup, find_packages


with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="madframe",
    version="0.0.1",
    packages=find_packages(include=["madframe"]),
    description="An event-based framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    entry_points={
        "console_scripts": [
            "madframe = madframe.command:run",
        ],
    },
    install_requires=[],
    extras_require={
        "dev": [
            "pytest",
            "pytest-mock",
            "pytest-asyncio",
            "pytest-coverage",
        ],
        "doc": ["pdoc"],
    },
)
