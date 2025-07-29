months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
  
while True:
    date = input("Date: ").strip().title()
    try:
        if "/" in date:
            m, d, y = date.split("/")
            m, d, y = int(m.strip()), int(d.strip()), int(y.strip())
        else:
            if "," not in date:
                raise ValueError
            parts = date.replace(",", "").split()
            if len(parts) != 3:
                raise ValueError
            month_name = parts[0].title()
            d, y = parts[1], parts[2]
            m = months.index(month_name) + 1
            d, y = int(d.strip()), int(y.strip())
            
        if 1 <= m <= 12 and 1 <= d <= 31:
            print(f"{y:04}-{m:02}-{d:02}")
            break
    except(ValueError, IndexError, AttributeError):
        pass
           
            
                 


  