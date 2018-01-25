# HelloWorld
# coding=utf-8
print("Hello World!")
print("你好！世界！")

#number variables
print("\n")
print("---Number variables---")
x=100
y=1.234e6
#z=100.0001L  #did not support as invalid syntax
c=complex(3.4,5.6)

print("x=",x)
print("y=",y)
#print("z=",z)
print("c=",c)
print("c+x=",c+x)

#string variables
print("\n")
print("---String variables---")
strx='Hello'
stry="World"

print("strx=",strx)
print("strx[0:2]=",strx[0:2])  #only print strx[0] and strx[1]
print("strx[1]=",strx[1])
print("strx[1:]=",strx[1:])

print("stry=",stry)
print("stry[3:5]=",stry[3:5])  #print stry[3], stry[4]

strz=strx+stry
print("strz=strx+stry=",strz)

#List variables， 列表
print("\n")
print("---List variables---")
listx=[1,2,3,
       "a","b","c",
       'aa','bb','cc']
listy=[4,5,6]
print("listx=",listx)
print("listx[2:4]=",listx[2:4]) #print listx[2], listx[3]
print("listy=",listy)
print("listx+listy=",listx+listy)
print("listy*2=",listy*2)
listx[0:3]=listy  #List variable could be changed again
print("After listx[0:3]=listy, Listx=")
print(listx)

#tuple variables, 元组
#it could not be changed again
print("\n")
print("---Tuple variables---")
tuplex=(1,2,3,"a","b","c",'aa','bb','cc')
tupley=(4,5,6)
print("tuplex=", tuplex)
print("tuplex[1:3]=",tuplex[1:3])
print("tupley=",tupley)
print("tuplex+tupley=",tuplex+tupley)
#tuplex[3:6]=tupley. #It will cause error because tuplex variables does not support re-assignment

#dictionary variables, 字典，按键值寻址，不是按地址寻址
print("\n")
print("---Dictionary variables---")
dictx = {}
dictx['one'] = "This is one"
dictx[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print("dictx=",dictx)
print("dictx['one']=",dictx['one'])  # 输出键为'one' 的值
print("dictx[2]=", dictx[2])  # 输出键为 2 的值
print("tinydict=",tinydict)  # 输出完整的字典
print("tinydict.keys()=",tinydict.keys())    # 输出所有键
print("tinydict.values()=",tinydict.values())  # 输出所有值



