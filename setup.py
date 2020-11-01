import setuptools

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

#https://www.alura.com.br/artigos/como-publicar-seu-codigo-python-no-pypi
setuptools.setup(
    name="teste-joaoEstrela", # Replace with your own username
    version="0.0.31",
    author="JoaoEstrela",
    author_email="jaoestrella@hotmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)