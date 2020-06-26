from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="to_pypi",
    version="1.0.1",
    description="GUI application is used to make python package for pypi and test pypi and upload. This lets user avoid using cmd commands for the same",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/nvakhilnair/PyPI-upload-package",
    author="Akhil",
    author_email="MadeWithPY009@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=[],
    install_requires=["PyQt4>=4.11.4","twine>=3.1.1",
"wheel>=0.34.2"],
    scripts=["to_pypi.py"],
    package_data={'data': ['icon.ico','logo.png']},
    include_package_data=True,
)
