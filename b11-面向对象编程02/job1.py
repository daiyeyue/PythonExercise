# coding=gbk
# 创建北京和成都两个校区
# 创建linux和python两个课程
# 创建北京校区python 3期课程和成都校区linux 1期课程
# 管理员创建了北京校区学院小张，并分配在了python 3期
# 管理员创建了讲师小周，并将其分配给了python 3期
# 讲师小周创建了一条python 3期的上课记录 Day02
# 讲师小周未Day02 这节课所有的学院批改了作业，小张得了A，小王得到B
# 学院小张查看了自己所报的课程
# 学院小张在查看了自己在python3的成绩列表后退出
# 学院小张给了讲师小周好评

Course_list = []
class School:
    def __init__(self,school_name): #构造函数
        self.school_name = school_name
        self.students_lists = []
        self.teachers_lists = []

        global Course_list

    def hire(self, obj):
        self.teachers_lists.append(obj.name)
        print("我们聘请了一个新的老师".format(obj.name))

    def enroll(self, obj):
        self.students_lists.append(obj.name)
        print("我们又有了一个新学员{}".format(obj.name))

class Grade(School):  #继承School
    def __init__(self, school_name, grade_code, grade_course):
        super(Grade, self).__init__(school_name)
        self.grade_code = grade_code
        self.grade_course = grade_course
        self.member = []
        Course_list.append(self.grade_course)

        print("我们现在有了{}的{}的{}".format(self.school_name, self.grade_code,self.grade_course))

    def course_info(self):
        print("课程大纲{}是 day01，day02，day03".format(self.grade_course))


Python = Grade("BJ", 3, "python")
Linux = Grade("CD",1,"linux")

class School_member():
    def __init__(self, name, age, sex, role):
        self.name = name
        self.age = age
        self.sex = sex
        self.role = role
        self.course_list = []
        print("我叫{}，我是一个{}".format(self.name, self.role))

stu_num_id = 0
class Students(School_member):
    def __init__(self, name, age, sex, role, course):
        super(Students, self).__init__( name, age, sex, role)
        global stu_num_id
        stu_num_id = stu_num_id + 1
        stu_id = course.school_name + "S" + str(course.grade_course) + str(stu_num_id).zfill(2)
        # zfill 填充作用，当只有一位数时，前面填充0，只能对str类型操作

        self.id = stu_id
        self.mark_list = {}

    def study(self, course):
        print("我来这里学习{}课，我的学号是{}".format(course.grade_course, self.id))

    def pay(self, course):
        print("我交了1000块钱给{}课".format(course.grade_course))
        self.course_list.append(course.grade_course)

    def praise(self, obj):
        print("{}觉得{}真棒".format(self.name, obj.name))

    def mark_check(self):
        for i in self.mark_list.items():
            print(i)

    def out(self):
        print("我离开了")

tea_num_id = 00
class Teacher(School_member):
    def __init__(self, name, age, sex, role, course):
        super(Teacher, self).__init__(name, age, sex, role)
        global tea_num_id
        tea_num_id = tea_num_id + 1
        tea_id = course.school_name + "S" + str(course.grade_course) + str(tea_num_id).zfill(2)
        self.id = tea_id

    def teach(self, course):
        print("我来这里讲课啦，我来这里讲{},我的id是{}".format(course.grade_course, self.id))

    def record_mark(self, Date, course, obj, level):
        obj.mark_list["Day"+str(Date)] = level

a = Students("小张",18,"男","学生",Python)
Python.enroll(a)
a.study(Python)
a.pay(Python)
b = Students("小王",22,"女","学生",Python)
Python.enroll(b)
b.study(Python)
b.pay(Python)
c = Teacher("小周",30,"男","老师",Python)
Python.hire(c)
c.record_mark(1,Python,a,"A")
c.record_mark(1,Python,b,"B")
c.record_mark(2,Python,a,"A")
c.record_mark(2,Python,b,"B")
print(a.course_list)
b.out()
a.praise(c)



