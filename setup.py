from setuptools import setup, find_packages

import os, sys

setup(name='motmot.wxvalidatedtext',
      description='validated integer/float text entry field for wxPython',
      author='Andrew Straw',
      author_email='strawman@astraw.com',
      license='BSD',
      version='0.5.1', # keep in sync with wxvalidatedtext/wxvalidatedtext.py
      zip_safe=True,

      namespace_packages = ['motmot'],
      packages = find_packages(),
      entry_points = {'gui_scripts': [
    'wxvalidatedtext_demo = motmot.wxvalidatedtext.demo:main',
    ]
                      },
      package_data = {'wxvalidatedtext_demo':['demo.xrc']},
      eager_resources = ['motmot/wxvalidatedtext/demo.xrc'],
      )
