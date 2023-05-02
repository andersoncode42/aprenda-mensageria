from setuptools import setup

# OLD
"""
setup(
    name="aprenda-mensageria",
    version="0.0.1",
    description="Uma tentativa de pacote python para testar mensageria",
    packages=["model", "mensageria"],
    # Indica que os pacotes estão na pasta src
    package_dir={"": "src"},
    install_requires=[],
)
"""

setup(
    name="aprenda-mensageria",
    version="0.0.1",
    description="Uma tentativa de pacote python para testar mensageria",
    packages=find_packages('src'),
    package_dir={"": "src"},
    install_requires=["pika~=1.3.1"],
)
