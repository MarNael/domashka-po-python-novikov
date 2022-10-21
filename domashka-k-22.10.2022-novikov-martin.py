#Вводится вектор. Вывести максимум из его элементов.
vector=input()
vector_list=[int(x) for x in vector.split()]
print(max(vector_list))

#Вводится вектор. Заменить в нём каждое число Фибоначчи на следующее.
def check1(x):
  return ((5*(x**2)+4)**0.5)%1==0
def check2(x):
  return ((5*(x**2)-4)**0.5)%1==0
number=input()
number_list=[int(x) for x in number.split()]
for i in range(len(number_list)):
  if check1(number_list[i]) or check2(number_list[i]):
    fib=[1,1]
    k=1
    s=number_list[i]
    while fib[k]<=s:
      fib.append(fib[k-1]+fib[k])
      if fib[k]==s:
        number_list[i]=fib[k+1]
      k+=1
print(number_list)

#Напишите программу, которая помогает определить какие вещи могут поместиться в рюкзак. Вводится существующий объем рюкзака. Затем вводятся объемы всех вещей, которые хочется туда поместить. Нужно вывести список объемов вещей, которые поместятся в рюкзак. Постарайтесь максимизировать кол-во вошедших вещей.
volume = int(input())
objects = input()
objects_list = [int(x) for x in objects.split()]
objects_list.sort()
total_sum = 0
objects_sum = []
for i in range(len(objects_list)):
  if total_sum+objects_list[i]<volume:
    total_sum+=objects_list[i]
    objects_sum.append(objects_list[i])
print(objects_sum)

#Данные об email-адресах студентов хранятся в словаре: {домен:логины} . Нужно дополнить код таким образом, чтобы он вывел все адреса в алфавитном порядке и в формате имя_пользователя@домен
domens = {"rea.ru": ["misha", "pasha"], "study.com": ["olga", "nastay", "igor"]}
i = 0
total_list = []
for dom, logins in domens.items():
  i+=1
  logins=str(logins)[1:len(str(logins))-1]
  logins_list=logins.split(', ')
  for k in range(len(logins_list)):
    total_list.append(logins_list[k][1:len(logins_list[k])-1]+'@'+dom)
print(sorted(total_list))





