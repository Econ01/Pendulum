import math
import sys
import matplotlib.pyplot as plt

time = []
w = []
Q = []
dt = float
g = 9.8
l = float
q = 1.0
f_driving = 0.2
omega_driving = 2.0
a = float
b = float
c = float

def setup():
    global dt,l,g
    w.insert(0,0.0)
    time.insert(0,0.0)
    print("What is the angle between normal:")
    Q.insert(0,float(input()))
    print("Lenght of the rope:")
    l = input()
    print("Time interval:")
    dt = input()

def calculate():
    global g,l,dt,q,omega_driving,f_driving,a,b,c
    for i in range(9999):
        time.insert(i+1,float(time[i])+float(dt))
        a = ((float(g)/float(l)*float(Q[i]))*float(dt))
        b = ((float(q)*float(w[i]))*float(dt))
        c = ((f_driving*math.sin(omega_driving*float(time[i]))))
        w.insert(i+1,float(w[i])-float(a)-float(b)+float(c))
        Q.insert(i+1,float(Q[i])+float(w[i+1])*float(dt))


def draw_graph():
    plt.plot(time,Q)
    plt.xlabel("Time (s)")
    plt.ylabel("Degree (Q)")
    plt.show()

setup()
calculate()
draw_graph()
