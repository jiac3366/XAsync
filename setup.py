import os

from setuptools import setup, find_packages

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def read_requirements(filename):
    requirements = []
    with open(os.path.join(BASE_DIR, filename)) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                requirements.append(line)
    return requirements


setup(
    name="celery_system",
    description="Celery System",
    install_requires=read_requirements("linux.txt"),
    packages=find_packages(include=("*")),
)
