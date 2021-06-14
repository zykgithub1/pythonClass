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