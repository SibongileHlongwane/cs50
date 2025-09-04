from sys import argv, exit
import csv

if len(argv) > 3:
    exit("Too many command-line arguments")
    
if len(argv) < 3:
    exit("Too few command-line arguments")   
    
before, after = argv[1], argv[2]
   
try:
    with open(before, "r") as input_file:   
        reader = csv.DictReader(input_file)
        
        with open(after, "w", newline="") as output_file:  
            writer = csv.DictWriter(output_file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            
            for row in reader:
                last, first = row["name"].split(", ")
                writer.writerow({"first": first.strip(), "last": last.strip(), "house": row["house"]})
except FileNotFoundError:
    exit(f"Could not read {before}")
      