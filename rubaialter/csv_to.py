import os
import sqlite3
import pandas as pd


def csv_to_xlsx(inputFilePath: str, extension="xlsx"):
    print(f"Processing is in progress ...")
    df = pd.read_csv(inputFilePath)  # Read CSV
    filename, file_extension = os.path.splitext(
        os.path.basename(inputFilePath)
    )  # Get File Name & Extension
    newFileName = filename + f".{extension}"
    convertedDataframe = pd.ExcelWriter(newFileName)
    df.to_excel(convertedDataframe, index=False)  # Convert to xlsx
    convertedDataframe.save()  # Save File in Converted Format
    print(f"All process done. {newFileName} is ready!")


def csv_to_xls(inputFilePath: str):
    csv_to_xlsx(inputFilePath, extension="xls")


def csv_to_sqlite(inputFilePath: str):
    print(f"Processing is in progress ...")
    df = pd.read_csv(inputFilePath)  # Read CSV
    filename, file_extension = os.path.splitext(
        os.path.basename(inputFilePath)
    )  # Get File Name & Extension
    newFileName = filename + ".sqlite3"
    conn = sqlite3.connect(newFileName)
    df.to_sql(name=filename, con=conn)
    conn.commit()
    print(f"All process done. {newFileName} is ready!")
    conn.close()


if __name__ == "__main__":
    os.system("clear")
    pass
