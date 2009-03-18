from distutils.core import setup

setup(
    name = 'pybugz',
    version = '0.7.4',
    author = 'Alastair Tse',
    author_email = 'alastair@liquidx.net',
    url = 'http://pybugz.googlecode.com',
    description = 'python interface to bugzilla',
    packages = ['bugz'],
    package_data = {'bugz': ['bugzdefs/*']},
    scripts = ['bin/bugz']
)
