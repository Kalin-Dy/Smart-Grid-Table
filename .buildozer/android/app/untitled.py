from tkinter import *
import tkinter as tk
import paho.mqtt.client as paho

broker="192.168.137.164"
#broker="127.000.000.001"
port=1883

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass


def Red():
    client1.publish("Red", "1")

def Yellow():
    client1.publish("Yellow", "1")

def Blue():
     client1.publish("Blue", "1")

def Purple():
    client1.publish("Purple", "1")

def Green():
    client1.publish("Green", "1")

def White():
    client1.publish("White", "1")


client1= paho.Client("Photon Controller")                           #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.connect(broker,port)                                 #establish connection



window = tk.Tk()
frame = tk.Frame(window)
frame.pack()

window.title("CBK Engineering DCML Testbench")

window.geometry('700x300')

Label=tk.Label(window, text="Led Status")
TopicLabel=tk.Label(window, text="Topic")
PayloadLabel=tk.Label(window, text="Payload")
TopicBox=Text(window,height =2,width=10)
ValueBox=Text(window,height =2,width=10)
btn1 = tk.Button(window, text="Red", command = Red)
btn2 = tk.Button(window, text="Yellow", command = Yellow)
btn3 = tk.Button(window, text="Blue", command = Blue)
btn4 = tk.Button(window, text="Purple", command = Purple)
btn5 = tk.Button(window, text="Green", command = Green)
btn6 = tk.Button(window, text="White", command = White)
payloadbtn=tk.Button(window, text="add",command =retrieve_input)


TopicLabel.pack(side=tk.RIGHT , anchor="n")
TopicBox.pack(side=tk.RIGHT, anchor="n")
PayloadLabel.pack(side=tk.RIGHT,anchor="n")
ValueBox.pack(side=tk.RIGHT, anchor="n")
payloadbtn.pack(side=tk.RIGHT, anchor="n")
Label.pack(side=tk.TOP,anchor="w")
btn1.pack(side=tk.TOP, anchor="w")
btn2.pack(side=tk.TOP, anchor="w")
btn3.pack(side=tk.TOP, anchor="w")
btn4.pack(side=tk.TOP, anchor="w")
btn5.pack(side=tk.TOP, anchor="w")
btn6.pack(side=tk.TOP, anchor="w")


window.mainloop()