import time
import datetime
if __name__=="__main__":
    fw = open("log.txt", 'w')
    count = 1
    while True:
        now = time.localtime()
        year = now[0]
        month = now[1]
        day = now[2]
        hour = now[3]
        temp = [str(count), str(year), str(month), str(day), str(hour)]
        str_merge = "-".join(temp)
        count += 1
        fw.write(str_merge + "\n")
        print(str_merge,count)
        if count==10:
            break
        time.sleep(1)
        print("写完一条")
    fw.close()
    pass