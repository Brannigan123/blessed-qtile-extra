from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Custom widgets for qtile wm'
LONG_DESCRIPTION = 'Custom widgets for qtile wm'

packages = find_packages()
package_data = {package: ["py.typed"] for package in packages}


setup(
    name="qtile_b_widgets",
    version=VERSION,
    author="Brannigan Sakwah",
    author_email="<brannigansakwah@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=packages,
    package_data=package_data,
    install_requires=[
        'qtile',
    ],
    keywords=['python', 'qtile', 'config', 'widget'],
)
