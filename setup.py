from pathlib import Path

from setuptools import find_packages, setup


here = Path(__file__).parent.resolve()
readme = (here / 'README.md').read_text()

setup(
    name='macsearch',
    version='1.0.0',
    description='Search network device manufacturer by MAC address',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Kamil Warchoł',
    author_email='kamil.warchol.93@gmail.com',
    url='https://github.com/fisheye36/macsearch',
    packages=find_packages(),
    install_requires=[
        'requests==2.25.1',
    ],
    entry_points='''
        [console_scripts]
        macsearch=macsearch.main:main
    ''',
    python_requires='>= 3.6',
)
