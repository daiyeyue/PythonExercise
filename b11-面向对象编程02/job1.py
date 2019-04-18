# coding=gbk
# ���������ͳɶ�����У��
# ����linux��python�����γ�
# ��������У��python 3�ڿγ̺ͳɶ�У��linux 1�ڿγ�
# ����Ա�����˱���У��ѧԺС�ţ�����������python 3��
# ����Ա�����˽�ʦС�ܣ�������������python 3��
# ��ʦС�ܴ�����һ��python 3�ڵ��Ͽμ�¼ Day02
# ��ʦС��δDay02 ��ڿ����е�ѧԺ��������ҵ��С�ŵ���A��С���õ�B
# ѧԺС�Ų鿴���Լ������Ŀγ�
# ѧԺС���ڲ鿴���Լ���python3�ĳɼ��б���˳�
# ѧԺС�Ÿ��˽�ʦС�ܺ���

Course_list = []
class School:
    def __init__(self,school_name): #���캯��
        self.school_name = school_name
        self.students_lists = []
        self.teachers_lists = []

        global Course_list

    def hire(self, obj):
        self.teachers_lists.append(obj.name)
        print("����Ƹ����һ���µ���ʦ".format(obj.name))

    def enroll(self, obj):
        self.students_lists.append(obj.name)
        print("����������һ����ѧԱ{}".format(obj.name))

class Grade(School):  #�̳�School
    def __init__(self, school_name, grade_code, grade_course):
        super(Grade, self).__init__(school_name)
        self.grade_code = grade_code
        self.grade_course = grade_course
        self.member = []
        Course_list.append(self.grade_course)

        print("������������{}��{}��{}".format(self.school_name, self.grade_code,self.grade_course))

    def course_info(self):
        print("�γ̴��{}�� day01��day02��day03".format(self.grade_course))


Python = Grade("BJ", 3, "python")
Linux = Grade("CD",1,"linux")

class School_member():
    def __init__(self, name, age, sex, role):
        self.name = name
        self.age = age
        self.sex = sex
        self.role = role
        self.course_list = []
        print("�ҽ�{}������һ��{}".format(self.name, self.role))

stu_num_id = 0
class Students(School_member):
    def __init__(self, name, age, sex, role, course):
        super(Students, self).__init__( name, age, sex, role)
        global stu_num_id
        stu_num_id = stu_num_id + 1
        stu_id = course.school_name + "S" + str(course.grade_course) + str(stu_num_id).zfill(2)
        # zfill ������ã���ֻ��һλ��ʱ��ǰ�����0��ֻ�ܶ�str���Ͳ���

        self.id = stu_id
        self.mark_list = {}

    def study(self, course):
        print("��������ѧϰ{}�Σ��ҵ�ѧ����{}".format(course.grade_course, self.id))

    def pay(self, course):
        print("�ҽ���1000��Ǯ��{}��".format(course.grade_course))
        self.course_list.append(course.grade_course)

    def praise(self, obj):
        print("{}����{}���".format(self.name, obj.name))

    def mark_check(self):
        for i in self.mark_list.items():
            print(i)

    def out(self):
        print("���뿪��")

tea_num_id = 00
class Teacher(School_member):
    def __init__(self, name, age, sex, role, course):
        super(Teacher, self).__init__(name, age, sex, role)
        global tea_num_id
        tea_num_id = tea_num_id + 1
        tea_id = course.school_name + "S" + str(course.grade_course) + str(tea_num_id).zfill(2)
        self.id = tea_id

    def teach(self, course):
        print("�������ｲ�������������ｲ{},�ҵ�id��{}".format(course.grade_course, self.id))

    def record_mark(self, Date, course, obj, level):
        obj.mark_list["Day"+str(Date)] = level

a = Students("С��",18,"��","ѧ��",Python)
Python.enroll(a)
a.study(Python)
a.pay(Python)
b = Students("С��",22,"Ů","ѧ��",Python)
Python.enroll(b)
b.study(Python)
b.pay(Python)
c = Teacher("С��",30,"��","��ʦ",Python)
Python.hire(c)
c.record_mark(1,Python,a,"A")
c.record_mark(1,Python,b,"B")
c.record_mark(2,Python,a,"A")
c.record_mark(2,Python,b,"B")
print(a.course_list)
b.out()
a.praise(c)



