def add_entry():
    global dic1
    name = input("Enter name: ")
    add = input("Enter address: ")
    email = input("Enter email: ")
    phone = int(input("Enter phone no: "))

    dic1.update({name:{'address':add,'email':email,'phone_no':phone}})

def exit_func(file_name):
    global dic1
    f = open(file_name,'w+')
    for key in dic1:
        f.write("name: "+key+"\t\taddress: "+dic1[key]['address']+"\t\temail: "+dic1[key]['email']+"\t\tphone_no: "+str(dic1[key]['phone_no'])+'\n')

def delete_entry():
    global dic1
    while True:
        key = input("Enter name('exit' to go back): ")
        if key in dic1:
            del dic1[key]
            break
        elif key=="exit":
            break
        else:
            print("name doesn't exist in address book")

dic1 = {}
file = "CSE101 - IP/A2/address_book.txt"
f1 = open(file,'r')
for i in f1:
    elements=i.split('\t\t')
    names=elements[0].split(': ')
    adds=elements[1].split(': ')
    emails=elements[2].split(': ')
    phones=elements[3].split(':')
    dic1.update({names[1]:{adds[0]:adds[1],emails[0]:emails[1],phones[0]:int(phones[1])}})

flag = True
while flag:
    selector = input("""Enter the operation:
    1. Add entry (a)
    2. Delete entry (d)
    3. Exit (e)
""")
    if selector=='a':
        add_entry()
    elif selector=='d':
        delete_entry()
    elif selector=='e':
        exit_func(file)
        flag = False
