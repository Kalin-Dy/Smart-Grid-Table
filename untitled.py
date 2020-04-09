# 11.03.2020 Smart Grid GUI v0.7 By Kalin Dyankov
# Importing Tkinter and paho for mqqtt support and tkinter GUI widgets
from tkinter import *
import tkinter as tk
import paho.mqtt.client as paho

# Initialising broker and port for the mqtt connection
broker = "broker.hivemq.com"
#broker="192.168.0.105"
# broker="192.168.43.6"
port = 1883


def LightMode(
        event):  ### This function sets the colour for all the elements to the default colour, the varible event is used so it can be Binded to an action
    window.configure(background='lightgray')
    SubmitMVButton.configure(foreground='black', background='lightgray')
    SubmitLVButton.configure(foreground='black', background='lightgrey')
    SubmitHVButton.configure(foreground='black', background='lightgrey')
    LVLabel.configure(foreground='black', background='lightgrey')
    HVLabel.configure(foreground='black', background='lightgrey')
    MVLabel.configure(foreground='black', background='lightgrey')
    GeneratorButton.configure(foreground='black', background='lightgrey')
    MediumVoltageButton.configure(foreground='black', background='lightgrey')
    LowVoltageButton.configure(foreground='black', background='lightgrey')
    HighVoltageList.configure(foreground='black', background='white')
    MediumVoltageList.configure(foreground='black', background='white')
    LowVoltageList.configure(foreground='black', background='white')
    PayloadLabel.configure(foreground='black', background='lightgrey')
    ValueBox.configure(foreground='black', background='white')


def DarkMode(
        event):  ### This function sets the colour for all the elements to a dark colour, the varible event is used so it can be Binded to an action
    window.configure(background='black')
    SubmitMVButton.configure(foreground='white', background='black')
    SubmitLVButton.configure(foreground='white', background='black')
    SubmitHVButton.configure(foreground='white', background='black')
    LVLabel.configure(foreground='white', background='black')
    HVLabel.configure(foreground='white', background='black')
    MVLabel.configure(foreground='white', background='black')
    GeneratorButton.configure(foreground='white', background='black')
    MediumVoltageButton.configure(foreground='white', background='black')
    LowVoltageButton.configure(foreground='white', background='black')
    HighVoltageList.configure(foreground='white', background='black')
    MediumVoltageList.configure(foreground='white', background='black')
    LowVoltageList.configure(foreground='white', background='black')
    PayloadLabel.configure(foreground='white', background='black')
    ValueBox.configure(foreground='white', background='black')


def ShowMediumVoltage():  ### This function hides all the unnecessary widgets showing only the ones used for the medium voltage building selection, note that th pack_forget() and .pack methods require this strict sequence.
    SubmitLVButton.pack_forget()
    SubmitHVButton.pack_forget()
    LVLabel.pack_forget()
    HVLabel.pack_forget()
    LowVoltageList.pack_forget()
    HighVoltageList.pack_forget()
    PayloadLabel.pack(side=tk.TOP,
                      anchor="n")  ### side=TOP and andchor N stand for top and North to ensure that the widget is placed on top in the middle of the window
    ValueBox.pack(side=tk.TOP, anchor="n")
    SubmitMVButton.pack(side=tk.TOP, anchor="n")
    MVLabel.pack(side=TOP)
    MediumVoltageList.pack(side=LEFT, fill=Y, expand=1)


def ShowLowVoltage():  ## This function hides all the unnecessary widgets showing only the ones used for the Low voltage building selection, note that th pack_forget() and .pack methods require this strict sequence.
    MVLabel.pack_forget()
    HVLabel.pack_forget()
    SubmitHVButton.pack_forget()
    SubmitMVButton.pack_forget()
    MediumVoltageList.pack_forget()
    HighVoltageList.pack_forget()
    PayloadLabel.pack(side=tk.TOP, anchor="n")
    ValueBox.pack(side=tk.TOP, anchor="n")
    SubmitLVButton.pack(side=tk.TOP, anchor="n")
    LVLabel.pack(side=TOP)
    LowVoltageList.pack(side=LEFT, fill=Y, expand=1)


def ShowGenerators():  ## This function hides all the unnecessary widgets showing only the ones used for the Generator/storage selection, note that th pack_forget() and .pack methods require this strict sequence.
    SubmitLVButton.pack_forget()
    SubmitMVButton.pack_forget()
    LVLabel.pack_forget()
    MVLabel.pack_forget()
    LowVoltageList.pack_forget()
    MediumVoltageList.pack_forget()
    PayloadLabel.pack(side=tk.TOP, anchor="n")
    ValueBox.pack(side=tk.TOP, anchor="n")
    SubmitHVButton.pack(side=tk.TOP, anchor="n")
    HVLabel.pack(side=TOP)
    HighVoltageList.pack(side=LEFT, fill=Y, expand=1)


def on_publish(client, userdata, result):  # create function for callback
    print("data published \n")
    pass


def retrieveMV_input():  ### Sends the data from the Value box on a chosen topic by the list appending p_set for the Json file
    inputValue = "p_set: "+ ValueBox.get("1.0", "end-1c")
    TopicValue = "None"
    Selection = MediumVoltageList.get(
        MediumVoltageList.curselection())  ### takes the data from selected item on the listbox
    if Selection == "HAN":
        TopicValue = "sendToPc/3920405579"
    elif Selection == "HAN2":
        TopicValue = "sendToPc/282947826"
    elif Selection == "HAN3":
        TopicValue = "sendToPc/4026521350"
    elif Selection == "Factory":
        TopicValue = "sendToPc/2310161908"
    elif Selection == "Factory 2":
        TopicValue = "sendToPc/4051964182"
    elif Selection == "Fueling station":
        TopicValue = "sendToPc/2052891520"
    elif Selection == "Processing factory":
        TopicValue = "sendToPc/605299859"
    elif Selection == "Chemical factory":
        TopicValue = "sendToPc/3649958435"
    elif Selection == "Charging station":
        TopicValue = "sendToPc/2310052191"
    if ValueBox.get("1.0", "end-1c") == "Darkmode":
        DarkMode()
    elif ValueBox.get("1.0", "end-1c") == "Lightmode":
        LightMode()
    client1.publish(TopicValue, inputValue)  ### Publishes data to mqtt broker
    ValueBox.delete("1.0", "end-1c")


def Generators_input():  ### This function sends the data from the Value box on a chosen topic by the list appending p_set for the Json file
    inputValue = "p_nom: " + ValueBox.get("1.0", "end-1c")
    TopicValue = "None"
    Selection = HighVoltageList.get(
        HighVoltageList.curselection())  ### takes the data from selected item on the listbox
    if Selection == "Nuclear Generator -HV":
        TopicValue = "sendToPc/2309930275"
    elif Selection == "Powerplant -HV":
        TopicValue = "sendToPc/527238502"
    elif Selection == "Coal Powerplant -HV":
        TopicValue = "sendToPc/295733986"
    elif Selection == "Nuclear Powerplant -HV":
        TopicValue = "sendToPc/3920381746"
    elif Selection == "Wind Generator -MV":
        TopicValue = "sendToPc/698489018"
    elif Selection == "HydroStation -MV":
        TopicValue = "sendToPc/2052891520"
    elif Selection == "Solar farm -MV":
        TopicValue = "sendToPc/2052767824"
    elif Selection == "Solar farm 2 -MV":
        TopicValue = "sendToPc/695262796"
    elif Selection == "Wind Solar -MV":
        TopicValue = "sendToPc/1506226421"
    elif Selection == "Storage1":
        TopicValue = "sendToPc/2846345288"
    elif Selection == "Storage2":
        TopicValue = "sendToPc/2052791472"
    elif Selection == "Storage3":
        TopicValue = "sendToPc/2310197510"
    elif Selection == "Battery storage":
        TopicValue = "sendToPc/3649465219"
    elif Selection == "Battery storage2":
        TopicValue = "sendToPc/360927797"
    elif Selection == "Neighbourhood Battery":
        TopicValue = "sendToPc/2309993847"
    elif Selection == "Solar farm without motor":
        TopicValue = "sendToPc/2309849586"
    elif Selection == "Solar farm small 1":
        TopicValue = "sendToPc/18990810"
    elif Selection == "Solar farm small 2":
        TopicValue = "sendToPc/3647830435"
    elif Selection == "Solar farm without solar panels":
        TopicValue = "sendToPc/3648096051"
    elif Selection == "Hydropower dam":
        TopicValue = "sendToPc/3846378531"
    elif Selection == "Nuclear powerplant 2":
        TopicValue = "sendToPc/168401146"
    elif Selection == "Solar farm 3":
        TopicValue = "sendToPc/515442678"
    if ValueBox.get("1.0", "end-1c") == "Darkmode":
        DarkMode()
    elif ValueBox.get("1.0", "end-1c") == "Lightmode":
        LightMode()
    client1.publish(TopicValue, inputValue)  ###Publishes dat to mqtt Broker
    ValueBox.delete("1.0", "end-1c")


def retrieveLV_input():  ### Sends the data from the Value box on a chosen topic by the list appending p_set for the Json file
    inputValue = "p_set: " + ValueBox.get("1.0", "end-1c")
    TopicValue = "None"
    Selection = LowVoltageList.get(LowVoltageList.curselection())
    if Selection == "Load":
        TopicValue = "sendToPc/2052517040"
    elif Selection == "Farm":
        TopicValue == "sendToPc/4066949349"
    elif Selection == "House":
        TopicValue = "sendToPc/2052817936"
    elif Selection == "Appartment":
        TopicValue = "sendToPc/3920341176"
    elif Selection == "Appartment2":
        TopicValue = "sendToPc/4025224262"
    elif Selection == "Appartment3":
        TopicValue = "sendToPc/2053040528"
    elif Selection == "Appartment4":
        TopicValue = "sendToPc/3688487909"
    elif Selection == "Appartment5":
        TopicValue = "sendToPc/72823031"
    elif Selection == "Appartment6":
        TopicValue = "sendToPc/3846246323"
    elif Selection == "Packhouse":
        TopicValue = "sendToPc/2310135841"
    elif Selection == "Charging station":
        TopicValue = "sendToPc/610176659"
    elif Selection == "Car charging station":
        TopicValue = "sendToPc/586463298"
    elif Selection == "Car charging station 2":
        TopicValue = "sendToPc/2310052343"
    elif Selection == "Packhouse2":
        TopicValue = "sendToPc/3920294633"
    elif Selection == "Hospital":
        TopicValue = "sendToPc/4024653174"
    elif Selection == "Hospital2":
        TopicValue = "sendToPc/3649459203"
    elif Selection == "Hospital3":
        TopicValue = "sendToPc/536179654"
    elif Selection == "Hospital4":
        TopicValue = "sendToPc/4026693430"
    elif Selection == "Terrace house 1":
        TopicValue = "sendToPc/695368886"
    elif Selection == "Terrace house 3":
        TopicValue = "sendToPc/3649886163"
    elif Selection == "Terrace house 2":
        TopicValue = "sendToPc/2052180480"
    elif Selection == "Detached house":
        TopicValue = "sendToPc/3649488643"
    elif Selection == "Detached house 2":
        TopicValue = "sendToPc/786497569"
    elif Selection == "Detached house 3":
        TopicValue = "sendToPc/525736038"
    elif Selection == "Shopping Mall":
        TopicValue = "sendToPc/2310254414"
    client1.publish(TopicValue, inputValue)
    ValueBox.delete("1.0", "end-1c")


def ShowlVValues(event):
    Selection = LowVoltageList.get(LowVoltageList.curselection())
    if Selection == "Load":
        maxValue = 100
        minValue = 15
        String = ("Load Selected, set power", minValue, "-" , maxValue)
        frame.text.set(String)
    elif Selection == "House":
        minValue = 25
        maxValue = 200
        String = 'House Selected, set power', minValue,'-', maxValue
        frame.text.set(String)
    elif Selection == "Appartment":
        minValue = 5
        maxValue = 60
        String = 'Appartment Selected, set power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Appartment2":
        minValue = 5
        maxValue = 60
        String = 'Appartment 2 Selected, set power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Appartment3":
        minValue = 5
        maxValue = 60
        String = 'Appartment 3 Selected, set power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Appartment4":
        minValue = 5
        maxValue = 60
        String = 'Appartment 4 Selected, set power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Appartment5":
        minValue = 5
        maxValue = 60
        String = 'Appartment 5 Selected, set power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Appartment6":
        minValue = 5
        maxValue = 60
        String = 'Appartment 6 Selected, set power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Packhouse":
        minValue = 30
        maxValue = 400
        String = 'Packhouse Selected, set power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Charging station":
        minValue = 100
        maxValue = 1000
        String = 'Charging station Selected, set power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Car charging station":
        minValue = 200
        maxValue = 3000
        String = 'Car charging station Selected, set power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Car charging station 2":
        minValue = 200
        maxValue = 3000
        String = 'Car charging station 2 Selected, set power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Packhouse2":
        minValue = 30
        maxValue = 400
        String = 'Packhouse Selected, set power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Hospital":
        minValue = 80
        maxValue = 1000
        String = 'Hospital Selected, set power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Hospital2":
        minValue = 80
        maxValue = 1000
        String = 'Hospital 2 Selected, set power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Hospital3":
        minValue = 80
        maxValue = 1000
        String = 'Hospital 3 Selected, set power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "sendToPc/Hospital4":
        minValue = 80
        maxValue = 1000
        String = 'Hospital 4 Selected, set power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Terrace house 1":
        minValue = 15
        maxValue = 100
        String = 'Terrace house 1 Selected, set power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Terrace house 3":
        minValue = 15
        maxValue = 100
        String = 'Terrace house 3 Selected, set power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Detached house":
        minValue = 80
        maxValue = 1000
        String = 'Detached house Selected, set power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Detached house 2":
        minValue = 80
        maxValue = 1000
        String = 'Detached house 2 Selected, set power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Detached house 3":
        minValue = 80
        maxValue = 1000
        String = 'Detached house 3 Selected, set power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Shopping Mall":
        minValue = 80
        maxValue = 1000
        String = 'Shopping Mall Selected, set power', minValue, '-', maxValue
        frame.text.set(String)
def ShowMVValues(event):
    Selection = MediumVoltageList.get(MediumVoltageList.curselection())  ### takes the data from selected item on the listbox
    if Selection == "HAN":
        minValue = 150
        maxValue = 1000
        String = 'HAN Selected, set power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "HAN2":
        minValue = 150
        maxValue = 1000
        String = 'HAN 2 Selected, set power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "HAN3":
        minValue = 150
        maxValue = 1000
        String = 'HAN 3 Selected, set power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Factory":
        minValue = 150
        maxValue = 1000
        String = 'Factory Selected, set power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Factory 2":
        minValue = 150
        maxValue = 1000
        String = 'Factory 2 Selected, set power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Fueling station":
        minValue = 150
        maxValue = 1000
        String = 'Fueling station Selected, set power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Processing factory":
        minValue = 150
        maxValue = 1000
        String = 'Processing factory, set power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Chemical factory":
        minValue = 150
        maxValue = 1000
        String = 'Chemical factory Selected, set power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Charging station":
        minValue = 150
        maxValue = 1000
        String = 'Charging Station, set power', minValue, '-', maxValue
        frame.text.set(String)
def ShowGENValues(event):
    Selection = HighVoltageList.get(
        HighVoltageList.curselection())  ### takes the data from selected item on the listbox
    if Selection == "Nuclear Generator -HV":
        minValue = 150
        maxValue = 1000
        String = 'Nuclear Generator Selected, set generated power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Powerplant -HV":
        minValue = 150
        maxValue = 1000
        String = 'Powerplant  Selected, set generated power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Coal Powerplant -HV":
        minValue = 150
        maxValue = 1000
        String = 'Coal Powerplant Selected, set generated power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Nuclear Powerplant -HV":
        minValue = 150
        maxValue = 1000
        String = 'Nuclear Powerplant Selected, set generated power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Wind Generator -MV":
        minValue = 150
        maxValue = 1000
        String = 'Wind Generator Selected, set generated power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "HydroStation -MV":
        minValue = 150
        maxValue = 1000
        String = 'HydroStation Selected, set generated power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Solar farm -MV":
        minValue = 150
        maxValue = 1000
        String = 'Solar farm Selected, set generated power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Solar farm 2 -MV":
        minValue = 150
        maxValue = 1000
        String = 'Solar farm 2 Selected, set generated power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Wind Solar -MV":
        minValue = 150
        maxValue = 1000
        String = 'Wind Solar Selected, set generated power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Storage1":
        minValue = 150
        maxValue = 1000
        String = 'Storage 1 Selected, set stored power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Storage2":
        minValue = 150
        maxValue = 1000
        String = 'Storage 2 Selected, set stored power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Storage3":
        minValue = 150
        maxValue = 1000
        String = 'Storage 3 Selected, set stored power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Battery storage":
        minValue = 150
        maxValue = 1000
        String = 'Battery Storage Selected, set stored power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Battery storage2":
        minValue = 150
        maxValue = 1000
        String = 'Battery Storage 2 Selected, set stored power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Neighbourhood Battery":
        minValue = 150
        maxValue = 1000
        String = 'Neighbourhood Battery Selected, set stored power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Solar farm without motor":
        minValue = 150
        maxValue = 1000
        String = 'Solar farm without motor Selected, set generated power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Solar farm small 1":
        minValue = 150
        maxValue = 1000
        String = ' Small Solar farm Selected, set generated power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Solar farm small 2":
        minValue = 150
        maxValue = 1000
        String = 'Small Solar farm 2 Selected, set generated power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Solar farm without solar panels":
        minValue = 150
        maxValue = 1000
        String = 'Solar farm without solar panels Selected, set generated power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Hydropower dam":
        minValue = 150
        maxValue = 1000
        String = 'Hydropower dam Selected, set generated power', minValue, '-', maxValue
        frame.text.set(String)
    elif Selection == "Nuclear powerplant 2":
        minValue = 150
        maxValue = 1000
        String = 'Nuclear Powerplant 2 Powerplant Selected, set generated power', minValue, '-', maxValue
        frame.text.set(String)

client1 = paho.Client("Controller")  # create client object
client1.on_publish = on_publish  # assign function to callback
client1.connect(broker, port)  # establish connection

window = tk.Tk()  ### create window
frame = tk.Frame(window)  ### frame the window
frame.pack()  ### add the frame
frame.text = tk.StringVar()
window.title("Smart Table Demo GUI")  ### Window title

window.geometry('400x800')  ### window geometry in pixels
LowVoltageBlocks = ["Load", "Appartment", "Appartment2", "Appartment3", "Appartment4", "Packhouse", "Packhouse2",
                    "Hospital", "Hospital2", "Hospital3",
                    "Hospital4", "Terrace house 1","Terrace house 2", "Terrace house 3", "Detached house", "Detached house 2",
                    "Detached house 3", "Shopping Mall",
                    "Farm", "Appartment5", "Appartment6","Farm", "Car charging station", "Car charging station 2",
                    "Charging station", "House"]

MediumVoltageBlocks = ["HAN", "HAN2", "Fueling station", "Processing factory", "Chemical factory", "Charging station"
    , "HAN3", "Factory", "Factory 2", ]

HighVoltageBlocks = ["Nuclear Generator -HV", "Powerplant -HV", "Coal Powerplant -HV", "Nuclear Powerplant -HV",
                     "Wind Generator -MV", "HydroStation -MV",
                     "Solar farm -MV", "Wind Solar -MV", "Solar farm 2 -MV","Solar farm 3", "Storage1", "Storage2", "Storage3",
                     "Battery storage", "Battery storage2", "Neighbourhood Battery",
                     "Solar farm without motor", "Solar farm small 1", "Solar farm small 2",
                     "Solar farm without solar panels", "Hydropower dam", "Nuclear powerplant 2"]

LowVoltageList = Listbox(selectmode=SINGLE)  ### Sets the listbox so only one element can be selected at a time
MediumVoltageList = Listbox(selectmode=SINGLE)
HighVoltageList = Listbox(selectmode=SINGLE)
### For loops filling all the items in the corresponding listboxes
for item in LowVoltageBlocks:
    LowVoltageList.insert(END, item)
for item in MediumVoltageBlocks:
    MediumVoltageList.insert(END, item)
for item in HighVoltageBlocks:
    HighVoltageList.insert(END, item)

### Creation of the widgets and their attributes
LVLabel = tk.Label(window, text="Low Voltage Buildings")
MVLabel = tk.Label(window, text="Medium Voltage Buildings")
HVLabel = tk.Label(window, text="Generators")
PCLabel = tk.Label(window, textvariable=frame.text)
PayloadLabel = tk.Label(window, text="Power")

PCLabel.pack(side=tk.TOP, anchor="n")
frame.text.set("whoop whoop")
LowVoltageList.bind('<<ListboxSelect>>', ShowlVValues)
MediumVoltageList.bind('<<ListboxSelect>>',ShowMVValues)
HighVoltageList.bind('<<ListboxSelect>>',ShowGENValues)
PayloadLabel.bind("<Button-1>", DarkMode)  ### Binding the Darkmode() to a leftclick
PayloadLabel.bind("<Button-3>", LightMode)  ### Binding the Lightmode() to a rightclick
ValueBox = Text(window, height=2, width=10)  ### Sets dimentions for the Value textbox
SubmitLVButton = tk.Button(window, text="Send consumption power value", command=retrieveLV_input)  ### Binds functions to buttonclicks a
SubmitMVButton = tk.Button(window, text="Send consumption power value", command=retrieveMV_input)
SubmitHVButton = tk.Button(window, text="Send Generator nominal power", command=Generators_input)
LowVoltageButton = tk.Button(window, text='Low Voltage Loads', command=ShowLowVoltage)
MediumVoltageButton = tk.Button(window, text='Medium Voltage loads', command=ShowMediumVoltage)
GeneratorButton = tk.Button(window, text='Generators', command=ShowGenerators)
ExitButton = tk.Button(window, text='X', command=exit)  ### X button to close the program
ExitButton.pack(side=tk.LEFT, anchor="nw")  ### adding the exit button to the GUI window
ExitButton.configure(background='red', foreground='white')
LowVoltageButton.pack(side=tk.BOTTOM, anchor="e")  ### Adding the Low medium and generator buttons to the window
MediumVoltageButton.pack(side=tk.BOTTOM, anchor="e")
GeneratorButton.pack(side=tk.BOTTOM, anchor="e")
window.mainloop()  ### Starts the loop of the window
