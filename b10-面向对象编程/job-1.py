#定义一个学生类，有下面的类属性

class Student():

    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.score = scores

    def get_name(self):
        return self.name

    def get_age(self):
        return int(self.age)

    def get_course(self):
        #使用字典定义各个科目的分数
        maxScore = max(self.score,key=self.score.get)
        return maxScore

stu = Student("daiye",18,{'语文': 33, '数学': 36, '英语': 41})
print(stu.get_age())
print(stu.get_course())
print(stu.get_name())