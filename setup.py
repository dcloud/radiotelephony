from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path

from radiotelephony import __version__, __license__

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='radiotelephony',
    version=__version__,
    packages=find_packages(),
    license=__license__,
    long_description=long_description,
    author='Daniel Cloud',
    author_email='daniel+radiotelephony@danielcloud.org',
    url='https://github.com/dcloud/radiotelephony',
    include_package_data=True,
    install_requires=[
        'Click',
        # Colorama is only required for Windows.
        'colorama',
    ],
    entry_points='''
        [console_scripts]
        radiotelephony=radiotelephony.cli:main
    ''',
)
