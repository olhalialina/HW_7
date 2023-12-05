
from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0.0',
    description='Program for sorting files by extension',
    url='https://github.com/olhalialina/HW_7.git',
    author='Olha Lialina',
    author_email='dreadful26@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=[],
    entry_points={'console_scripts': ['clean_folder = clean_folder.clean:main']}
        )