from setuptools import setup, find_packages

setup(
    name="ft_package",
    version="0.0.1",
    author="lleciak",
    author_email="lleciak@42.fr",
    description="A sample test package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/lleciak/ft_package",
    packages=find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    license="MIT",
)

