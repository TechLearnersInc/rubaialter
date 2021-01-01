import os
import shutil
import subprocess

# Global Variables ↓
inputFileCSV: str = "datasets/test.csv"
outputFileCSV: str = "test.csv"

inputFileXLS: str = "datasets/test.xls"
outputFileXLS: str = "test.xls"

inputFileXLSX: str = "datasets/test.xlsx"
outputFileXLSX: str = "test.xlsx"

inputFileSQLITE3: str = "datasets/test.sqlite3"
outputFileSQLITE3: str = "test.sqlite3"

# Preparation ↓
def test_prepare():
    try:
        shutil.rmtree("rubaialter")
    except FileNotFoundError:
        pass
    shutil.copytree("../rubaialter", "rubaialter")


# CSV to CSV ↓
def test_csv_to_csv():
    global inputFileCSV, outputFileCSV
    shutil.copyfile(inputFileCSV, outputFileCSV)
    output = subprocess.check_output(
        ["python", "-m", "rubaialter", inputFileCSV, "--csv"]
    )
    output = output.decode("utf-8").strip()
    os.remove(outputFileCSV)
    assert output == "The file is already in csv format."


# CSV to XLS ↓
def test_csv_to_xls():
    global inputFileCSV, outputFileXLS
    subprocess.check_call(["python", "-m", "rubaialter", inputFileCSV, "--xls"])
    assert os.path.exists(outputFileXLS)
    os.remove(outputFileXLS)


# CSV to XLSX ↓
def test_csv_to_xlsx():
    global inputFileCSV, outputFileXLSX
    subprocess.check_call(["python", "-m", "rubaialter", inputFileCSV, "--xlsx"])
    assert os.path.exists(outputFileXLSX)
    os.remove(outputFileXLSX)


# CSV to SQLITE3 ↓
def test_csv_to_sqlite3():
    global inputFileCSV, outputFileSQLITE3
    subprocess.check_call(["python", "-m", "rubaialter", inputFileCSV, "--sqlite3"])
    assert os.path.exists(outputFileSQLITE3)
    os.remove(outputFileSQLITE3)


# Cleanup ↓
def test_clean():
    shutil.rmtree("rubaialter")