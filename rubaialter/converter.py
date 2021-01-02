import os
from rubaialter.csv_to import csv_to_sqlite, csv_to_xls, csv_to_xlsx
from rubaialter.sqlite_to import sqlite_to_csv, sqlite_to_xls, sqlite_to_xlsx
from rubaialter.xls_xlsx_to import (
    xls_to_csv,
    xls_to_sqlite,
    xlsx_to_csv,
    xlsx_to_sqlite,
    xlsx_to_xls,
    xls_to_xlsx,
)


def toCSV(inputFilePath: str):
    filename, file_extension = os.path.splitext(
        os.path.basename(inputFilePath)
    )  # Get File Name & Extension

    if file_extension == ".csv":
        print("The file is already in csv format.")
    elif file_extension == ".sqlite3":
        sqlite_to_csv(inputFilePath)
    elif file_extension == ".xls":
        xls_to_csv(inputFilePath)
    elif file_extension == ".xlsx":
        xlsx_to_csv(inputFilePath)


def toSQLite(inputFilePath: str):
    filename, file_extension = os.path.splitext(
        os.path.basename(inputFilePath)
    )  # Get File Name & Extension

    if file_extension == ".sqlite3":
        print("The file is already in sqlite3 format.")
    elif file_extension == ".csv":
        csv_to_sqlite(inputFilePath)
    elif file_extension == ".xls":
        xls_to_sqlite(inputFilePath)
    elif file_extension == ".xlsx":
        xlsx_to_sqlite(inputFilePath)


def toXLSX(inputFilePath: str):
    filename, file_extension = os.path.splitext(
        os.path.basename(inputFilePath)
    )  # Get File Name & Extension

    if file_extension == ".xlsx":
        print("The file is already in xlsx format.")
    elif file_extension == ".sqlite3":
        sqlite_to_xlsx(inputFilePath)
    elif file_extension == ".xls":
        xls_to_xlsx(inputFilePath)
    elif file_extension == ".csv":
        csv_to_xlsx(inputFilePath)


def toXLS(inputFilePath: str):
    filename, file_extension = os.path.splitext(
        os.path.basename(inputFilePath)
    )  # Get File Name & Extension

    if file_extension == ".xls":
        print("The file is already in xls format.")
    elif file_extension == ".sqlite3":
        sqlite_to_xls(inputFilePath)
    elif file_extension == ".csv":
        csv_to_xls(inputFilePath)
    elif file_extension == ".xlsx":
        xlsx_to_xls(inputFilePath)
