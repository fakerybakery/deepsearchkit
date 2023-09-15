from setuptools import setup, find_packages

setup(
    name='deepsearchkit',
    version='1.0.1',
    packages=find_packages(),
    install_requires=[
        'txtai',
        'tqdm'
    ],
    author='mrfakename',
    author_email='me@mrfake.name',
    description='A small, fast, and easy package for semantic searching using artificial intelligence.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/fakerybakery/deepsearchkit',
    # license='',
)
