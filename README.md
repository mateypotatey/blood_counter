## Python script to process scilVet ABC plus xml files and generate a .csv file
### If you have a scil Vet abc Plus machine and are struggling with formatting the generated xml files to .csv, this script will help you

scil Vet abs Plus: https://www.scilvet.com/products/laboratory-diagnostics/productrange/hematology/product/scil-vet-abc-plus

The manufacturer provides a powershell file to generate an excel spreadsheet but this has proven to be unreliable.
This script generates temporary json files from the .xml files and then puts them into a pandas dataframe.

The resulting data is exported as a .csv file, the temporary json files are deleted and the processed .xml files are moved to a "processed directory".

The results are stored in a new folder with the current date, saved as a file with the current date and time.


Libraries required:
lxml==4.9.3
numpy==1.25.1
pandas==2.0.3
python-dateutil==2.8.2
pytz==2023.3
six==1.16.0
tzdata==2023.3
xmltodict==0.13.0

Install the necessary libraries using:
pip install -r requirements.txt

Included in this repo are also a number of example .xml files to show how it works.