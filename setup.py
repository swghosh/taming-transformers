from setuptools import setup, find_packages

setup(
    name='taming-transformers',
    version='1.0.0+pt-2.0',
    description='Taming Transformers for High-Resolution Image Synthesis',
    packages=find_packages(),
    install_requires=[
        'torch',
        'numpy',
        'tqdm',
    ],
)
