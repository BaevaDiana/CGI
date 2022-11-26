import sqlite3
from sqlite3 import Error


def sql_connection():
    try:
        con = sqlite3.connect('SQL_LoadLog.db')
        return con
        print("Соединение работает")
    except Error:
        print(Error)


"FOREIGN KEY (id_SubFaculties) REFERENCES SubFaculties (id_SubFaculties) ON DELETE CASCADE,"
"FOREIGN KEY(id_Lect) REFERENCES Lecturer (id_Lect) ON DELETE CASCADE,"
"FOREIGN KEY(id_Lect) REFERENCES Lecturer (id_Lect) ON DELETE CASCADE,"
"FOREIGN KEY(id_Sub) REFERENCES Subject (id_Sub) ON DELETE CASCADE,"
"FOREIGN KEY(id_SubFaculties) REFERENCES SubFaculties (id_SubFaculties) ON DELETE CASCADE,"

def sql_subfaculties(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE SubFaculties("
        "id_SubFaculties int PRIMARY KEY,"
        "SubFacultiesName text,"
        "EmployeeList text,"
        "SalaryeEmployee text,"
        "GroupList text)")

    cursorObj.execute(
        "INSERT INTO SubFaculties "
         "VALUES(1, 'Кафедра вычислительных технологий', 'Шиян В.И.,Жук А.С.Приходько Т.А.', '50000-100000', '36,39') "
    )
    cursorObj.execute(
        "INSERT INTO SubFaculties "
        "VALUES(2, 'Кафедра информационных технологий', 'Гаркуша О.В.,Добровольская Н.Ю.,Михайличенко А.А.', '50000-100000','36,39')"
    )

    cursorObj.execute(
        "INSERT INTO SubFaculties "
        "VALUES(3,' Кафедра математического моделирования', 'Евдокимов А.А.,Истомин Н.К.,Рубцов С.Е.', '50000-10000', '37,38')"
    )
    con.commit()


def sql_lecturer(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE Lecturer("
        "id_Lect int PRIMARY KEY,"
        "id_SubFaculties int,"
        "FullNameLecturer text,"
        "ScienceDegree text,"
        "SubFaculties text,"
        "Discipline text,"
        "WorkExperience int)")

    cursorObj.execute(
        "INSERT INTO Lecturer "
        "VALUES(11,1,'Шиян Валерий Игоревич','Преподаватель','Кафедра вычислительных технологий','Интерпретируемые языки программирования',5)"
    )

    cursorObj.execute(
        "INSERT INTO Lecturer " 
        "VALUES(12,2,'Гаркуша Олег Васильевич','Доцент','Кафедра информационных технологий','Операционные системы',42)"
    )

    cursorObj.execute(
        "INSERT INTO Lecturer "
        "VALUES(13,3,'Евдокимов Александр Александрович','Доцент','Кафедра математического моделирования','Управление информацией',5)"
    )
    con.commit()


def sql_subject(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE Subject("
        "id_Sub int PRIMARY KEY,"
        "id_Lect int,"
        "TypeSubject text)")

    cursorObj.execute(
        "INSERT INTO Subject "
        " VALUES(11,11,'Лекция')"
    )

    cursorObj.execute(
        "INSERT INTO Subject "
        "VALUES(22,12,'Лабораторная работа')"
    )

    cursorObj.execute(
        "INSERT INTO Subject "
        "VALUES(10,13,'Лекция')"
    )
    con.commit()


def sql_lesson(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE Lesson("
        "id_Lect int,"
        "id_Sub int,"
        "NumberOfGroups int,"
        "NumberOfStudents int)")

    cursorObj.execute(
        "INSERT INTO Lesson "
        "VALUES(11,22,1,15)"
    )

    cursorObj.execute(
        "INSERT INTO Lesson "
        "VALUES(12,11,3,50)"
    )

    cursorObj.execute(
        "INSERT INTO Lesson "
        "VALUES(13,10,1,15)"
    )
    con.commit()


def sql_loadlog(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE LoadLog("
        "id_JournalPersonnelNumber int PRIMARY KEY,"
        "id_SubFaculties int,"
        "NameSubject text,"
        "NumberOfHours int,"
        "NumberOfGroups int)"
    )

    cursorObj.execute(
        "INSERT INTO LoadLog "
        "VALUES(1,2,'Интерпретируемые языки программирования',4,4)"
    )

    cursorObj.execute(
        "INSERT INTO LoadLog "
        "VALUES(2,1,'Информационная безопасность',2,4)"
    )

    cursorObj.execute(
        "INSERT INTO LoadLog "
        "VALUES(3,3,'Управление информацией',6,4)"
    )
    con.commit()

def select(con):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT name FROM sqlite_master WHERE type='table'")
    table = cursorObj.fetchall()

    tablesList = []
    for tab in table:
        tablesList.append(tab[0])

    for listItem in tablesList:
        print(f"Вывод содержимого таблицы {listItem}")
        cursorObj.execute(f'SELECT * from {listItem}')
        [print(row) for row in cursorObj.fetchall()]


#con = sql_connection()
#sql_subfaculties(con)
#sql_lecturer(con)
#sql_subject(con)
#sql_lesson(con)
#sql_loadlog(con)

#delete,update