# -*- coding:utf-8 -*-

import datetime


class PersonTypeError(TypeError):
    pass


class PersonValueError(ValueError):
    pass


class Person(object):
    _num = 0  # 计数与单个实例无关，所以设为类属性

    def __init__(self, name, sex, birthday, identity):
        if not (isinstance(name, str)) and sex in ("男", "女"):
            raise PersonTypeError(name, sex)
        try:
            birth = datetime.date(*birthday)
        except:
            raise PersonValueError("wrong date:", birthday)
        self._name = name
        self._sex = sex
        self._birthday = birth
        self._id = identity
        Person._num += 1

    def id(self): return self._id

    def name(self): return self._name

    def sex(self): return self._sex

    def birthday(self): return self._birthday

    def age(self): return datetime.date.today().year - self._birthday.year

    def set_name(self, new_name):
        if not isinstance(new_name, str):
            raise PersonValueError("set_name:", new_name)
        self._name = new_name

    def __lt__(self, another):
        if not isinstance(another, Person):
            raise PersonTypeError(another)
        return self._id < another.id

    @classmethod  # 调用时使用“Person.nun()”
    def num(cls): return Person._num

    def __str__(self):
        return " ".join((self._id, self._name, str(self._birthday), self._sex, self.age))
        # str的join方法要求参数是iterator

    def details(self):
        return ", ".join(('编号：' + self._id,
                          '姓名：' + self._name,
                          '性别：' + self._sex,
                          '出生日期：' + str(self._birthday)
                          ))


class Student(Person):
    _id_num = 0  # 因为id数量与学生实例无关，所以用静态方法来统计id数量，并保持唯一性

    @classmethod  # 因为学生id与学生实例有关，所以用类方法来生成学生的id
    def _id_gent(cls):
        cls._id_num += 1
        year = datetime.date.today().year
        return "1{:04}{:05}".format(year, cls._id_num)

    def __init__(self, name, sex, birthday, department):
        # 父类.__init__(self, *attr)来定义如何继承父类的初始数据
        Person.__init__(self, name, sex, birthday, Student._id_gent())
        self._department = department
        self._enroll_date = datetime.date.today()
        self._course = {}

    # 与选课和成绩有关的方法
    def set_course(self, course_name):
        self._course[course_name] = None

    def set_score(self, course_name, score):
        if course_name not in self._course:
            raise PersonValueError("该学生没有选这门课：", course_name)
        self._course[course_name] = score

    def scores(self):
        return [(cname, self._course[cname]) for cname in self._course]

    def details(self):
        return ",".join((Person.details(self),
                         "入学日期：" + str(self._enroll_date),
                         "院系：" + self._department,
                         "课程记录：" + str(self.scores())
                         ))


class Staff(Person):
    _id_num = 0

    @classmethod
    def _id_gen(cls, birthday):  # 实现职工号的生成
        cls._id_num += 1
        birth_year = datetime.date(*birthday).year
        return "0{:04}{:05}".format(birth_year, cls._id_num)

    def __init__(self, name, sex, birthday, entry_date=None):
        super().__init__(name, sex, birthday, Staff._id_gen(birthday))  # super().__init__效果与Person.__init__一致
        if entry_date:
            try:
                self._entry_date = datetime.date(*entry_date)
            except:
                raise PersonValueError("Wrong Date:", entry_date)
        else:
            self._entry_date = datetime.date.today()

        # 下面这三项设置默认值之后再提供一个修改的方法
        self._salary = 2520
        self._department = "Undefined"
        self._position = "Undefined"

    def set_salary(self, salary):
        if not isinstance(salary, int):
            raise PersonValueError("Wrong salary:", salary)
        self._salary = salary

    def set_position(self, position):
        if not isinstance(position, str):
            raise PersonValueError("Wrong position:", position)
        self._position = position

    def set_department(self, department):
        if not isinstance(department, str):
            raise PersonValueError("Wrong department:", department)
        self._department = department

    def details(self):
        return ",".join((super().details(),  # super().details实际是调用的父类Person的details方法
                         "入职日期：" + str(self._entry_date),
                         "院系：" + self._department,
                         "职位：" + self._position,
                         "工资：" + str(self._salary)
                         ))

