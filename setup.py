import setuptools
from sshb import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    install_requires = fh.read().splitlines()

setuptools.setup(
    name="sshb",
    version=__version__,
    author="Ömer Atalay",
    author_email="omer@atalay.dev",
    description="Connecting SSH a lot ? Try sshb.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="ssh sshb ssh-bookmark",
    url="https://github.com/atalaydev/sshb",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    entry_points={
        'console_scripts': ['sshb=sshb.__main__:main'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
