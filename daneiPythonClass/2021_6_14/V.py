from M import StudentModel
from C import StudentManagerController
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