from setuptools import find_packages, setup
setup(
    name='PyHaier',
    packages=find_packages(include=['PyHaier']),
    version='0.1.5',
    description='Haier heatpump modbus rtu protocol decoder library',
    author='Jacek Brzozowski ',
    author_email='jacekbrzozowski.pld@gmail.com',
    license='GNU AGPL v3.0',
)