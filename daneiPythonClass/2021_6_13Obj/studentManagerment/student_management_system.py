"""
学生管理系统
步骤：
数据模型类：1->studentModel
            2->StudentManageControll
            3->完成数据：学生列表__student_list
            4->行为获取列表  stu_list
            5->添加学生：add_student
"""


class StudentModel:
    """
    学生信息模块
    """

    def __init__(self, name="", age=0, score=0, id=0, ):
        """

        :param name:str 姓名
        :param age: Int age
        :param score: float socre
        :param id: id 自增 可不填
        """
        self.id = id
        self.name = name
        self.age = age
        self.score = score
    # @property
    # def age(self):
    #     return self.__age
    # @age.setter
    # def age(self,age):
    #     if  15<=age<=30:
    #         self.__age=age
    #     else:
    #         while True:
    #             newage = int(input("请重新输入年龄"))
    #             if 15<=newage<=30:
    #                 self.__age=newage
    #                 return
    #
    # @property
    # def age(self):
    #     return self.__age
    #
    # @age.setter
    # def age(self, age):
    #     if 15 <= age <= 30:
    #         self.__age = age
    #     else:
    #         while True:
    #             newage = int(input("请重新输入年龄"))
    #             if 15 <= newage <= 30:
    #                 self.__age = newage
    #                 return


class StudentManagerController:
    """
    学生管理控制器  赋值业务逻辑处理
    """
    __init_id = 1000

    def __init__(self):
        """
        返回学生列表
        """
        self.__stu_list = []

    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self, stu_info):
        """
        添加新学生
        :param stu_info: 没有编号的学生信息
        :return:
        """
        stu_info.id = self.__generate_Id(stu_info)
        self.__stu_list.append(stu_info)

    def remove_student(self, id):
        targert=self.__find_stu_byid(id)
        if targert != None:
            self.stu_list.remove(targert)
            return True
        else:
            return False

    def sort_by_socre(self):
        ans=self.stu_list.copy()
        ans.sort(key=lambda x:x.score,reverse=True )
        return ans


    def __find_stu_byid(self, id):
        """
        通过id寻找学生
        :param id:
        :return:
        """
        for item in self.stu_list:
            if item.id == id:
                return item

    def update_stu(self,stu_info):
        """
        根据学生SutdentModel的实例对象修改学生
        :param stu_info:
        :return:
        """
        target=self.__find_stu_byid(stu_info.id)
        if target!=None:
            target.id=stu_info.id
            target.name=stu_info.name
            target.age=stu_info.age
            target.score=stu_info.score
            return True
        return False

    def __generate_Id(self, stu_info):
        StudentManagerController.__init_id += 1
        return StudentManagerController.__init_id

class StudentManagerView:
    """
    学生管理器视图
    """

    def __init__(self):
        self.__manager=StudentManagerController()
    def __display_menu(self):
        print("1->添加学生")
        print("2->显示学生")
        print("3->删除学生")
        print("4->修改学生")
        print("5->按照成绩升序显示学生")

    def __select_menu(self):
        item=input("请输入：")
        if item =="1":
            self.__input_student()
            return 1
        if item =="2":
            self.__output_student(self.__manager.stu_list)
            return 2
        if item =="3":
            self.__remove_student()
            return 3
        if item =="4":
            self.__update_student()
            return 4
        if item =="5":
            self.__sort_by_ascscore()
            return 5
        if item=="6":
            return 6

    def main(self):
        while True:
            self.__display_menu()
            choise=self.__select_menu()
            if choise==6:
                print("结束程序拜拜")
                break

    def __input_student(self):
        stu_info = self.__inputstu_return_model()
        self.__manager.add_student(stu_info)

    def __inputstu_return_model(self):
        str_name = input("请输入姓名")
        int_age = int(input("请输入年龄"))
        float_score = eval(input("请输入成绩"))
        stu_info = StudentModel(str_name, int_age, float_score)
        return stu_info
    def __inputstuid_return_model(self,id):
        str_name = input("请输入姓名")
        int_age = int(input("请输入年龄"))
        float_score = eval(input("请输入成绩"))
        stu_info = StudentModel(str_name, int_age, float_score,id)
        return stu_info

        str_name = input("请输入姓名")
        int_age = int(input("请输入年龄"))
        float_score = eval(input("请输入成绩"))
        stu_info = StudentModel(str_name, int_age, float_score)
        return stu_info

    def __output_student(self,list_output):
        for item in list_output:
            print(item.id,item.name,item.age,item.score)

    def __remove_student(self):
        while True:
            id=int(input("请输入id"))
            flag = self.__manager.remove_student(id)
            if flag:
                print("删除成功")
                break
            print("删除失败")

    def __update_student(self):
        search_id=int(input("请输入要修改的学生的id"))
        stu_info=self.__inputstuid_return_model(search_id)
        self.__manager.update_stu(stu_info)

    def __sort_by_ascscore(self):
        ans=self.__manager.sort_by_socre()
        for item in ans:
            print(item.score)


sview=StudentManagerView()
sview.main()
