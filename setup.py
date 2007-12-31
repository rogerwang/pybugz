from distutils.core import setup

setup(
    name = 'pybugz',
    author = 'Alastair Tse',
    author_email = 'alastair@liquidx.net',
    url = 'http://pybugz.googlecode.com',
    version = '0.8.0',
    packages = ['bugz'],
    package_data = {'bugz': ['bugzdefs/*']},
    scripts = ['scripts/bugz']
)
