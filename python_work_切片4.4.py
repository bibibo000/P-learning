name=['jake','mike','jone','helon',"bob"]
print(name[1:3])
print(name[:3])
print(name[1:])
print(name[-2:])
print(name[-4:-2])#如你所见输出结果一定是从左到右所以是-4到-2而非-2到-4
print('以下是获奖名单：')
for i in name[:4]:
    print(f"\t\t{i}")
hate=["豆芽",'肉松','辣椒','海带']
very_hate=hate[:]
print(f"我不喜欢的食物有{hate}")
print(f"我非常不喜欢的食物也是{very_hate}")
