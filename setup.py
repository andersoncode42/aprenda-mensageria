from setuptools import setup

setup(
    name="meu-projeto",
    version="0.1.0",
    description="Um exemplo de pacote python",
    packages=["model"],
    package_dir={"": "src"}, # Indica que os pacotes estão na pasta src
    install_requires=[],
)