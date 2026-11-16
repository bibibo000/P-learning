for i in range(1,21):
    print(i)
for i in range(1,10):
    print(i)
number=[i for i in range(1,1000000)]
print(sum(number))
shu=[3,6,9,12,15,18,21,24,27,30]
for i in shu:
    print(i)
shu_1=[]
#利用append的方式
for i in range(1,11):
    shu_1.append(i**3)
print(shu_1)
#列表推导式
shu=[i**3 for i in range(1,11)]
print(shu)