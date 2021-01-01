import os
import shutil

from setuptools import find_packages, setup


def main():
    here = os.path.abspath(os.path.dirname(__file__))

    # Get the long description from the relevant file
    long_description = ""
    try:
        with open(os.path.join(here, "README.rst"), encoding="utf-8") as f:
            long_description = f.read()
    except:
        pass

    setup(
        name="rubaialter",
        # Versions should comply with PEP440.  For a discussion on single-sourcing
        # the version across setup.py and the project code, see
        # http://packaging.python.org/en/latest/tutorial.html#version
        version="1.0.0b1",
        description="Convert .py and .pyx to (.pyd | .so) very easily.",
        long_description=long_description,
        long_description_content_type="text/x-rst",
        # The project's main homepage.
        url="https://github.com/TechLearnersInc/rubaialter",
        # Author details
        author="Muhammad Sakib Khan Inan",
        author_email="sakib.khaninan@gmail.com",
        # Choose your license
        license="MIT",
        # Minimum Python version required
        python_requires=">=3.6",
        # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
        project_urls={
            "Source": "https://github.com/TechLearnersInc/rubaialter",
            "Tracker": "https://github.com/TechLearnersInc/rubaialter/issues",
            "Facebook": "https://www.facebook.com/TechLearnersInc",
            "Linkedin": "https://www.linkedin.com/company/techlearners/",
            "Telegram": "https://t.me/TechLearners",
        },
        classifiers=[
            # How mature is this project? Common values are
            #   3 - Alpha
            #   4 - Beta
            #   5 - Production/Stable
            "Development Status :: 4 - Beta",
            "Environment :: Console",
            # Indicate who your project is intended for
            "Intended Audience :: Developers",
            "Intended Audience :: Science/Research",
            "Topic :: Utilities",
            # Pick your license as you wish (should match "license" above)
            "License :: OSI Approved :: MIT License",
            # Specify the Python versions you support here. In particular, ensure
            # that you indicate whether you support Python 2, Python 3 or both.
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
        ],
        # What does your project relate to?
        keywords="pandas rubaialter csv xls excel xlsx sqlite sqlite3 converter dataset",
        # You can just specify the packages manually here if your project is
        # simple. Or you can use find_packages().
        packages=find_packages(),
        # List run-time dependencies here. These will be installed by pip
        # when your project is installed. For an analysis of "install_requires"
        # vs pip's requirements files see:
        # https://packaging.python.org/en/latest/technical.html#install-requires-vs-requirements-files
        install_requires=["openpyxl", "pandas", "xlrd", "xlwt"],
        # To provide executable scripts, use entry points in preference to the
        # "scripts" keyword. Entry points provide cross-platform support and allow
        # pip to create the appropriate form of executable for the target platform.
        entry_points={
            "console_scripts": [
                "rubaialter=rubaialter:main",
            ]
        },
    )

    # Cleanup
    try:
        shutil.rmtree("rubaialter.egg-info")
        shutil.rmtree("build")
    except Exception:
        pass


if __name__ == "__main__":
    main()
