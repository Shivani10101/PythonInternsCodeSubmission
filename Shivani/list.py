#why do we use list - when we need to group values together
from operator import concat
from unicodedata import name


roll_no=[1001,1002,1003,1004,1005]     #homogenious list
print(roll_no)
print(type(roll_no))

#multiple information about a person
name="shivani"
age=22
hight=5.4
print(name,type(name),age,type(age),hight,type(hight))

#group the above information together
person_info=[name,age,hight]
print(person_info)

#print values at each index of the list
roll_no=[5,6,7,8,10,20]
index=0
for item in roll_no:
    print(index, item)
    index= index+1
    
#list length
list=["apple","banana","cherry","carrot"]
print(len(list))

#access list item(Range of indexes)
thislist= ["apple","banana","cherry","orange","kiwi","mango","melon"]
print(thislist[2:5])      #this will return the item from position 2 to 5.

#concatination in list
list1=["shivani", "mca", 22]
list2=["sapna", "mba", 23]
concat_result= list1+list2
print(concat_result)

#you can also ADD new item at the end of the list, by using the append() method.
# Add new item item the list
concat_result.append('ghaziabad')
print(concat_result)

#update slice in the list- this can change the size of the list or clear it. 
list2= ["sarita","mca",22]
concat_result[1:2]= list2
print(concat_result)

#Remove a slice from list
concat_result[1:4]=[]
print(concat_result)
