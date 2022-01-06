import setuptools
from setuptools import setup, find_packages

setup(
    name='EMG tutorial',
    version='1.0',
    packages=setuptools.find_packages(),
    url='https://github.com/luuleitner/EMG_tutorial',
    license='Apache License 2.0',
    author='Christoph Leitner',
    description='Applied electrophysiology and Sensors - EMG exercise',
    install_requires=['tqdm', 'numpy', 'matplotlib', 'pandas'],
)