from setuptools import setup, find_packages

setup(
    name='test_api_xpress',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'newman',
    ],
    entry_points={
        'console_scripts': [
            'test_api_xpress = main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
