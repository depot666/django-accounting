#!/usr/bin/env python
"""
Installation script:

To release a new version to PyPi:
- Ensure the version is correctly set in accounting.__init__.py
- Run: python setup.py sdist upload
"""
from setuptools import setup, find_packages
import os
import sys

from accounting import get_version

PROJECT_DIR = os.path.dirname(__file__)

setup(name='django-accounting',
      version=get_version().replace(' ', '-'),
      url='https://github.com/dulaccc/django-accounting',
      author="Pierre Dulac",
      author_email="pierre@dulaccc.me",
      description="Accounting made accessible for small businesses and "
                  "sole proprietorships through a simple Django project",
      long_description=open(os.path.join(PROJECT_DIR, 'README.md')).read(),
      keywords="Accounting, Django, Money, Cashflow",
      license='MIT',
      platforms=['linux'],
      packages=find_packages(exclude=["tests*"]),
      include_package_data=True,
      install_requires=[
          'django>=1.7.0,<1.8',
          # Bower is used for the assets dependencies
          'django-bower==5.0.1',
          # Used to render the forms
          'django-bootstrap3==4.11.0',
          # A better static files server
          'dj-static==0.0.6',
          # Define beautiful tags
          'django-classy-tags==0.5.1',
          # Internationalization
          'Babel>=1.0,<1.4',
      ],
      # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: Unix',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Topic :: Software Development :: Libraries :: Application Frameworks']
      )