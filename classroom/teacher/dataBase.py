import mysql.connector
info=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    db="classroom"
)

value=info.cursor()
def login(arg):
    try:
        value.execute('SELECT * from teacher WHERE username=%s and password=%s',arg)
        return value.fetchall()
    except:
        return False


def ViewCourses():
    try:
        value.execute('SELECT * from courses')
        return value.fetchall()
    except:
        return False


def viewSubname(data):
    try:
        value.execute('SELECT ID,sub_name from subject where subject.course_id=%s',data)
        return value.fetchall()
    except:
        return False


def addMaterial(data):
    try:
        value.execute('INSERT INTO material (teacher_id, subjectId, material, title, description) VALUES (%s, %s, %s, %s, %s)', data)
        info.commit()
        return True
    except:
        return False


def viewMaterial(id):
    try:
        value.execute('SELECT material.id, subject.sub_name, material.material, material.title, material.description FROM material LEFT JOIN subject ON subject.id = material.subjectId WHERE teacher_id = %s', (id[0][0], ))
        return value.fetchall()
    except:
        return False

def deleteMaterial(id):
    try:
        # print(data)
        value.execute("DELETE FROM material WHERE id = %s",id)
        info.commit()
        return True
    except:
        return False


def getFile(matId):
    try:
        value.execute('SELECT material FROM material WHERE id = %s', matId)
        return value.fetchone()
    except:
        return False

def getMaterial(id):
    try:
        value.execute('SELECT subject.id, subject.sub_name, material.material, material.title, material.description FROM material LEFT JOIN subject ON subject.id = material.subjectId WHERE material.id = %s', id)
        return value.fetchone()
    except:
        return False

def editMaterial(data):
    try:
        value.execute('UPDATE material SET material = %s, title = %s, description = %s WHERE id = %s', data)
        info.commit()
        return True
    except:
        return False



def addAssignment(data):
    try:
        value.execute('INSERT INTO assignments (teacher_id, subjectId, assignments, title, description) VALUES (%s, %s, %s, %s, %s)', data)
        info.commit()
        return True
    except:
        return False


def viewassignments(id):
    try:
        value.execute('SELECT assignments.id, subject.sub_name, assignments.assignments, assignments.title, assignments.description FROM assignments LEFT JOIN subject ON subject.id = assignments.subjectId WHERE teacher_id = %s', (id[0][0], ))
        return value.fetchall()
    except:
        return False

def deleteassignments(id):
    try:
        # print(data)
        value.execute("DELETE FROM assignments WHERE id = %s",id)
        info.commit()
        return True
    except:
        return False


def getFileAssignmet(matId):
    try:
        value.execute('SELECT assignments FROM assignments WHERE id = %s', matId)
        return value.fetchone()
    except:
        return False

def getassignments(id):
    try:
        value.execute('SELECT subject.id, subject.sub_name, assignments.assignments, assignments.title, assignments.description FROM assignments LEFT JOIN subject ON subject.id = assignments.subjectId WHERE assignments.id = %s', id)
        return value.fetchone()
    except:
        return False

def editassignments(data):
    try:
        value.execute('UPDATE assignments SET assignments = %s, title = %s, description = %s WHERE id = %s', data)
        info.commit()
        return True
    except:
        return False
