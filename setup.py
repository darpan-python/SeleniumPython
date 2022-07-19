from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='sel_table',
    version='1.0',
    install_requires=required,
    package_dir={'': 'sel_table'},
    packages=['core', 'drivers'],
    include_package_data=True,
    py_modules=['app'],
    author='root',
    author_email='',
    description='Selenium application for internal use only'
)

# Command to execute
#python setup.py install
