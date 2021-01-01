import argparse
import logging
import os
import pathlib
import sys
from rubaialter import converter

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


class rubaialter:
    def __init__(self) -> None:
        self.__args = self.__Arguments()
        self.__Checking()
        self.__Conversion()

    # Arguments Parser ↓
    def __Arguments(self):
        parser = argparse.ArgumentParser(
            description="A module for altering datasets formats made on top of Pandas"
        )

        # Taking Files ↓
        parser.add_argument(
            "filenames",
            type=pathlib.Path,
            nargs="+",
            help=".csv, .xls, .xlsx, .sqlite3",
        )

        # To CSV ↓
        parser.add_argument(
            "--csv",
            default=False,
            action="store_true",
            help="Convert to csv",
        )

        # To XLS ↓
        parser.add_argument(
            "--xls",
            default=False,
            action="store_true",
            help="Convert to xls",
        )

        # To XLSX ↓
        parser.add_argument(
            "--xlsx",
            default=False,
            action="store_true",
            help="Convert to xlsx",
        )

        # To SQLITE ↓
        parser.add_argument(
            "--sqlite",
            default=False,
            action="store_true",
            help="Convert to sqlite",
        )

        # Force ↓
        parser.add_argument(
            "--force",
            default=False,
            action="store_true",
            help="Enable overwriting",
        )
        print(parser.parse_args().__dict__)
        return parser.parse_args().__dict__

    # Received File Checking ↓
    def __Checking(self):
        valid: bool = True
        extensions: tuple = (".csv", ".xls", ".xlsx", ".sqlite3")

        for file in self.__args.get("filenames"):
            if not os.path.exists(file):
                logging.error(f'"{file}" doesn\'t exist.')
                valid = False
            if not os.path.isfile(file):
                logging.error(f'"{file}" is not a file')
                valid = False
            if os.path.splitext(file)[-1] not in extensions:
                logging.error(f'"{file}" is not a valid file')
                valid = False

        if not valid:
            sys.exit(-1)

    # Conversion ↓
    def __Conversion(self):
        for file in self.__args.get("filenames"):
            if self.__args.get("csv"):
                converter.toCSV(inputFilePath=file)
            if self.__args.get("xls"):
                converter.toXLS(inputFilePath=file)
            if self.__args.get("xlsx"):
                converter.toXLSX(inputFilePath=file)
            if self.__args.get("sqlite3"):
                converter.toSQLite(inputFilePath=file)


def main():
    try:
        rubaialter()
    except Exception as e:
        logging.error(e)


if __name__ == "__main__":
    print("Hello World")
