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
        value.execute('SELECT * from admin WHERE Username=%s and Password=%s',arg)
        return value.fetchall()
    except:
        return False

def addCourses(data):
    try:
        print(data)
        value.execute("INSERT INTO courses (Course_name) VALUES (%s)",data)
        info.commit()
        return True
    except:
        return False

def ViewCourses():
    try:
        value.execute('SELECT * from courses')
        return value.fetchall()
    except:
        return False


def deleteCourses(data):
    try:
        # print(data)
        value.execute("DELETE FROM courses WHERE ID = %s",data)
        info.commit()
        return True
    except:
        return False

def editCourses(data):     
    try:
        print(data)
        value.execute(" SELECT * FROM courses WHERE id = %s",data)
        return value.fetchall()
    except:
        return False

def updateCourses_items(data):     
    try:
        print(data)
        value.execute(" UPDATE courses SET Course_name = %s WHERE id = %s",data)
        info.commit()
        return True
    except:
        return False

def addSubject(data):
    try:
        print(data)
        value.execute("INSERT INTO subject (course_id,sub_name,Sub_code) VALUES (%s,%s,%s)",data)
        info.commit()
        return True
    except:
        return False


def ViewSubject():
    try:
        value.execute('SELECT subject.id,courses.Course_name ,subject.sub_name,subject.sub_code from subject left join courses on courses.id = subject.course_id')
        return value.fetchall()
    except:
        return False


def deleteSubject(data):
    try:
        # print(data)
        value.execute("DELETE FROM subject WHERE ID = %s",data)
        info.commit()
        return True
    except:
        return False

def editSubject(data):     
    try:
        print(data)
        value.execute(" SELECT courses.id,courses.Course_name ,subject.sub_name,subject.sub_code from subject left join courses on courses.id = subject.course_id WHERE subject.id = %s",data)
        return value.fetchall()
    except:
        return False

def updateSubject_items(data):     
    try:
        print(data)
        value.execute(" UPDATE subject SET course_id = %s,sub_name=%s,sub_code=%s WHERE id = %s",data)
        info.commit()
        return True
    except:
        return False


def addTeacher(data):
    try:
        print(data)
        value.execute("INSERT INTO teacher (name ,age,qual,username,password) VALUES (%s,%s,%s,%s,%s)",data)
        info.commit()
        return True
    except:
        return False

def ViewTeacher():
    try:
        value.execute('SELECT * from teacher')
        return value.fetchall()
    except:
        return False

def editTeacher(data):     
    try:
        print(data)
        value.execute(" SELECT * FROM teacher WHERE id = %s",data)
        return value.fetchall()
    except:
        return False


def deleteTeacher(data):
    try:
        # print(data)
        value.execute("DELETE FROM teacher WHERE ID = %s",data)
        info.commit()
        return True
    except:
        return False

def updateTeacher_items(data):     
    try:
        print(data)
        value.execute(" UPDATE teacher SET name=%s,age=%s,qual = %s,username=%s,password=%s WHERE id = %s",data)
        info.commit()
        return True
    except:
        return False

def addAssign(data):
    try:
        print("helo",data)
        value.execute("INSERT INTO assign (teacher_id,courses_id,subject_id) VALUES (%s,%s,%s)",data)
        info.commit()
        return True
    except:
        return False

def ViewnameTeacher():
    try:
        value.execute('SELECT ID,name from teacher')
        return value.fetchall()
    except:
        return False

def viewSubname(data):
    try:
        value.execute('SELECT ID,sub_name from subject where subject.course_id=%s',data)
        return value.fetchall()
    except:
        return False

def viewassign():
    try:
        value.execute('SELECT assign.ID,teacher.name,courses.Course_name,subject.sub_name from assign left join teacher on teacher.id =  assign.teacher_id left join courses on courses.id = assign.courses_id left join subject on subject.id = assign.subject_id')
        return value.fetchall()
    except:
        return False

def deleteassign(data):
    try:
        # print(data)
        value.execute("DELETE FROM assign WHERE ID = %s",data)
        info.commit()
        return True
    except:
        return False

def editAssign(data):     
    try:
        print(data)
        value.execute(" SELECT teacher.ID,teacher.name,courses.id,courses.Course_name,subject.id,subject.sub_name from assign left join teacher on teacher.id =  assign.teacher_id left join courses on courses.id = assign.courses_id left join subject on subject.id = assign.subject_id WHERE assign.id = %s",data)
        return value.fetchone()
    except:
        return False

def updateassign_item(data):     
    try:
        print(data)
        value.execute(" UPDATE assign SET teacher_id=%s,courses_id=%s,subject_id = %s WHERE id = %s",data)
        info.commit()
        return True
    except:
        return False

def viewMaterial():
    try:
        value.execute('SELECT material.id, subject.sub_name, material.material, material.title, material.description FROM material LEFT JOIN subject ON subject.id = material.subjectId')
        return value.fetchall()
    except:
        return False

def getFile(matId):
    try:
        value.execute('SELECT material FROM material WHERE id = %s', matId)
        return value.fetchone()
    except:
        return False


def viewassignments():
    try:
        value.execute('SELECT assignments.id, subject.sub_name, assignments.assignments, assignments.title, assignments.description FROM assignments LEFT JOIN subject ON subject.id = assignments.subjectId ')
        return value.fetchall()
    except:
        return False

def getFileAssignmet(matId):
    try:
        value.execute('SELECT assignments FROM assignments WHERE id = %s', matId)
        return value.fetchone()
    except:
        return False

def allTeachers():
    try:
        value.execute('SELECT id, name FROM teacher')
        return value.fetchall()
    except:
        return False

def getFilterMat(techId):
    try:
        value.execute('SELECT material.id, subject.sub_name, material.material, material.title, material.description FROM material LEFT JOIN subject ON subject.id = material.subjectId WHERE material.teacher_id = %s', (techId, ))
        return value.fetchall()
    except:
        return []

def getFilterAssign(techId):
    try:
        value.execute('SELECT assignments.id, subject.sub_name, assignments.assignments, assignments.title, assignments.description FROM assignments LEFT JOIN subject ON subject.id = assignments.subjectId WHERE assignments.teacher_id = %s', (techId, ))
        return value.fetchall()
    except:
        return []