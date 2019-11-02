import setuptools

with open("project-description.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyserini",
    version="0.6.0_3",
    author="Jimmy Lin",
    author_email="jimmylin@uwaterloo.ca",
    description="Python interface to Anserini",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/castorini/pyserini",
    install_requires=['Cython', 'pyjnius'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)