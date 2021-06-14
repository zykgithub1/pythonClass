
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