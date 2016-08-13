from setuptools import setup, find_packages

setup(name='textteaser',
      url='https://github.com/DataTeaser/textteaser',
      license='MIT',
      version='0.0.2',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=['nltk'],
)
