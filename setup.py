from setuptools import setup, find_packages

entrypoints = {
    'console_scripts': 'datagen = datagen:main'
}

setup(
      name='datagen',
      version='1.0.0',
      description='Generate delimited sample data with a simple schema.',
      author='Todd Wilson',
      author_email='todd@toddwilson.net',
      license='Apache License 2.0',
      url='https://github.com/toddwilson/datagen',
      entry_points=entrypoints,
      include_package_data = True,
      packages=find_packages('datagen')
)
