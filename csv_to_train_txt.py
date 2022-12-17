import csv
with open("./homeriskactivity_hight.csv") as f1:
    kg = csv.reader(f1, delimiter=",")
    header = next(kg)
    with open("./train.txt", "w") as f2:
        for row in kg:
            f2.write("\""+row[0]+"\","+"\""+row[1]+"\",""\""+row[2]+"\"\n")
