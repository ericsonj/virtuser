import setuptools

setuptools.setup(
    name="virtuser",
    version="1.0.0rc1",
    author="Ericson Joseph",
    author_email="ericsonjoseph@gmail.com",
    description="Create and handle virtual users shells",
    scripts=['scripts/virtuser'],
    url="https://github.com/ericsonj/virtuser",
    license="MIT",
    packages=setuptools.find_packages(),
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
