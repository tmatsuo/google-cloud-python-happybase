import os

from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()


REQUIREMENTS = [
    'gcloud',
]

setup(
    name='google-cloud-happybase',
    version='0.19.0',
    description='API Client library for Google Cloud Happybase layer',
    author='Google Cloud Platform',
    author_email='jjg+gcloud-python@google.com',
    long_description=README,
    scripts=[],
    url='https://github.com/GoogleCloudPlatform/gcloud-python',
    license='Apache 2.0',
    platforms='Posix; MacOS X; Windows',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['google', 'google.cloud'],
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet',
    ]
)
