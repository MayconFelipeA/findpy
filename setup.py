import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'findpy',
    version = '0.0.1',
    author = 'Maycon Felipe',
    author_email = 'maycon_felipegato@hotmail.com',
    description = 'Find folders and files, find string in files, txt, etc..',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/MayconFelipeA/findpy',
    packages = setuptools.find_packages(),
    classifiers = [
        # License
        'License :: OSI Approved :: MIT License',

        # System
        'Operating System :: OS Independent',

        # Python support version 3
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
    ],
    keywords = 'Findpy findString findFolder find archives',
    python_requires = '>=3.6'
)