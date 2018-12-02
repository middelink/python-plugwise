import os
import sys

from setuptools import setup, find_packages

setup(name='plugwiselib', 
    version='0.2',
    description='A library for communicating with Plugwise smartplugs',
    author='Sven Petai',
    author_email='hadara@bsd.ee',
    url='https://bitbucket.org/hadara/python-plugwise/wiki/Home',
    license='MIT',
    packages=find_packages(),
    py_modules=['plugwise'],
    install_requires=[
          'crcmod',
          'pyserial',
      ],
    download_url='https://github.com/cyberjunky/python-plugwise/archive/0.2.tar.gz',
    scripts=['plugwise_util'],
)

