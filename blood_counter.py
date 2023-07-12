import json
import xmltodict
import glob
import pandas as pd
import os
import datetime
import shutil

#loads up all xml files in the root directory to be converted to a csv file
xml_list = glob.glob("*.xml")

#create the current date and filename to save the .csv file under
curr_date = str(datetime.date.today())
filename = str(datetime.datetime.now())[:19]

#to make it work on windows, need to replace colons in the filename
filename = filename.replace(":", "-")

#Create the output directory with the current date if it doesn't exist
if os.path.exists("output/" + curr_date):
    pass
elif os.path.exists("output/"):
    os.mkdir("output/" + curr_date)
else:
    os.mkdir("output")
    os.mkdir("output/" + curr_date)

#create the temporary json folder if it doesn't exist
if os.path.exists("temp_jsons"):
    pass
else:
    os.mkdir("temp_jsons")

#create the folder for processed xml files if it doesn't exist
if os.path.exists("processed"):
    pass
else:
    os.mkdir("processed")

#iterate over the xml files in the current directory and convert them to json files
for item in xml_list:
    with open(item, 'r', encoding="utf-8") as myfile:
        obj = xmltodict.parse(myfile.read())
        file_id = obj["lab-result"]["@id"]

    with open("temp_jsons/" + file_id + ".json", "w") as writefile:
        json.dump(obj, writefile)

#list of json files from the current directory that will be put into the dataframe
json_list = glob.glob("temp_jsons/*.json")

#create blank dataframe
df = pd.DataFrame(columns=["Sample No", "Patient ID", "WBC", "LYM#", "MON#", "GRA#", "EOS#", "LYM%", "MON%", "GRA%", "EOS%", "RBC",
                           "HGB", "HCT", "MCV", "MCH", "MCHC", "RDW", "PLT", "MPV"])

#iterate over the json list and add each sample to the dataframe
for item in json_list:
    with open(item) as f:
        
        my_dict = {}
        data = json.load(f)

        sample_name = data["lab-result"]["sample-no"]
        my_dict["Sample No"] = sample_name
        
        try:
            patient_name = data["lab-result"]["patient-no"]
            my_dict["Patient ID"] = patient_name
        except KeyError:
            my_dict["Patient ID"] = ""

        for row in data["lab-result"]["results"]["param"]:
            my_dict[row["name"]] = row["value"]

        df.loc[len(df)] = my_dict

#save the current dataframe to a folder with the current date, named as a file with current date and time
df.to_csv("output/" + curr_date + "/" + filename + ".csv", sep=",")

#delete the temporary json directory
shutil.rmtree("temp_jsons")

#move the processed xml files to the "processed" folder so the root directory is empty again
for item in xml_list:
    shutil.copy(item, "processed/")
    os.remove(item)

