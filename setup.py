from setuptools import setup, find_packages

long_description = 'Powerful arrays in Python - https://github.com/nayakrujul/star'

setup(
  name = 'star-array',
  version = '1.0',
  license='Apache',
  description = 'Powerful arrays in Python',
  author = 'Rujul Nayak',
  author_email = 'rujulnayak@outlook.com',
  url = 'https://github.com/nayakrujul/star',
  download_url = 'https://github.com/nayakrujul/star/archive/refs/tags/v_01.tar.gz',
  keywords = ['array'],
  install_requires=[
      ],
  classifiers=[
    'Development Status :: 3 - Alpha', 
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
  long_description=long_description,
  long_description_content_type='text/x-rst',
  packages = find_packages()
)
