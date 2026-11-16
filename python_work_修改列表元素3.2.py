car=["Toyota","Honda","BMW","Audi"]
print(car)
#这是改数据
car[0]="BYD"
print(car)
#这是加数据
car.append("Tesla")
print(car)
car.insert(0,"Chery")
print(car)
car.insert(3,"Nissan")
print(car)
#这是删数据
del car[2]
print(car)
#运用pop删除数据      pop就是弹出
best_car=car.pop(0)
print(f'I think the best car is {best_car}.')
print(car)
car.append("Mazda")
print(car)
car.insert(1,"Ford")
print(car)
#这是运用remove删除数据
cheap_car="Ford"
car.remove(cheap_car)
print(f'{cheap_car} is too cheap for me.')
