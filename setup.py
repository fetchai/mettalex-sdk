import setuptools

setuptools.setup(
    name="Mettalex",
    version="0.0.1",
    author="Mettalex Dev Team",
    author_email="info@mettalex.com",
    description="A package for SDK of Mettalex DEX",
    long_description="An sdk package to perform trades on Mettalex dex",
    long_description_content_type="text/markdown",
    url="https://github.com/fetchai/mettalex-sdk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['pathlib', 'argparse', 'requests', 'web3', 'pandas'],
    python_requires='>=3.0',
)
