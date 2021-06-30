def get_positon(list_arr,low,high):
    pivod=list_arr[low]
    i,j=low,high
    while i<j:
        while i<j and list_arr[j]>=pivod:
            j-=1
        if i<j:
            list_arr[i]=list_arr[j]
            i+=1
        while i<j and list_arr[i]<pivod:
            i+=1
        if i<j:
            list_arr[j]=list_arr[i]
            j-=1
    list_arr[i]=pivod
    return i

list_=[4,9,3,1,2,5,8,4]
list_=[10,9,8,7,6,5,4,3,2,1]
# get_positon(list_,0,len(list_)-1)
# print(list_)


def quickSort(list_arr,low,high):
    if low<high:
        mid=get_positon(list_arr,low,high)
        quickSort(list_arr,low,mid-1)
        quickSort(list_arr,mid+1,high)

# quickSort(list_,0,len(list_)-1)
def select_sort(list_):
    for i in range(len(list_)-1):
        min=i
        for j in range(i+1,len(list_)):
            if list_[j]<list_[min]:
                min=j
        list_[i],list_[min]=list_[min],list_[i]
# select_sort(list_)
def insert_sort(list_):
    for i in range(1,len(list_)):
        temp=list_[i]
        j=i-1
        while j>=0 and list_[j]>temp:
            list_[j+1]=list_[j]
            j-=1
        list_[j+1]=temp

insert_sort(list_)
print(list_)