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

def find():
    global dic1
    x = input("Enter name: ")
    for key in dic1:
        for j in range(len(key)):
            if x.capitalize() == key[:j+1]:
                print(key+"\t\taddress: "+dic1[key]['address']+"\t\temail: "+dic1[key]['email']+"\t\tphone_no: "+str(dic1[key]['phone_no']))

def find_by_email_or_numbers():
    global dic1
    x = input("Enter email or number: ")
    if x.isdigit():
        for key in dic1:
            if int(x)==dic1[key]['phone_no']:
                print(key+"\t\taddress: "+dic1[key]['address']+"\t\temail: "+dic1[key]['email']+"\t\tphone_no: "+str(dic1[key]['phone_no']))
                break
            else:
                print("Phone number not found")
                break
    else:
        for key in dic1:
            if x==dic1[key]['email']:
                print(key+"\t\taddress: "+dic1[key]['address']+"\t\temail: "+dic1[key]['email']+"\t\tphone_no: "+str(dic1[key]['phone_no']))
                break
            else:
                print("Email not found")
                break

def merge():
    global dic1
    dic2 = {}
    file = input("Enter path of file: ")
    f1 = open(file,'r')
    for i in f1:
        elements=i.split('\t\t')
        names=elements[0].split(': ')
        adds=elements[1].split(': ')
        emails=elements[2].split(': ')
        phones=elements[3].split(':')
        dic2.update({names[1]:{adds[0]:adds[1],emails[0]:emails[1],phones[0]:int(phones[1])}})
    dic1.update(dic2)


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
file = "/Users/saksham/Desktop/Programming/CSE101 - IP/A2/address_book.txt"
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
    3. Find (f)
    4. Search using phone number or email (s)
    5. Merge another address book (m)
    5. Exit (e)
""")
    if selector=='a':
        add_entry()
    elif selector=='d':
        delete_entry()
    elif selector=='f':
        find()
    elif selector=='s':
        find_by_email_or_numbers()
    elif selector=='m':
        merge()
    elif selector=='e':
        exit_func(file)
        flag = False
    else:
        print('invalid input, terminating')
        flag = False
