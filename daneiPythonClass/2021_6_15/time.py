import time

# print(time.localtime())
# tup01=time.localtime()
# nowtime_str=time.strftime("%y-%m-%d %H:%M:%S",tup01)
# print(nowtime_str)
# tupel_nowtime=time.strptime(nowtime_str,"%y-%m-%d %H:%M:%S")
# print(tupel_nowtime)
# tuple_goal=time.localtime("2022-10-10")
# print(tuple_goal)
def get_xingqi(year,month,day):
    """
    获取星期数
    :param year:
    :param month:
    :param day:
    :return:
    """
    goal_tuple=time.strptime("%d-%d-%d"%(year,month,day),"%Y-%m-%d")
    days={
        0: "星期日",
        1: "星期一",
        2: "星期二",
        3: "星期三",
        4: "星期四",
        5: "星期五",
        6: "星期六",
          }
    return days[goal_tuple[6]]
# print(get_xingqi(2022,6,20))
def get_lifedays(year,month,day):
    nowtime=time.time()
    str_tuple=time.strptime("%d-%d-%d"%(year,month,day),"%Y-%m-%d")
    birth_seconds=time.mktime(str_tuple)
    lifes=(nowtime-birth_seconds)//1
    days=lifes/3600//24
    return days
# print(get_lifedays(1996,9,10))

def get_kaoyan_days(year,month,day):
    str_tuple=time.strptime("%d-%d-%d"%(year,month,day),"%Y-%m-%d")
    goal_seconds=time.mktime(str_tuple)
    length=goal_seconds-time.time()
    return length/3600//24
print(get_kaoyan_days(2022,12,22))
