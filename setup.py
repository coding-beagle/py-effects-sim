from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='piamp',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'Click',
        'SoundDevice'
    ],
    entry_points={
        'console_scripts': [
            'piamp = piamp.main:cli',
        ],
    },
)
