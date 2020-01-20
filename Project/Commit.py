import time
import json
print("Welcome to Warehouse Management System select an option to continue")

data = {}
try:
    with open("data.json","r") as f:
        data = json.load(f)
except:
    
    with open("data.json","w+") as f:
        f.write("""{"0":{}}""") # So that json doesnt misbehave

while True:
    time.sleep(1)
    print("------------------ MENU ------------------")
    time.sleep(1)
    options = """
  1. Search Available Product By Code           3. Search Available Product By Manufacturer Name
  2. Search Available Product By ptype          4. Search Available Product By Product Name
  5. Search product by location                 6. Print All Available Products
  7. Add New Product                            8. Exit

Select An Option To Continue: """
    
    try:
        option = int(input(options))
        time.sleep(1)
        if option not in range(1,9):
            raise ValueError
        if option == 1:
            x = input("Enter Code: ")
            print("Checking for Codes :")
            for ptype in data:
                for Manufacturer in data[ptype]:
                    for Code in data[ptype][Manufacturer]:
                        if Code.lower().startswith(x.lower()):
                            print(Code,Manufacturer,sep="-")
                    else:
                        print("Sorry! Code Not Assigned")
            print("_____________________________\n\n")
            
        elif option == 2:
            options = {}
            counter = 1
            for ptype in data:
                if ptype != "0":
                    options[counter] = ptype
                    print(str(counter)+":"+ptype,end="\t\t")
                    counter += 1
            print()
            x = 0
            while x not in range(1,5):
                x = int(input("Select ptype(1-4): "))
            
            print("Available Codes in ptype:")
            print("Code | Manufacturer")
            for Manufacturer in data[options[x]]:
                for Code in data[options[x]][Manufacturer]:
                    print(Code,Manufacturer,sep=" | ")
            print("____________________________\n\n")
        elif option == 3:
            x = input("Enter Manufacturer Name: ")
            print("\nAvailable Codes are:")
            print("Code | Manufacturer")
            avail = False
            for ptype in data:
                for Manufacturer in data[ptype]:
                    
                    if Manufacturer.lower().startswith(x.lower()):
                        for Code in data[ptype][Manufacturer]:
                            avail = True
                            print(Code,Manufacturer,sep=" | ")
            if not avail:
                print("Product not available")
            print("_____________________________\n\n")
            
        elif option == 4:
            x = input("Enter Product Name: ")
            print("\nAvailable Product are:")
            avail = False
            print("Product Name | Code | Manufacturer")
            for ptype in data:
                for Manufacturer in data[ptype]:
                    for Code in data[ptype][Manufacturer]:
                        for Product in data[ptype][Manufacturer][Code]:
                            
                            if Product.lower().startswith(x.lower()):
                                print(Product,Code,Manufacturer,sep=" | ")
                                avail = True
            if not avail:
                print("No Product Found")
            print("___________________________\n\n")

        elif option ==5:
            x=input("Enter location: ")
            print("\nAvailable Products are:")
            print("Product Name | Code | Manufacturer")
            n=""
            m = n.join(str(ord(c)) for c in x)
            m =int(m)
            for ptype in data:
                for Manufacturer in data[ptype]:
                    for Code in data[ptype][Manufacturer]:
                        for location in data[ptype][Manufacturer][Code]:
                            for Product in data[ptype][Manufacturer][Code][m]:
                                if Product.lower().startswith(x.lower()):
                                
                                    print(Product,Code,Manufacturer,sep=" | ")
                                    avail = True


        elif option == 6:
            print("Product Name | Code | Manufacturer")
            for ptype in data:
                print("\nptype: "+ptype,end="\n\n")
                for Manufacturer in data[ptype]:
                    for Code in data[ptype][Manufacturer]:
                        for Product in data[ptype][Manufacturer][Code]:
                            print(Product,Code,Manufacturer,sep=" | ")
            print("____________________________\n\n")
            
        elif option == 7:
            ptype = input("ptype name:")
            try:
                x = data[ptype]
            except: 
                data[ptype]= {}
            Manufacturer = input("Manufacturer name:")
            try:
                x = data[ptype][Manufacturer]
            except: 
                data[ptype][Manufacturer]= {}
            Code = input("Code:")
            try:
                x = data[ptype][Manufacturer][Code]
            except: 
                data[ptype][Manufacturer][Code]= {}
            Product = input("Product(comma seperated):")
            try:
                data[ptype][Manufacturer].update({Code:Product.split(",")})
            except:
                data[ptype][Manufacturer]={}
                data[ptype][Manufacturer].update({Code:Product.split(",")})
                
            location =input("Location Code: ")
            try:
                n=""
                m = n.join(str(ord(c)) for c in location)
                m =int(m)
                data[ptype][Manufacturer].update({[m]:({Code:Product.split(",")})})
            except:
                data[ptype][Manufacturer]={}
                data[ptype][Manufacturer].update({location:({Code:Product.split(",")})})
            with open("data.json","w") as file:
                json.dump(data,file)
            print("Added Product To Record List")
            print("____________________________\n\n")


        elif option == 8:
            print("This program is sponsored by : RAID Shadow Legends")
            break
    except ValueError:
        print("Invalid Option, Try Again \n")
        continue