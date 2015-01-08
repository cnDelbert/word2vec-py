import os
import subprocess
from distutils.core import setup

'''
To update to a new version:
1. change version
2. python setup.py sdist upload
'''

DESCRIPTION = 'Google word2vec python wrapper'

directory = 'bin'
if not os.path.exists(directory):
    os.makedirs(directory)

return_code = subprocess.call(['make', '-C', 'word2vec-c'])

if return_code != 0:
    exit(0)

setup(
    name='word2vec',
    version='0.7',
    maintainer='Delbert',
    maintainer_email='code@delbert.me',
    url='https://github.com/cnDelbert/word2vec-py',
#    packages=['word2vec'],
    description=DESCRIPTION,
    license='Apache License Version 2.0, January 2004',
    data_files=[('bin', ['bin/word2vec', 'bin/word2phrase', 'bin/w2v-distance',
                         'bin/w2v-word-analogy', 'bin/w2v-compute-accuracy'])],
    install_requires=[
        'numpy>=1.7.1'
    ],
)
