from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

entrypoints = {
    'console_scripts': 'datagen = datagen:main'
}

setup(
      name='datagen',
      version='1.0.0',
      description='Generate delimited sample data with a simple schema.',
      long_description=readme,
      author='Todd Wilson',
      author_email='todd@toddwilson.net',
      license='Apache License 2.0',
      url='https://github.com/toddwilson/datagen',
      entry_points=entrypoints,
      include_package_data = True,
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
        'Programming Language :: Python :: 3.4',
    ),
)
