import sys
from setuptools import setup, find_packages

PACKAGE = 'vdw'
VERSION = __import__(PACKAGE).get_version()

install_requires = [
    'django>=1.4.11,<1.5',
    'south==0.8.2',
    'python-memcached==1.48',
    'coverage',
    'rq>=0.3.8',
    'django-rq>=0.5.1',
    'psycopg2==2.4.4',
    'avocado>=2.3.3,<3.0',
    'modeltree>=1.1.7',
    'django-objectset>=0.2.2',
    'django-sts==0.7.3',
    'django-reversion==1.6.6',
    'django-guardian==1.0.4',
    'diff-match-patch',
    'pyvcf>=0.6.5',
]

if sys.version_info < (2, 7):
    install_requires += ['importlib']

kwargs = {
    'name': PACKAGE,
    'version': VERSION,
    'packages': find_packages(exclude=['tests', '*.tests', '*.tests.*',
                                       'tests.*']),
    'include_package_data': True,
    'install_requires': install_requires,
    'test_suite': 'test_suite',
    'tests_require': ['httpretty'],
    'author': 'Byron Ruth',
    'author_email': 'b@devel.io',
    'description': 'Models and loader for processing, storing, and querying genetic data',  # noqa
    'license': 'BSD',
    'keywords': 'vcf varify harvest orm genome',
    'url': 'http://github.com/cbmi/varify-data-warehouse',
    'classifiers': [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Framework :: Django',
        'Topic :: Internet :: WWW/HTTP',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Information Technology',
    ],
}

setup(**kwargs)
