==========
Rubaialter
==========

*A module for altering numerical dataset's formats, made on top of Pandas*

.. image:: https://img.shields.io/badge/build-beta-brightgreen
   :target: https://github.com/TechLearnersInc/rubaialter

.. image:: https://img.shields.io/badge/license-MIT-green
   :target: LICENSE.txt

.. image:: https://img.shields.io/static/v1?label=Created%20with%20%E2%9D%A4%EF%B8%8F%20by&message=TechLearners&color=red
   :target: https://github.com/TechLearnersInc

Introduction
------------
This module is written on top of Pandas to alter a numerical dataset into different formats quickly. From now,  alteration of dataset formats is as exciting as writing a poem. So, write a poem and create magic with data, one step faster with this module.

:code:`rubaialter` is a module that will perform conversions among these :code:`.csv ,.xlsx, .xls, .sqlite3` file formats using Pandas under the hood.

Example::

    $ rubaialter dataset.xlsx --csv

:code:`pip install rubaialter` will automatically create an
executable script in your :code:`Scripts/` folder, so you
should be able to simply::

    $ rubaialter dataset.csv --xlsx

or even::

    $ rubaialter *.csv --xlsx

You can type::

    $ rubaialter -h

to obtain the following CLI::

    usage: rubaialter.py [-h] [--csv] [--xls] [--xlsx] [--sqlite]
                         [--force] filenames [filenames ...]

    A module for altering datasets formats made on top of Pandas

    positional arguments:
    filenames   .csv, .xls, .xlsx, .sqlite3

    optional arguments:
    -h, --help  show this help message and exit
    --csv       Convert to csv
    --xls       Convert to xls
    --xlsx      Convert to xlsx
    --sqlite    Convert to sqlite
    --force     Enable overwriting
