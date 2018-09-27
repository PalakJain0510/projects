import csv
from os import path

def getCSVData(fileName):
    """
    method to read csv data from csv file

    * :param fileName: name of file
    * :return: rows of file

    """

    try:
        # create an empty list to store rows
        rows = []
        # open the CSV file
        dataFile = open(fileName, "r")
        # create a CSV Reader from CSV file
        if (path.exists(fileName)):
            print("file exists")
            reader = csv.reader(dataFile)
            # skip the headers
            next(reader)
            for row in reader:
                rows.append(row)
            return rows
        else:
            print("file not found")
    except Exception as e:
        print(e+"exception")