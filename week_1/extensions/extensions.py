file = input("File name: ").strip().lower()
if "." in file:
    extension = file.split(".")[-1] 
else:
    extension = ""
     

match extension:
    case "gif":
        print("image/gif", end="")
    case "jpg"| "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:    
        print("application/octet-stream")
        


    
