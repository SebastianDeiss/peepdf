from setuptools import find_packages, setup

setup(
    name="peepdf",
    version="0.3.1",
    author="Jose Miguel Esparza",
    license="GNU GPLv3",
    url="http://eternal-todo.com",
    install_requires=[
        "jsbeautifier==1.6.2",
        "colorama==0.3.7",
        "Pillow==3.2.0",
        "pythonaes==1.0",
        "lxml==3.6.0",
    ],
    entry_points={
        "console_scripts": [
            "peepdf = peepdf.main:main",
        ],
    },
    packages=["peepdf"],
)
