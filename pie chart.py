import turtle
from random import randint

names_list = list()
faravani_list = list()
sum_faravani = 0

print("Enter name of field, then a space and then frequency of field, and then enter.")
print("When fields finish, type \"done\".")

while True:
    data = input() #name dade, fasele, faravani, enter, edame..., vaghti tamoom shod "done"
    #mesal:
    #goroohe_seni_alef 30
    #goroohe_seni_be 70
    #goroohe_seni_jim 48
    #done
    
    if data == "done" :
        break
    name, faravani = data.split()
    names_list.append(name)
    faravani_list.append(int(faravani))
    sum_faravani += int(faravani)
    
turtle.pensize(2)
turtle.colormode(255)

for i in range(len(names_list)):
    turtle.color(randint(0, 255),
                 randint(0, 255),
                 randint(0, 255))
    turtle.begin_fill()
    turtle.fd(100)
    turtle.left(90)
    turtle.circle(100, (faravani_list[i] / sum_faravani) * 360)
    turtle.left(90)
    turtle.fd(100)
    turtle.right(180)
    turtle.end_fill()
    
turtle.color("black")    
for i in range(len(names_list)):
    turtle.fd(100)
    turtle.left(90)
    turtle.circle(100, (faravani_list[i] / sum_faravani) * 360)
    turtle.left(90)
    turtle.fd(100)
    turtle.right(180)
    turtle.pu()
    turtle.right((faravani_list[i] / sum_faravani) * 180)
    turtle.fd(130)
    turtle.pd()
    turtle.write(names_list[i])
    turtle.pu()
    turtle.right(180)
    turtle.fd(130)
    turtle.right(180)
    turtle.left((faravani_list[i] / sum_faravani) * 180)
    turtle.pd()
    
turtle.done()
