from setuptools import find_packages, setup


def get_requirements():
    with open("requirements.txt") as f:
        required_packages = f.read().splitlines()
        return required_packages


setup(
    name="YAFADEI",
    version="1.0.0",
    description="Website For Artists",
    url="https://github.com/odyyyy/YAFADEI",
    packages=find_packages(),
    include_package_data=True,
    install_requires=get_requirements(),
)
