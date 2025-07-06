from setuptools import setup, find_packages

setup(
    name="love_lines",
    version="0.1.0",
    description="A sweet library that gives you beautiful love lines ❤️",
    long_description = open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Brooklyn widz",
    url="https://github.com/yourusername/love_lines",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Linguistic",
    ],
    python_requires='>=3.6',
)