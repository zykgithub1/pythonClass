# def div__apples(apple_count):
#
#     person_count = int(input("请输入人数"))
#     ans = apple_count // person_count
#     ans=apple_count/2
#     print("every one gets %d apples"%(ans))
# try:
#     div__apples(10)
# except ValueError:
#     print("输入的人数必须是整数")
# except ZeroDivisionError:
#     print("输入的人数不能是0")
# except Exception:
#     print("未知错误")
# else:
#     print("没有出错")
#     raise ValueError("关闭")
# print("后续逻辑")
def get_grade():
    while True:
        try:
            grade = int(input("请输入成绩"))
        except:
            continue
        if 0<grade<100:
            return grade
print(get_grade())



