import setuptools

with open("README", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="uberduct",
    version="0.0.2",
    author="Zach Wener",
    author_email="info@uberduck.ai",
    data_files=[
        ("dict", ["src/uberduct/dict/cmudict.dict"]),
    ],
    description="Augmenting the CMU dictionary",
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/uberduck-ai/uberdict",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    package_data={"": ["cmu*"]},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
