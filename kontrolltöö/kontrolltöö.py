#1
n = int(input("Kirjuta number 1-9, mitu sa tahad majakest: "))

for i in range(n):
    print("  ~~~~~  ")
    print(" /_____\\")
    print(" | []  | ")
    print("  ----- ")
    if i!= n-1:
        print("          ")

#2
n = int(input("Kirjuta mittu klassis on inimest?. :"))
klass_1 = []
klass_2 = []
for i in range(n):
    hinne = int(input(f"Kirjuta opilase {i+1}, esimese klassi hinnet. :"))
    klass_1.append(hinne)
for i in range(n):
    hinne = int(input(f"Kirjuta opilase {i+1}, teise klassi hinnet. :"))
    klass_2.append(hinne)
klass_1_average = sum(klass_1)/n
klass_2_average = sum(klass_2)/n
print("keskmine esimese klassi hind:", klass_1_average)
print("keskmine teise klassi hind:", klass_2_average)

#3
import random
n = int(input("Kirjuta mittu õpilast klassis.: "))
marks = []
for i in range(n):
    mark = random.randint(1, 5)
    marks.append(mark)
min_mark = marks[0]
max_mark = marks[0]
for i in range(1,n):
    if marks[i] < min_mark:
        min_mark = marks[i]
    if marks[i] > max_mark:
        max_mark = marks[i]
print("Minimum mark:", min_mark)
print("Maximum mark:", max_mark)


#4
import random
n = int(input("Kirjuta mittu inimest piirkonnas on.: "))

districts = 12
population = 0
area = 0

for i in range(districts):
    district_population = random.randint(1000, 10000)
    district_area = random.randint(100, 1000)
    population += district_population
    area += district_area

average_density = population / area
print("Keskmine rahvastikutihedus:", average_density, "inimene/km^2")

#5
x_min = float(input("Sisestage x minimaalne väärtus: "))
x_max = float(input("Sisestage x maksimaalne väärtus: "))
step = float(input("Juurdekasvu väärtuse x sisestamine: "))

x = x_min
print("x\t\ty") #table headers
while x<=x_max:
    y = -0.5*x + x
    print(x,"\t",y)
