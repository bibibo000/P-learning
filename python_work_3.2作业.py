candidate=["毛泽东",'爷爷','周恩来','卢昱晓',"刘翔"]
print(candidate)
pity=candidate[4]
print(f"非常可惜地告诉大家{pity}可能无法参加这次晚会")
candidate[4]="猪猪侠"
print(f'但是很高兴地告诉大家{candidate[4]}可以参加这次晚会')
print(f'所以名单就是{candidate},敬请期待吧！')
candidate.insert(0,"孙悟空")
print(candidate)
candidate.insert(3,"赛罗")
candidate.append("钢铁侠")
print(candidate)
print(f"oh no!,{candidate}很抱歉我今天出来没带够钱,只能邀请两人聚会")
endone=candidate.pop(1)
endtwo=candidate.pop(1)
for i in candidate:
    print(f"很抱歉,{i}不能参加这次晚会")
print(f"但是很高兴地告诉大家{endone}和{endtwo}可以参加这次晚会")
end=[endone,endtwo]
del end[0:3]
print(end)
