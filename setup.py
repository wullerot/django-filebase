from setuptools import find_packages, setup
from filebase import __version__

setup(
    name='filebase',
    version=__version__,
    url='http://github.com/bnzk/django-filebase',
    author='bnzk, rouxcode',
    author_email='bnzk@bnzk.ch',
    description="File management for django projects. Django 2.2 and up only.",
    license='BSD',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    python_requires='>=3.7',
    install_requires=[
        'Django>=2.2',
        'easy_thumbnails>=2.6',
    ],
    extras_require={
        'tests': [
            'pytest~=4.4',
            "pytest-django~=3.4",
            'coverage~=4.5',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
