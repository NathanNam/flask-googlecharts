from setuptools import setup

extra = {}
install_requires = ['Flask>=0.10.1']
setup(
    name='Flask-GoogleCharts',
    version='0.0.1',
    url='http://github.com/wikkiewikkie/flask-googlecharts/',
    license='MIT',
    author='Kevin Schellenberg',
    author_email='wikkiewikkie@gmail.com',
    description='Google Charts API support for Flask',
    long_description=__doc__,
    py_modules=['flask_googlecharts'],
    zip_safe=False,
    platforms='any',
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: JavaScript',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    **extra
)