from setuptools import setup

setup(
    name="aprenda-mensageria",
    version="0.0.1",
    description="Uma tentativa de pacote python para testar mensageria",
    packages=["model", "mensageria"],
    # Indica que os pacotes estão na pasta src
    package_dir={"": "src"},
    install_requires=[],
)