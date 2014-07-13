from setuptools import setup, find_packages

VERSION = '1.0.0'

with open('README.rst') as f:
    README = f.read()

entrypoints = {
    'console_scripts': 'datagen = datagen:main'
}

setup(
    name='datagen',
    version=VERSION,
    description='Generate delimited sample data with a simple schema.',
    long_description=README,
    author='Todd Wilson',
    author_email='todd@toddwilson.net',
    license='Apache License 2.0',
    url='https://github.com/toddwilson/datagen',
    download_url='https://github.com/toddwilson/datagen/tarball/%s' % VERSION,
    keywords=['data generation', 'sample data', 'hadoop'],
    entry_points=entrypoints,
    include_package_data=True,
    packages=find_packages('datagen'),
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    )
)
