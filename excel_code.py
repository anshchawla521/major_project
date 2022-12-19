import openpyxl
path = "C:/Users/ASUS/Desktop/dataset.xlsx"   # enter path in raw form

dataset = openpyxl.load_workbook(path)

sheet = dataset.active

def check(uniqueid):
    i = 2
    flag = True
    while flag:
        print(i)
        x = sheet.cell(row = i, column= 1)
        # print(x, x.value, type(x.value))
        if x.value == None:
            break
        elif int(x.value) == uniqueid:
            return i
        i += 1
        
    return i

def read(uniqueid):
    present = check(uniqueid)
    if sheet.cell(row = present, column = 1).value == None:
        print("no")
        return False
    else:
        send = dict()
        col = 1
        while col <= 11:
            cell = sheet.cell(row = 1, column = col)
            temp = sheet.cell(row = present, column= col)
            if cell.value == "Student Name":
                send.update({"name":temp.value})
            elif str(cell.value) == "Student ID":
                send.update({"sid":temp.value})
            elif str(cell.value) == "Unique ID":
                send.update({"uid":temp.value})
            elif cell.value == "Student Phone Number":
                send.update({"phone":temp.value})
            col += 1
            if len(send) == 4:
                break
        return send

def write(data):
    present = check(data["uid"])
    # if sheet.cell(row = present, column = 1).value == data["uid"]:
    #     print("present")
    #     return False
    # else:
    col = 1
    while col <= 11:
        print(present)
        cell = sheet.cell(row = 1, column = col)
        temp = sheet.cell(row = present, column= col)
        if cell.value == "Student Name":
            temp.value = data["name"]
        elif str(cell.value) == "Student ID":
            temp.value = data["sid"]
        elif str(cell.value) == "Unique ID":
            temp.value = data["uid"]
        elif cell.value == "Student Phone Number":
            temp.value = data["phone"]
        elif cell.value == "Location":
            temp.value = data["location"]
        col += 1
    return True


print(read(8038593633906583))
write({"name" : "Saksham", "sid" : "19107069", "uid" : "1548976320168423","phone":"7894561238", "location" : "IN"})
print(read(1548976320168423))

dataset.save("dataset1.xlsx")