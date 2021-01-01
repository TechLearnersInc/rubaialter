import os
import sys
import shutil
import pytest
import pandas
import subprocess

inputFileCSV: str = "datasets/test.csv"
outputFileCSV: str = "test.csv"

inputFileXLS: str = "datasets/test.xls"
outputFileXLS: str = "test.xls"

inputFileXLSX: str = "datasets/test.xlsx"
outputFileXLSX: str = "test.xlsx"

inputFileSQLITE3: str = "datasets/test.sqlite3"
outputFileSQLITE3: str = "test.sqlite3"


def test_prepare():
    try:
        shutil.rmtree("rubaialter")
    except FileNotFoundError:
        pass
    shutil.copytree("../rubaialter", "rubaialter")


def test_csv_to_csv():
    global inputFileCSV, outputFileCSV
    shutil.copyfile(inputFileCSV, outputFileCSV)
    output = subprocess.check_output(
        ["python", "-m", "rubaialter", inputFileCSV, "--csv"]
    )
    output = output.decode("utf-8").strip()
    os.remove(outputFileCSV)
    assert output == "The file is already in csv format."


def test_csv_to_xls():
    global inputFileCSV, outputFileCSV
    subprocess.check_call(["python", "-m", "rubaialter", inputFileCSV, "--xls"])
    assert os.path.exists(outputFileXLS)
    os.remove(outputFileXLS)


def test_clean():
    shutil.rmtree("rubaialter")
