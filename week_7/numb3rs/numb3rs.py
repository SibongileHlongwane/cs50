import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^(?:0|[1-9]\d{0,2})\.(?:0|[1-9]\d{0,2})\.(?:0|[1-9]\d{0,2})\.(?:0|[1-9]\d{0,2})$"
    match = re.search(pattern, ip)
    
    if match:
        for part in ip.split("."):
            if not 0 <= int(part)<= 255:
                return False
        return True
    else:
        return False
                
if __name__ == "__main__":
    main()