from setuptools import setup, find_packages

setup(
    name='oauth-python-twitter',
    version='0.2',
    description='A derivative of twitter.Api class to allow Oauth to be used for authentication.',
    author='Hameedullah Khan',
    author_email='hameed@hameedkhan.net',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: OS Independent',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=['python-twitter>=0.6'],
)
