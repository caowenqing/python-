# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.set_gender(gender)

    def set_gender(self, gender):
        if gender in ('male','female'):
            self.__gender=gender
        else:
            raise ValueError("gender must be male or female")

    def get_gender(self):
        return self.__gender

# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
