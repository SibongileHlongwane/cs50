import re
import sys

def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError as e:
        sys.exit(f"ValueError: {e}")

def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.search(pattern, s, re.IGNORECASE)

    if not match:
        raise ValueError("Invalid time format")
    
    start_hour_str, start_minute_str, start_period, \
    end_hour_str, end_minute_str, end_period = match.groups()
    
    def _convert_single(hour_str, minute_str, period):
        hour = int(hour_str)
        minute = int(minute_str) if minute_str else 0

        if not (1 <= hour <= 12 and 0 <= minute <= 59):
            raise ValueError("Invalid time values")

        if period.upper() == "PM" and hour != 12:
            hour += 12
        elif period.upper() == "AM" and hour == 12:
            hour = 0
        
        return f"{hour:02}:{minute:02}"
    
    try:
        start_time = _convert_single(start_hour_str, start_minute_str, start_period)
        end_time = _convert_single(end_hour_str, end_minute_str, end_period)
        return f"{start_time} to {end_time}"
    except ValueError as e:
        raise ValueError(f"Invalid time values: {e}")
        
if __name__ == "__main__":
    main()

