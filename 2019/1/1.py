import math


def calc_fuel(a):
    return math.floor(a/3)-2

def calc_fuel_all(arr):
    fuel=0
    for i in arr:
        part=i
        while True:
            part=calc_fuel(part)
            if part>0:
                fuel+=part
            else:
                break;
    return fuel

a=[]

with open("in.txt") as f:
    for line in f.readlines():
        a.append(int(line))

print calc_fuel_all(a)
