import csv

new_data_dict = {}
with open("data.csv", 'r') as data_file:
    data = csv.DictReader(data_file, delimiter=",")
    for row in data:
        item = new_data_dict.get(row["UID"], dict())
        item[row["BID"]] = int(row["R"])
        item[row["A"]] = row["L"]

        new_data_dict[row["UID"]] = item

print (new_data_dict)
