from setuptools import setup, find_packages


# Načtení závislostí z requirements.txt
def parse_requirements(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()

setup(
    name="log_this",
    version="1.0.0",
    packages=find_packages(),
    install_requires=parse_requirements('requirements.txt'),
    description="Malá knihovna pro logování funkcí a metod",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Dalibor Sova",
    author_email="daliborsova@seznam.cz",
    url="https://github.com/Sudip2708",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    # Nastavení pro zadávání příkazu z příkazové řádky.
    entry_points={
        'console_scripts': [
            'log-this-config=log_this.manager.config.cli:main',
            'log_this_config=log_this.manager.config.cli:main',
        ],
    },
)