# fo=open("test.txt","wb+")
# fo.write("what is your goal?曾驿凯".encode())
# fo.close()
# fr=open("test.txt","r")
# ans=fr.readlines()
# print(ans[0].decode())

# words="abandun"
# for line in fo:
#     w=line.split(" ")[0]
#     if w==words:
#         words_list=line.split(" ")
#         for i in range(len(words_list)-1,-1,-1):
#             if words_list[i]==""or words_list[i]==w:
#                 del words_list[i]
#         print(words_list[0])
# else:
#     print("没找到该单词")
fo=open('test.txt',"a")
fo.write("雄关漫道真如铁\n")
fr=open("test.txt","r")
print(fr.read())




fo.close()
fr.close()