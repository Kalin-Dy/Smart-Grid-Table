# 11.03.2020 Smart Grid GUI v0.7 By Kalin Dyankov
# Importing Tkinter and paho for mqqtt support and tkinter GUI widgets

import paho.mqtt.client as paho
import tkinter as tk
from tkinter import *
from tkinter import messagebox

# Initialising broker and port for the mqtt connection
broker = "broker.hivemq.com"
#broker="192.168.0.105"
# broker="192.168.43.6"
port = 1883
class Building:
    minValue = 0
    maxValue = 10
class Load(Building):
    minValue=  15
    maxValue = 100
class Appartment(Building):
    minValue = 5
    maxValue = 60
class Packhouse(Building):
    minValue = 30
    maxValue = 400
class Hospital(Building):
    minValue = 80
    maxValue = 1000
class TerraceHouse(Building):
    minValue = 15
    maxValue = 100
class DetachedHouse(Building):
    minValue = 80
    maxValue = 1000
class ShoppingMall(Building):
    minValue = 80
    maxValue = 1000
class Farm(Building):   ##String don work
    minValue = 10
    maxValue = 500
class CarChargingStation(Building):
    minValue = 200
    maxValue = 3000
class ChargingStation(Building):
    minValue = 100
    maxValue = 1000
class House(Building):
    minValue = 25
    maxValue = 200
class HAN(Building):
    minValue = 150
    maxValue = 1000
class FuelingStation(Building):
    minValue = 150
    maxValue = 1000
class ProcessingFactory(Building):
    minValue = 150
    maxValue = 1000
class ChemicalFactory(Building):
    minValue = 150
    maxValue = 1000
class Factory(Building):
    minValue = 150
    maxValue = 1000
class NuclearGenerator(Building):
    minValue = 150
    maxValue = 1000
class Powerplant(Building):
    minValue = 150
    maxValue = 1000
class CoalPowerplant(Building):
    minValue = 150
    maxValue = 1000
class WindGenerator(Building):
    minValue = 150
    maxValue = 1000
class NuclearPowerplant(Building):
    minValue = 150
    maxValue = 1000
class Hydrostation(Building):
    minValue = 150
    maxValue = 1000
class SolarFarm(Building):
    minValue = 150
    maxValue = 1000
class WindSolar(Building):
    minValue = 150
    maxValue = 1000
class Storage(Building):
    minValue = 150
    maxValue = 1000
class Battery(Building):
    minValue = 150
    maxValue = 1000
class SmallSolarFarm(Building):
    minValue = 150
    maxValue = 1000
class HydropowerDam(Building):
    minValue = 150
    maxValue = 1000

def CheckRange(low,high,power,TopicValue,inputValue):
    if(power<low or power>high):
        Errormsg.showerror(title="Power Error", message="Power not within acceptable range")
    else:
        client1.publish(TopicValue, inputValue)


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
    Power = int(ValueBox.get("1.0", "end-1c"))
    Selection = MediumVoltageList.get(
        MediumVoltageList.curselection())  ### takes the data from selected item on the listbox
    if Selection == "HAN":
        TopicValue = "sendToPc/3920405579"
        CheckRange(HAN.minValue, HAN.maxValue, Power, TopicValue, inputValue)
    elif Selection == "HAN2":
        TopicValue = "sendToPc/282947826"
        CheckRange(HAN.minValue, HAN.maxValue, Power, TopicValue, inputValue)
    elif Selection == "HAN3":
        TopicValue = "sendToPc/4026521350"
        CheckRange(HAN.minValue, HAN.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Factory":
        TopicValue = "sendToPc/2310161908"
        CheckRange(Factory.minValue, Factory.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Factory 2":
        TopicValue = "sendToPc/4051964182"
        CheckRange(Factory.minValue, Factory.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Fueling station":
        TopicValue = "sendToPc/2052891520"
        CheckRange(FuelingStation.minValue, FuelingStation.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Processing factory":
        TopicValue = "sendToPc/605299859"
        CheckRange(ProcessingFactory.minValue, ProcessingFactory.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Chemical factory":
        TopicValue = "sendToPc/3649958435"
        CheckRange(ChemicalFactory.minValue, ChemicalFactory.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Charging station":
        TopicValue = "sendToPc/2310052191"
        CheckRange(ChargingStation.minValue, ChargingStation.maxValue, Power, TopicValue, inputValue)

    ValueBox.delete("1.0", "end-1c")


def Generators_input():  ### This function sends the data from the Value box on a chosen topic by the list appending p_set for the Json file
    inputValue = "p_nom: " + ValueBox.get("1.0", "end-1c")
    TopicValue = "None"
    Power = int(ValueBox.get("1.0", "end-1c"))
    Selection = HighVoltageList.get(
        HighVoltageList.curselection())  ### takes the data from selected item on the listbox
    if Selection == "Nuclear Generator -HV":
        TopicValue = "sendToPc/2309930275"
        CheckRange(NuclearGenerator.minValue,NuclearGenerator.maxValue,Power,TopicValue,inputValue)
    elif Selection == "Powerplant -HV":
        TopicValue = "sendToPc/527238502"
        CheckRange(Powerplant.minValue, Powerplant.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Coal Powerplant -HV":
        TopicValue = "sendToPc/295733986"
        CheckRange(CoalPowerplant.minValue, CoalPowerplant.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Nuclear Powerplant -HV":
        TopicValue = "sendToPc/3920381746"
        CheckRange(NuclearPowerplant.minValue, NuclearPowerplant.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Wind Generator -MV":
        TopicValue = "sendToPc/698489018"
        CheckRange(WindGenerator.minValue, WindGenerator.maxValue, Power, TopicValue, inputValue)
    elif Selection == "HydroStation -MV":
        TopicValue = "sendToPc/2052891520"
        CheckRange(Hydrostation.minValue, Hydrostation.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Solar farm -MV":
        TopicValue = "sendToPc/2052767824"
        CheckRange(SolarFarm.minValue, SolarFarm.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Solar farm 2 -MV":
        TopicValue = "sendToPc/695262796"
        CheckRange(SolarFarm.minValue, SolarFarm.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Wind Solar -MV":
        TopicValue = "sendToPc/1506226421"
        CheckRange(WindSolar.minValue, WindSolar.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Storage1":
        TopicValue = "sendToPc/2846345288"
        CheckRange(Storage.minValue, Storage.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Storage2":
        TopicValue = "sendToPc/2052791472"
        CheckRange(Storage.minValue, Storage.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Storage3":
        TopicValue = "sendToPc/2310197510"
        CheckRange(Storage.minValue, Storage.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Battery storage":
        TopicValue = "sendToPc/3649465219"
        CheckRange(Battery.minValue, Battery.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Battery storage2":
        TopicValue = "sendToPc/360927797"
        CheckRange(Battery.minValue, Battery.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Neighbourhood Battery":
        TopicValue = "sendToPc/2309993847"
        CheckRange(Battery.minValue, Battery.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Solar farm without motor":
        TopicValue = "sendToPc/2309849586"
        CheckRange(SolarFarm.minValue, SolarFarm.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Solar farm small 1":
        TopicValue = "sendToPc/18990810"
        CheckRange(SmallSolarFarm.minValue, SmallSolarFarm.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Solar farm small 2":
        TopicValue = "sendToPc/3647830435"
        CheckRange(SmallSolarFarm.minValue, SmallSolarFarm.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Solar farm without solar panels":
        TopicValue = "sendToPc/3648096051"
        CheckRange(SolarFarm.minValue, SolarFarm.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Hydropower dam":
        TopicValue = "sendToPc/3846378531"
        CheckRange(HydropowerDam.minValue, HydropowerDam.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Nuclear powerplant 2":
        TopicValue = "sendToPc/168401146"
        CheckRange(NuclearPowerplant.minValue, NuclearPowerplant.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Solar farm 3":
        TopicValue = "sendToPc/515442678"
        CheckRange(SolarFarm.minValue, SolarFarm.maxValue, Power, TopicValue, inputValue)
    ##client1.publish(TopicValue, inputValue)  ###Publishes dat to mqtt Broker
    ValueBox.delete("1.0", "end-1c")
def retrieveLV_input():  ### Sends the data from the Value box on a chosen topic by the list appending p_set for the Json file
    inputValue = "p_set: " + ValueBox.get("1.0", "end-1c")
    TopicValue = "None"
    Power = int(ValueBox.get("1.0", "end-1c"))
    Selection = LowVoltageList.get(LowVoltageList.curselection())
    if Selection == "Load":
        TopicValue = "sendToPc/2052517040"
        CheckRange(Load.minValue,Load.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Farm":
        TopicValue == "sendToPc/4066949349"
        CheckRange(Farm.minValue, Farm.maxValue, Power, TopicValue, inputValue)
    elif Selection == "House":
        TopicValue = "sendToPc/2052817936"
        CheckRange(House.minValue, House.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Appartment":
        TopicValue = "sendToPc/3920341176"
        CheckRange(Appartment.minValue, Appartment.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Appartment2":
        TopicValue = "sendToPc/4025224262"
        CheckRange(Appartment.minValue, Appartment.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Appartment3":
        TopicValue = "sendToPc/2053040528"
        CheckRange(Appartment.minValue, Appartment.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Appartment4":
        TopicValue = "sendToPc/3688487909"
        CheckRange(Appartment.minValue, Appartment.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Appartment5":
        TopicValue = "sendToPc/72823031"
        CheckRange(Appartment.minValue, Appartment.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Appartment6":
        TopicValue = "sendToPc/3846246323"
        CheckRange(Appartment.minValue, Appartment.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Packhouse":
        TopicValue = "sendToPc/2310135841"
        CheckRange(Packhouse.minValue, Packhouse.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Charging station":
        TopicValue = "sendToPc/610176659"
        CheckRange(ChargingStation.minValue, ChargingStation.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Car charging station":
        TopicValue = "sendToPc/586463298"
        CheckRange(CarChargingStation.minValue,CarChargingStation.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Car charging station 2":
        TopicValue = "sendToPc/2310052343"
        CheckRange(CarChargingStation.minValue,CarChargingStation.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Packhouse2":
        TopicValue = "sendToPc/3920294633"
        CheckRange(Packhouse.minValue, Packhouse.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Hospital":
        TopicValue = "sendToPc/4024653174"
        CheckRange(Hospital.minValue,Hospital.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Hospital2":
        TopicValue = "sendToPc/3649459203"
        CheckRange(Hospital.minValue, Hospital.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Hospital3":
        TopicValue = "sendToPc/536179654"
        CheckRange(Hospital.minValue, Hospital.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Hospital4":
        TopicValue = "sendToPc/4026693430"
        CheckRange(Hospital.minValue, Hospital.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Terrace house 1":
        TopicValue = "sendToPc/695368886"
        CheckRange(TerraceHouse.minValue, TerraceHouse.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Terrace house 3":
        TopicValue = "sendToPc/3649886163"
        CheckRange(TerraceHouse.minValue, TerraceHouse.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Terrace house 2":
        TopicValue = "sendToPc/2052180480"
        CheckRange(TerraceHouse.minValue, TerraceHouse.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Detached house":
        TopicValue = "sendToPc/3649488643"
        CheckRange(DetachedHouse.minValue, DetachedHouse.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Detached house 2":
        TopicValue = "sendToPc/786497569"
        CheckRange(DetachedHouse.minValue, DetachedHouse.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Detached house 3":
        TopicValue = "sendToPc/525736038"
        CheckRange(DetachedHouse.minValue, DetachedHouse.maxValue, Power, TopicValue, inputValue)
    elif Selection == "Shopping Mall":
        TopicValue = "sendToPc/2310254414"
        CheckRange(ShoppingMall.minValue, ShoppingMall.maxValue, Power, TopicValue, inputValue)
    ValueBox.delete("1.0", "end-1c")


def ShowlVValues(event):
    Selection = LowVoltageList.get(LowVoltageList.curselection())
    if Selection == "Load":
        String = f"{Selection} Selected, set power: from {Load.minValue} to {Load.maxValue}"
        frame.text.set(String)
    elif Selection == "House":
        String = f"{Selection} Selected, set power: from {House.minValue} to {House.maxValue}"
        frame.text.set(String)
    elif Selection == "Appartment":
        String = f"{Selection} Selected, set power: from {Appartment.minValue} to {Appartment.maxValue}"
        frame.text.set(String)
    elif Selection == "Appartment2":
        String = f"{Selection} Selected, set power: from {Appartment.minValue} to {Appartment.maxValue}"
        frame.text.set(String)
    elif Selection == "Appartment3":
        String = f"{Selection} Selected, set power: from {Appartment.minValue} to {Appartment.maxValue}"
        frame.text.set(String)
    elif Selection == "Appartment4":
        String = f"{Selection} Selected, set power: from {Appartment.minValue} to {Appartment.maxValue}"
        frame.text.set(String)
    elif Selection == "Appartment5":
        String = f"{Selection} Selected, set power: from {Appartment.minValue} to {Appartment.maxValue}"
        frame.text.set(String)
    elif Selection == "Appartment6":
        String = f"{Selection} Selected, set power: from {Appartment.minValue} to {Appartment.maxValue}"
        frame.text.set(String)
    elif Selection == "Packhouse":
        String = f"{Selection} Selected, set power: from {Packhouse.minValue} to {Packhouse.maxValue}"
        frame.text.set(String)
    elif Selection == "Charging station":
        String = f"{Selection} Selected, set power: from {ChargingStation.minValue} to {ChargingStation.maxValue}"
        frame.text.set(String)
    elif Selection == "Car charging station":
        String = f"{Selection} Selected, set power: from {CarChargingStation.minValue} to {CarChargingStation.maxValue}"
        frame.text.set(String)
    elif Selection == "Car charging station 2":
        String = f"{Selection} Selected, set power: from {CarChargingStation.minValue} to {CarChargingStation.maxValue}"
        frame.text.set(String)
    elif Selection == "Packhouse2":
        String = f"{Selection} Selected, set power: from {Packhouse.minValue} to {Packhouse.maxValue}"
        frame.text.set(String)
    elif Selection == "Hospital":
        String = f"{Selection} Selected, set power: from {Hospital.minValue} to {Hospital.maxValue}"
        frame.text.set(String)
    elif Selection == "Hospital2":
        String = f"{Selection} Selected, set power: from {Hospital.minValue} to {Hospital.maxValue}"
        frame.text.set(String)
    elif Selection == "Hospital3":
        String = f"{Selection} Selected, set power: from {Hospital.minValue} to {Hospital.maxValue}"
        frame.text.set(String)
    elif Selection == "Hospital4":
        String = f"{Selection} Selected, set power: from {Hospital.minValue} to {Hospital.maxValue}"
        frame.text.set(String)
    elif Selection == "Terrace house 1":
        String = f"{Selection} Selected, set power: from {TerraceHouse.minValue} to {TerraceHouse.maxValue}"
        frame.text.set(String)
    elif Selection == "Terrace house 2":
        String = f"{Selection} Selected, set power: from {TerraceHouse.minValue} to {TerraceHouse.maxValue}"
        frame.text.set(String)
    elif Selection == "Terrace house 3":
        String = f"{Selection} Selected, set power: from {TerraceHouse.minValue} to {TerraceHouse.maxValue}"
        frame.text.set(String)
    elif Selection == "Detached house":
        String = f"{Selection} Selected, set power: from {DetachedHouse.minValue} to {DetachedHouse.maxValue}"
        frame.text.set(String)
    elif Selection == "Detached house 2":
        String = f"{Selection} Selected, set power: from {DetachedHouse.minValue} to {DetachedHouse.maxValue}"
        frame.text.set(String)
    elif Selection == "Detached house 3":
        String = f"{Selection} Selected, set power: from {DetachedHouse.minValue} to {DetachedHouse.maxValue}"
        frame.text.set(String)
    elif Selection == "Shopping Mall":
        String = f"{Selection} Selected, set power: from {ShoppingMall.minValue} to {ShoppingMall.maxValue}"
        frame.text.set(String)
    elif Selection == "Farm":
        String = f"{Selection} Selected, set power: from {Farm.minValue} to {Farm.maxValue}"
        frame.text.set(String)
def ShowMVValues(event):
    Selection = MediumVoltageList.get(MediumVoltageList.curselection())  ### takes the data from selected item on the listbox
    if Selection == "HAN":
        String = f"{Selection} Selected, set power: from {HAN.minValue} to {HAN.maxValue}"
        frame.text.set(String)
    elif Selection == "HAN2":
        String = f"{Selection} Selected, set power: from {HAN.minValue} to {HAN.maxValue}"
        frame.text.set(String)
    elif Selection == "HAN3":
        String = f"{Selection} Selected, set power: from {HAN.minValue} to {HAN.maxValue}"
        frame.text.set(String)
    elif Selection == "Factory":
        String = f"{Selection} Selected, set power: from {Factory.minValue} to {Factory.maxValue}"
        frame.text.set(String)
    elif Selection == "Factory 2":
        String = f"{Selection} Selected, set power: from {Factory.minValue} to {Factory.maxValue}"
        frame.text.set(String)
    elif Selection == "Fueling station":
        String = f"{Selection} Selected, set power: from {FuelingStation.minValue} to {FuelingStation.maxValue}"
        frame.text.set(String)
    elif Selection == "Processing factory":
        String = f"{Selection} Selected, set power: from {ProcessingFactory.minValue} to {ProcessingFactory.maxValue}"
        frame.text.set(String)
    elif Selection == "Chemical factory":
        String = f"{Selection} Selected, set power: from {ChemicalFactory.minValue} to {ChemicalFactory.maxValue}"
        frame.text.set(String)
    elif Selection == "Charging station":
        String = f"{Selection} Selected, set power: from {ChargingStation.minValue} to {ChargingStation.maxValue}"
        frame.text.set(String)
def ShowGENValues(event):
    Selection = HighVoltageList.get(
        HighVoltageList.curselection())  ### takes the data from selected item on the listbox
    if Selection == "Nuclear Generator -HV":
        String = f"{Selection} Selected, set power: from {NuclearGenerator.minValue} to {NuclearGenerator.maxValue}"
        frame.text.set(String)
    elif Selection == "Powerplant -HV":
        String = f"{Selection} Selected, set power: from {Powerplant.minValue} to {Powerplant.maxValue}"
        frame.text.set(String)
    elif Selection == "Coal Powerplant -HV":
        String = f"{Selection} Selected, set power: from {CoalPowerplant.minValue} to {CoalPowerplant.maxValue}"
        frame.text.set(String)
    elif Selection == "Nuclear Powerplant -HV":
        String = f"{Selection} Selected, set power: from {NuclearPowerplant.minValue} to {NuclearPowerplant.maxValue}"
        frame.text.set(String)
    elif Selection == "Wind Generator -MV":
        String = f"{Selection} Selected, set power: from {WindGenerator.minValue} to {WindGenerator.maxValue}"
        frame.text.set(String)
    elif Selection == "HydroStation -MV":
        String = f"{Selection} Selected, set power: from {Hydrostation.minValue} to {Hydrostation.maxValue}"
        frame.text.set(String)
    elif Selection == "Solar farm -MV":
        String = f"{Selection} Selected, set power: from {SolarFarm.minValue} to {SolarFarm.maxValue}"
        frame.text.set(String)
    elif Selection == "Solar farm 2 -MV":
        String = f"{Selection} Selected, set power: from {SolarFarm.minValue} to {SolarFarm.maxValue}"
        frame.text.set(String)
    elif Selection == "Wind Solar -MV":
        String = f"{Selection} Selected, set power: from {WindSolar.minValue} to {WindSolar.maxValue}"
        frame.text.set(String)
    elif Selection == "Storage1":
        String = f"{Selection} Selected, set power: from {Storage.minValue} to {Storage.maxValue}"
        frame.text.set(String)
    elif Selection == "Storage2":
        String = f"{Selection} Selected, set power: from {Storage.minValue} to {Storage.maxValue}"
        frame.text.set(String)
    elif Selection == "Storage3":
        String = f"{Selection} Selected, set power: from {Storage.minValue} to {Storage.maxValue}"
        frame.text.set(String)
    elif Selection == "Battery storage":
        String = f"{Selection} Selected, set power: from {Battery.minValue} to {Battery.maxValue}"
        frame.text.set(String)
    elif Selection == "Battery storage2":
        String = f"{Selection} Selected, set power: from {Battery.minValue} to {Battery.maxValue}"
        frame.text.set(String)
    elif Selection == "Neighbourhood Battery":
        String = f"{Selection} Selected, set power: from {Battery.minValue} to {Battery.maxValue}"
        frame.text.set(String)
    elif Selection == "Solar farm without motor":
        String = f"{Selection} Selected, set power: from {SolarFarm.minValue} to {SolarFarm.maxValue}"
        frame.text.set(String)
    elif Selection == "Solar farm small 1":
        String = f"{Selection} Selected, set power: from {SmallSolarFarm.minValue} to {SmallSolarFarm.maxValue}"
        frame.text.set(String)
    elif Selection == "Solar farm small 2":
        String = f"{Selection} Selected, set power: from {SmallSolarFarm.minValue} to {SmallSolarFarm.maxValue}"
        frame.text.set(String)
    elif Selection == "Solar farm without solar panels":
        String = f"{Selection} Selected, set power: from {SolarFarm.minValue} to {SolarFarm.maxValue}"
        frame.text.set(String)
    elif Selection == "Hydropower dam":
        String = f"{Selection} Selected, set power: from {HydropowerDam.minValue} to {HydropowerDam.maxValue}"
        frame.text.set(String)
    elif Selection == "Nuclear powerplant 2":
        String = f"{Selection} Selected, set power: from {NuclearPowerplant.minValue} to {NuclearPowerplant.maxValue}"
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
                    "Farm", "Appartment5", "Appartment6", "Car charging station", "Car charging station 2",
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
Errormsg= tk.messagebox
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
