import csv
import itertools

fields = [ 'org', '2015', '2014', '2013' ]
dw     = { 'orgname1': { '2015' : 2, '2014' : 1, '2013' : 1 },
           'orgname2': { '2015' : 1, '2014' : 2, '2013' : 3 },
           'orgname3': { '2015' : 1, '2014' : 3, '2013' : 1 }
        }

with open("test_output.csv", "wb") as f:
    w = csv.DictWriter(f, fields)
    w.writeheader()
    for k in dw:
        w.writerow({field: dw[k].get(field) or k for field in fields})
