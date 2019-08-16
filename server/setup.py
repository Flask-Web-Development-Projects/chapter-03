from setuptools import setup

required = [
    "flask-api==1.1",
    "flask-cors==3.0.7",
    "flask-httpauth==3.2.4",
    "flask-migrate==2.4.0",
    "flask-script==2.0.6",
    "passlib==1.7.1"
]

setup(
    name="catalog",
    packages=["catalog"],
    include_package_data=True,
    install_requires=required
)