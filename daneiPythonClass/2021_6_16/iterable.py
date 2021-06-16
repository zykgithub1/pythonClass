"""
for 的 theory
1,get iterate
2,loop get next iterate
"""
# lis01=[1,2,3,4,5,6,7]
# itrato=lis01.__iter__()
# while True:
#     try:
#         print(itrato.__next__())
#     except:
#         break
dic01={
    "铁扇公主":101,
    "芭蕉":102,
    "扳手":103
}
iter01=dic01.__iter__()
while True:
    try:
        item=iter01.__next__()
        print(item,"->",dic01[item])
    except:
        break

