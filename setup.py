from setuptools import setup
setup(name='extractseq',
version='0.1',
description='Extract sequence package',
url='#',
author='Begüm Serra',
author_email='begumserra.buyuktarakci@icm.uu.se',
license='MIT',
packages=['extractseq'],
 install_requires=[
          'pandas=1.3.4',
'python=3.10.0',
'biopython=1.79',
'sys',
'argparse',
'Bio',
'SeqIO',
      ],

zip_safe=False)
