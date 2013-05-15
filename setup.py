from setuptools import setup
import textwrap

setup(
    name='python-actionkit',
    version='0.1',
    author='Nick Catalano',
    packages=['actionkit',],
    url='https://github.com/neworganizing/python-actionkit',
    license='APACHE',
    description="python-actionkit is a python interface to the ActionKit ECRM. The goal is to provide simple access to ActionKid via the the REST and XML-RPC APIs as well as the Django ORM",
    long_description=textwrap.dedent(open('README.rst', 'r').read()),
    install_requires=[
        'requests',
    ],
    keywords = "python actionkit",
    classifiers=['Development Status :: 4 - Beta', 'Environment :: Console', 'Intended Audience :: Developers', 'Natural Language :: English', 'Operating System :: OS Independent', 'Topic :: Internet :: WWW/HTTP'],
)