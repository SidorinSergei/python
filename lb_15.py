import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con=sqlite3.connect('pivko_na_ivko.db')
        return con
    except Error:
        print(Error)

def sql_table(con):
    cursorObj=con.cursor()
    cursorObj.execute(
    "CREATE TABLE Сотрудник(id_сотрудника integer PRIMARY KEY,ФИО text,должность text)"
    )
    cursorObj.execute(
    "CREATE TABLE Автомобиль(id_автомобиля integer PRIMARY KEY,id_сотрудника,фирма text,стоимость float)")
    cursorObj.execute(
    "CREATE TABLE Журнал(id_журнала integer PRIMARY KEY,количество_авто integer,цена_авто float)")
    cursorObj.execute(
    "CREATE TABLE Покупатель_автомобиль(id_покупателя,id_автомобиля integer PRIMARY KEY)"
    )
    cursorObj.execute(
    "CREATE TABLE Покупатель(id_покупателя integer PRIMARY KEY,ФИО text)"
    )
    con.commit()
def pivko_insert(con):
    cursorObj=con.cursor()
    cursorObj.execute(
    "INSERT INTO Сотрудник VALUES(1,'Щетков Игнат Игнатович','уборщик')")
    cursorObj.execute(
        "INSERT INTO Сотрудник VALUES(2,'Добров Пьер Васильевич','консультант')")
    cursorObj.execute(
        "INSERT INTO Сотрудник VALUES(3,'Димитров Семен Игнатович','консультант')")
    cursorObj.execute(
        "INSERT INTO Сотрудник VALUES(4,'Васильков Дмитрий Сергеевич','директор')")
    cursorObj.execute(
        "INSERT INTO Сотрудник VALUES(5,'Романов Роман Романович','секретарь')")
    cursorObj.execute("INSERT INTO Автомобиль VALUES(1,2,'Лада',33000)")
    cursorObj.execute("INSERT INTO Автомобиль VALUES(2,3,'Ford',1200000)")
    cursorObj.execute("INSERT INTO Автомобиль VALUES(3,3,'Mercedes-Benz',3000000)")
    cursorObj.execute("INSERT INTO Автомобиль VALUES(4,2,'Лада',500000)")
    cursorObj.execute("INSERT INTO Автомобиль VALUES(5,3,'BMW',3000000)")
    cursorObj.execute("INSERT INTO Журнал VALUES(1,3,7200000)")
    cursorObj.execute("INSERT INTO Журнал VALUES(2,2,533000)")
    cursorObj.execute("INSERT INTO Покупатель VALUES(1,'Попов Иван Викторович')")
    cursorObj.execute("INSERT INTO Покупатель VALUES(2,'Щетоков Иван Иваныч')")
    cursorObj.execute("INSERT INTO Покупатель VALUES(3,'Семенов Владимир Владимирович')")
    cursorObj.execute("INSERT INTO Покупатель VALUES(4,'Пупкин Василий Дмитриевич')")
    cursorObj.execute("INSERT INTO Покупатель VALUES(5,'Данилов Григорий Андреевич')")
    # cursorObj.execute("INSERT INTO Покупатель_автомобиль VALUES(1,2)")
    # cursorObj.execute("INSERT INTO Покупатель_автомобиль VALUES(2,3)")
    # cursorObj.execute("INSERT INTO Покупатель_автомобиль VALUES(3,5)")
    # cursorObj.execute("INSERT INTO Покупатель_автомобиль VALUES(4,1)")
    # cursorObj.execute("INSERT INTO Покупатель_автомобиль VALUES(5,4)")
    con.commit()

def pivko_select(con):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT name FROM sqlite_master WHERE type='table'")
    table = cursorObj.fetchall()

    tablesList = []
    for tab in table:


        tablesList.append(tab[0])

        for listItem in tablesList:

         cursorObj.execute(f'SELECT * from {listItem}')
        [print(row) for row in cursorObj.fetchall()]
        print(f'table {listItem}')

    con = sql_connection()

def pivko_update(con):
    cursorObj = con.cursor()
    cursorObj.execute('UPDATE Автомобиль SET стоимость = 35000 where id_автомобиля = 1')
    con.commit()

    cursorObj = con.cursor()
    cursorObj.execute('UPDATE Автомобиль SET стоимость = 3300000 where id_автомобиля = 3')
    con.commit()

    cursorObj = con.cursor()
    cursorObj.execute('UPDATE Журнал SET цена_авто = 535000 where id_журнала = 2')
    con.commit()

    cursorObj = con.cursor()
    cursorObj.execute('UPDATE Журнал SET цена_авто = 7500000 where id_журнала = 1')
    con.commit()

def pivko_delete(con):
    cursorObj = con.cursor()
    cursorObj.execute('DELETE from Сотрудник where ФИО = "Романов Роман Романович" ')
    con.commit()

con=sql_connection()
#sql_table(con)
#pivko_insert(con)

#pivko_update(con)
pivko_delete(con)
pivko_select(con)
