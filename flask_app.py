from flask import Flask
from flask import render_template
import csv
app = Flask(__name__)

@app.route("/")
@app.route("/1")
def page1():
    list_data_1 = []
    list_data_2 = []
    list_data_3 = []
    with open("./csv/API_NY.GDP.PCAP.CD_DS2_en_csv_v2_612482.csv", "r", encoding="utf-8") as csv_file:
        file_data = csv.reader(csv_file)
        rows_raw = [row for row in file_data]
        rows = rows_raw[2:]
        for row in rows:
            list_data_1.append(row)
    with open("./csv/API_AG.LND.FRST.ZS_DS2_en_csv_v2_612513.csv", "r", encoding="utf-8") as csv_file:
        file_data = csv.reader(csv_file)
        rows_raw = [row for row in file_data]
        rows = rows_raw[2:]
        for row in rows:
            list_data_2.append(row)
    with open("./csv/API_EN.ATM.PM25.MC.M3_DS2_en_csv_v2_616933.csv", "r", encoding="utf-8") as csv_file:
        file_data = csv.reader(csv_file)
        rows_raw = [row for row in file_data]
        rows = rows_raw[2:]
        for row in rows:
            list_data_3.append(row)
    return render_template("page1.html", prev="#", next="/2", list_data_1=list_data_1, list_data_2=list_data_2, list_data_3=list_data_3)


@app.route("/2")
def page2():
    list_data_1 = []
    with open("./csv/pm25.csv", "r", encoding="utf-8") as csv_file:
        file_data = csv.reader(csv_file)
        rows_raw = [row for row in file_data]
        rows = rows_raw[1:]
        for row in rows:
            list_data_1.append(row)
    return render_template("page2.html", prev="/1", next="/3", list_data_1=list_data_1)


@app.route("/3")
def page3():
    list_data_1 = []
    list_data_2 = []
    list_data_3 = []
    with open("./csv/GDP.csv", "r", encoding="utf-8") as csv_file:
        file_data = csv.reader(csv_file)
        rows_raw = [row for row in file_data]
        rows = rows_raw[2:]
        for row in rows:
            list_data_1.append(row)
    with open("./csv/forest.csv", "r", encoding="utf-8") as csv_file:
        file_data = csv.reader(csv_file)
        rows_raw = [row for row in file_data]
        rows = rows_raw[2:]
        for row in rows:
            list_data_2.append(row)
    with open("./csv/PM2.5.csv", "r", encoding="utf-8") as csv_file:
        file_data = csv.reader(csv_file)
        rows_raw = [row for row in file_data]
        rows = rows_raw[2:]
        for row in rows:
            list_data_3.append(row)
    return render_template("page3.html", prev="/2", next="/4", list_data_1=list_data_1, list_data_2=list_data_2, list_data_3=list_data_3)


@app.route("/4")
def page4():
    list_data_1 = []
    list_data_2 = []
    with open("./csv/API_NY.GDP.PCAP.CD_DS2_en_csv_v2_612482.csv", "r", encoding="utf-8") as csv_file:
        file_data = csv.reader(csv_file)
        rows_raw = [row for row in file_data]
        rows = rows_raw[2:]
        for row in rows:
            list_data_1.append(row)
    with open("./csv/PM2.5.csv", "r", encoding="utf-8") as csv_file:
        file_data = csv.reader(csv_file)
        rows_raw = [row for row in file_data]
        rows = rows_raw[2:]
        for row in rows:
            list_data_2.append(row)
    return render_template("page4.html", prev="/3", next="#", list_data_1=list_data_1, list_data_2=list_data_2)


if __name__ == "__main__":
    app.run()
