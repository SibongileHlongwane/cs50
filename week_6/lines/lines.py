from sys import argv
from sys import exit
from pathlib import Path

if len(argv) > 2:
    exit("Too many command-line arguments")
    
if len(argv) < 2:
    exit("Too few command-line arguments")
    
test_file = argv[1]

if not test_file.endswith(".py"):
    exit("Not a python file")
    
if not Path(test_file).exists():
    exit("File does not exist")

with open(test_file, "r") as file:
    count = 0
    for row in file:
        if row.lstrip().startswith("#") or row.strip() == "":
            continue
        count += 1
    print(count)