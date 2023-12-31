# -*- coding: utf-8 -*-
"""
@author: PabloDelCampo
"""

from setuptools import setup, find_packages
from tensor_calculator import __author__,__version__,__name__


VERSION = __version__
AUTHOR = __author__
NAME = __name__

setup(
    name                    = NAME,
    version                 = VERSION,
    description             = 'Package containing a tensor calculator',
    author                  = AUTHOR,
    author_email            = 'pablodc314@gmail.com',
    license                 = 'MIT',
    python_requires         = '>=3.9.5',
    packages                = find_packages(),
    include_package_data    = True,
    package_data            = {'': ['resources/*.csv','resources/clusters/*.csv']},
    install_requires        = [
                                'pandas',
                                'numpy',
                                'torch'
                                ]
     )