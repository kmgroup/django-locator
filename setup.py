from setuptools import setup


setup(
    name='django-locator',
    version='1.0.0',
    license='Simplified BSD',

    install_requires = [
        'Django',
    ],

    description='An easy to integrate store locator plugin for Django.',
    long_description=open('README.md').read(),

    author='Isaac Bythewood',
    author_email='isaac@bythewood.me',

    url='http://github.com/overshard/django-locator',
    download_url='http://github.com/overshard/django-locator/downloads',

    include_package_data=True,

    packages=['locator'],

    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
