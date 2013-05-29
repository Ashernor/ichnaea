import os
import sys
from setuptools import setup, find_packages

__version__ = '0.1'

here = os.path.abspath(os.path.dirname(__file__))

requires = [
    'colander',
    'configparser',
    'cornice',
    'retools',
    'PyMySQL',
    'statsd-client',
    'chaussette',
    'konfig',
    'circus',
    'geoalchemy2',
    'psycopg2',
]


if sys.version_info < (2, 7):
    requires.append('argparse')

test_requires = requires + [
    'beautifulsoup4',
    'coverage',
    'nose',
    'unittest2',
    'Webtest',
    'pyspatialite',
    'pysqlite'
]

with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.rst')) as f:
    CHANGES = f.read()


setup(
    name='ichnaea',
    version=__version__,
    description='Mozilla Ichnaea',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application"
    ],
    keywords="web services",
    author='Mozilla Services',
    author_email='services-dev@mozilla.org',
    url='https://github.com/mozilla/ichnaea',
    license="Apache 2.0",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    tests_require=test_requires,
    test_suite="ichnaea",
    extras_require={'test': test_requires},
    entry_points="""\
    [paste.app_factory]
    main = ichnaea:main
    [console_scripts]
    ichnaea_import = ichnaea.importer:console_entry
    """,
)
