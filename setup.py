from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
    version='1.0.0',
    description='sorter, renamer, cleaner',
    author='Svitlana Shulha.',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean=clean_folder.clean:start']}
    ) 
