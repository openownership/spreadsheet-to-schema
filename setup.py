from setuptools import setup

setup(
    name='spreadsheet-to-schema',
    version='0.0.1',
    author='Open Ownership',
    author_email='code@opendataservices.coop',
    scripts=['spreadsheet-to-schema'],
    url='https://github.com/openownership/',
    description='',
    install_requires=['click', 'json-merge-patch']
)
