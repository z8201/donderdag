import csv

file = "kassa.csv"
kassa = []
boodschappenlijst = {}

with open(file,mode='r',newline='') as fileObj:
    fileCSV = csv.reader(fileObj, delimiter=';')
    header = next(fileCSV)

    for line in fileCSV:
        kassa.append(line)

while True:
    product = input("Geen een product om te scannen, of type 'stop' om de bon te printen: ")
    
    if product.lower() == "stop":
        # bon printen
        print()
    else:
        for line in kassa:
            if product == line[0]:
                aantal = int(input(f"Hoeveel {product} heeft u? "))
                if product in boodschappenlijst:
                    boodschappenlijst[product] += aantal
                else:
                    boodschappenlijst[product] = aantal
                print(f"{product} is {aantal} keer toegevoegd aan boodschappenkar")
                break
        else:
            print(f"{product} komt niet voor, probeer opnieuw.")
