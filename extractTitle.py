import csv
import json

with open('cia.json') as json_data:
    cia_data = json.load(json_data)

    writeToCsv = csv.writer(open("cia_title.txt", "w+"))

    # writeToCsv.writerow([ 'Explanation_A', 'Explanation_B', 'Explanation_C', 'Explanation_D'])

    for cia_data in cia_data:
        writeToCsv.writerow([
            cia_data["source"]["stuName"] + " Topic: " + cia_data["source"]["topicNumber"] + " " + cia_data["source"]["topicName"]
        ])