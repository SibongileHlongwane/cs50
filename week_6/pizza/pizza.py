import csv 
from sys import argv 
from sys import exit 
from pathlib import Path 
from tabulate import tabulate  

if len(argv) > 2:
    exit("Too many command-line arguments")
    
if len(argv) < 2:
    exit("Too few command-line arguments")
    
test_file = argv[1]

if not test_file.endswith(".csv"):
    exit("Not a csv file")
    
if not Path(test_file).exists():
    exit("File does not exist")
    
with open(test_file, "r",newline="") as sicilian:
    reader = csv.DictReader(sicilian)
    menu = list(reader)
    print(tabulate(menu, headers="keys", tablefmt="grid"))
