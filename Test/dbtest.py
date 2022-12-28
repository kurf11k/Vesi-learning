import pyodbc

def create_connection():
    connection = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-E0N6A66\\SQLEXPRESS;'
                        'Database=TestName;'
                        'Trusted_Connection=yes;')
    
    return connection

def add_new_person(name):
    connection = create_connection()
    cursor = connection.cursor()
    insert_command = 'INSERT INTO Person(name) VALUES(?)'
    cursor.execute(insert_command, name)
    connection.commit()
    cursor.close()
    connection.close()

def list_persons():
    connection = create_connection()
    cursor = connection.cursor()
    read_command = "SELECT name FROM Person"
    cursor.execute(read_command)

    for row in cursor:
        print(row.name)

        
    cursor.close()
    connection.close()
    


while True:
    print("1 - Seznam osob")
    print("2 - Přidat novou osobu")
    x = input("Zadej číslo akce: ")
    
    if x == "1":
        print("-------------------")
        print("Seznam osob")
        print("-------------------")
        list_persons()
        print("-------------------")
    
    elif x == "2":
        name = input("Zadej jméno osoby: ")
        add_new_person(name)
        
    else:
        break;