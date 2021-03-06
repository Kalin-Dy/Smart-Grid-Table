from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget,QFrame, QLabel,QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QModelIndex
import paho.mqtt.client as paho
import json
import os
import sys

class Resolution:
    x=0
    y=0
    Scenariox = x / 4
    Scenarioy = y / 2
class MQTT():
    port=0
    broker="broker.hivemq.com"
    Topic ="none"
    Payload =" "
class SmartTableWindow(QMainWindow):

    def __init__(self):
        super(SmartTableWindow, self).__init__()
        self.Configfile()
        self.setGeometry(Resolution.x,Resolution.y,Resolution.x,Resolution.y)
        self.setWindowTitle("SmartTableGUI")
        self.initUI()

    def initUI(self):
        self.client1 = paho.Client()  # create client object
        self.client1.on_publish = on_publish  # assign function to callback
        self.client1.connect(MQTT.broker, MQTT.port)
        self.ConfigButton=QtWidgets.QPushButton(self)
        self.SendConfig=QtWidgets.QPushButton(self)
        self.ConfigBroker=QtWidgets.QLineEdit(self)
        self.ConfigPort = QtWidgets.QLineEdit(self)
        self.ConfigResolutionX = QtWidgets.QLineEdit(self)
        self.ConfigResolutionY = QtWidgets.QLineEdit(self)
        self.AdminLabel=QtWidgets.QLabel(self)
        self.AddbuildingNameLabel=QtWidgets.QLabel(self)
        self.AddbuildingVoltageLabel = QtWidgets.QLabel(self)
        self.AddbuildingTypeLabel = QtWidgets.QLabel(self)
        self.AddbuildingMaximumPowerLabel = QtWidgets.QLabel(self)
        self.AddbuildingMinimumPowerLabel = QtWidgets.QLabel(self)
        self.AddbuildingSetPowerLabel = QtWidgets.QLabel(self)
        self.AddBuildingRFIDLabel=QtWidgets.QLabel(self)
        self.AddBuildingNameTextBox=QtWidgets.QLineEdit(self)
        self.AddBuildingVoltageTextBox = QtWidgets.QLineEdit(self)
        self.AddBuildingTypeTextBox = QtWidgets.QLineEdit(self)
        self.AddBuildingMinimumPowerTextBox = QtWidgets.QLineEdit(self)
        self.AddBuildingSetPowerTextBox = QtWidgets.QLineEdit(self)
        self.AddBuildingMaximumPowerTextBox = QtWidgets.QLineEdit(self)
        self.AddBuildingRFIDTextBox = QtWidgets.QLineEdit(self)
        self.AdminRestartButton= QtWidgets.QPushButton(self)
        self.PasswordButton=QtWidgets.QPushButton(self)
        self.Password=QtWidgets.QLineEdit(self)
        self.BackFromVoltages=QtWidgets.QPushButton(self)
        self.AddBuildingButton=QtWidgets.QPushButton(self)
        self.AdminButton=QtWidgets.QPushButton(self)
        self.VoltagePictureButton=QtWidgets.QPushButton(self)
        self.SubmitPayloadButton=QtWidgets.QPushButton(self)
        self.BackFromBuildingSelection=QtWidgets.QPushButton(self)
        self.ExitButton=QtWidgets.QPushButton(self)
        self.PowerText=QLabel(self)
        self.PowerLabel=QtWidgets.QTextEdit(self)
        self.DebugButton =QtWidgets.QPushButton(self)
        self.PowerSlider = QtWidgets.QSlider(self)
        self.MVlist= QtWidgets.QComboBox(self)
        self.HVscrollArea = QtWidgets.QWidget(self)
        self.HVlist = QtWidgets.QComboBox(self)
        self.LVscrollArea = QtWidgets.QWidget(self)
        self.LVlist = QtWidgets.QComboBox(self)
        self.LowVoltageButton = QtWidgets.QPushButton(self)
        self.MediumVoltageButton = QtWidgets.QPushButton(self)
        self.HighVoltageButton = QtWidgets.QPushButton(self)
        self.BackToTutorial=QtWidgets.QPushButton(self)
        self.BackFromScenario =QtWidgets.QPushButton(self)
        self.ScenarioSunny = QtWidgets.QPushButton(self)
        self.ScenarioDay = QtWidgets.QPushButton(self)
        self.ScenarioNight = QtWidgets.QPushButton(self)
        self.ScenarioEV = QtWidgets.QPushButton(self)
        self.ScenarioWindy = QtWidgets.QPushButton(self)
        self.ScenarioHeatPumps = QtWidgets.QPushButton(self)
        self.ScenarioSummer = QtWidgets.QPushButton(self)
        self.ScenarioWinter = QtWidgets.QPushButton(self)
        self.IndividualAdjustmentsButton= QtWidgets.QPushButton(self)
        self.ScenariosButton = QtWidgets.QPushButton(self)
        self.TutorialButton  = QtWidgets.QPushButton(self)
        self.TutorialButton2 = QtWidgets.QPushButton(self)
        self.TutorialButton3 = QtWidgets.QPushButton(self)
        self.TutorialButton4 = QtWidgets.QPushButton(self)
        self.TutorialButton5 = QtWidgets.QPushButton(self)
        self.Listsinitialization()
        self.HideInitObjects()
        self.Page0()
    def HideInitObjects(self):
        self.ConfigButton.hide()
        self.SendConfig.hide()
        self.ConfigPort.hide()
        self.ConfigBroker.hide()
        self.ConfigResolutionX.hide()
        self.ConfigResolutionY.hide()
        self.AdminLabel.hide()
        self.AddbuildingNameLabel.hide()
        self.AddbuildingVoltageLabel.hide()
        self.AddbuildingTypeLabel.hide()
        self.AddbuildingMaximumPowerLabel.hide()
        self.AddbuildingMinimumPowerLabel.hide()
        self.AddbuildingSetPowerLabel.hide()
        self.AddBuildingRFIDLabel.hide()
        self.AddBuildingNameTextBox.hide()
        self.AddBuildingVoltageTextBox.hide()
        self.AddBuildingTypeTextBox.hide()
        self.AddBuildingMinimumPowerTextBox.hide()
        self.AddBuildingSetPowerTextBox.hide()
        self.AddBuildingMaximumPowerTextBox.hide()
        self.AddBuildingRFIDTextBox.hide()
        self.AdminRestartButton.hide()
        self.PasswordButton.hide()
        self.Password.hide()
        self.BackFromVoltages.hide()
        self.AddBuildingButton.hide()
        self.AdminButton.hide()
        self.VoltagePictureButton.hide()
        self.SubmitPayloadButton.hide()
        self.HVlist.hide()
        self.MVlist.hide()
        self.BackFromBuildingSelection.hide()
        self.ExitButton.show()
        self.PowerText.hide()
        self.PowerLabel.hide()
        self.DebugButton.hide()
        self.PowerSlider.hide()
        self.LVlist.hide()
        self.LowVoltageButton.hide()
        self.MediumVoltageButton.hide()
        self.HighVoltageButton.hide()
        self.BackToTutorial.hide()
        self.BackFromScenario.hide()
        self.TutorialButton4.hide()
        self.TutorialButton2.hide()
        self.TutorialButton3.hide()
        self.TutorialButton5.hide()
        self.ScenariosButton.hide()
        self.ScenarioEV.hide()
        self.ScenarioDay.hide()
        self.ScenarioNight.hide()
        self.ScenarioSummer.hide()
        self.ScenarioWinter.hide()
        self.ScenarioHeatPumps.hide()
        self.ScenarioWindy.hide()
        self.ScenarioSunny.hide()
        self.IndividualAdjustmentsButton.hide()
    def HideAdminPage(self):
        self.ConfigButton.hide()
        self.AddBuildingButton.hide()
        self.Password.hide()
        self.PasswordButton.hide()
        self.AdminLabel.hide()
        self.AddbuildingNameLabel.hide()
        self.AddbuildingVoltageLabel.hide()
        self.AddbuildingTypeLabel.hide()
        self.AddbuildingMaximumPowerLabel.hide()
        self.AddbuildingMinimumPowerLabel.hide()
        self.AddbuildingSetPowerLabel.hide()
        self.AddBuildingRFIDLabel.hide()
        self.AddBuildingNameTextBox.hide()
        self.AddBuildingVoltageTextBox.hide()
        self.AddBuildingTypeTextBox.hide()
        self.AddBuildingMinimumPowerTextBox.hide()
        self.AddBuildingSetPowerTextBox.hide()
        self.AddBuildingMaximumPowerTextBox.hide()
        self.AddBuildingRFIDTextBox.hide()
        self.AdminRestartButton.hide()
        self.PasswordButton.hide()
        self.Password.hide()
    def Page0(self):
        self.TutorialButton.setFixedSize(Resolution.x,Resolution.y)
        self.TutorialButton.setIcon(QtGui.QIcon("Wlkmscrin.jpeg"))
        self.TutorialButton.setIconSize(QtCore.QSize(884, 792))
        self.TutorialButton.clicked.connect(self.TPage1)
    def TPage1(self):
        self.TutorialButton.hide()
        self.TutorialButton2.show()
        self.TutorialButton2.setFixedSize(Resolution.x,Resolution.y)
        self.TutorialButton2.setIcon(QtGui.QIcon("Firstpage.jpg"))
        self.TutorialButton2.setIconSize(QtCore.QSize(884, 792))
        self.TutorialButton2.clicked.connect(self.TPage2)
    def TPage2(self):
        self.TutorialButton2.hide()
        self.TutorialButton3.show()
        self.TutorialButton3.setFixedSize(Resolution.x,Resolution.y)
        self.TutorialButton3.setIcon(QtGui.QIcon("Secondpage.jpg"))
        self.TutorialButton3.setIconSize(QtCore.QSize(884, 792))
        self.TutorialButton3.clicked.connect(self.TPage3)
    def TPage3(self):
        self.TutorialButton3.hide()
        self.TutorialButton4.show()
        self.TutorialButton4.setFixedSize(Resolution.x,Resolution.y)
        self.TutorialButton4.setIcon(QtGui.QIcon("Thirdpage.jpg"))
        self.TutorialButton4.setIconSize(QtCore.QSize(884, 792))
        self.TutorialButton4.clicked.connect(self.TPage4)
    def TPage4(self):
        self.TutorialButton4.hide()
        self.TutorialButton5.show()
        self.TutorialButton5.setFixedSize(Resolution.x,Resolution.y)
        self.TutorialButton5.setIcon(QtGui.QIcon("Fourthpage.jpg"))
        self.TutorialButton5.setIconSize(QtCore.QSize(884, 792))
        self.TutorialButton5.clicked.connect(self.MainPage)
    def MainPage(self):
        self.ExitButton.setGeometry(Resolution.x-Resolution.x/24,0,Resolution.x/24,Resolution.y/24)
        self.ExitButton.show()
        self.ExitButton.setText("X")
        self.ExitButton.setStyleSheet("background-color: red")
        self.ExitButton.clicked.connect(exit)
        self.HideScenarios()
        self.VoltagePageHide()
        self.TutorialButton5.hide()
        self.ScenariosButton.setText("Scenarios")
        self.ScenariosButton.setGeometry(0,Resolution.y/3,Resolution.x,Resolution.y/3)
        self.ScenariosButton.clicked.connect(self.ShowScenarios)
        self.IndividualAdjustmentsButton.setText("Individual Adjustments")
        self.IndividualAdjustmentsButton.setGeometry(0,2*(Resolution.y/3),Resolution.x,(Resolution.y/3))
        self.IndividualAdjustmentsButton.clicked.connect(self.ShowVoltage)
        self.BackToTutorial.setText("Tutorial")
        self.BackToTutorial.setGeometry(0,Resolution.y/24,Resolution.x,Resolution.y/3)
        self.BackToTutorial.clicked.connect(self.TPage1)
        self.ScenariosButton.show()
        self.IndividualAdjustmentsButton.show()
        self.BackToTutorial.show()
    def ShowScenarios(self):
        self.AddBuilding()
        self.IndividualAdjustmentsButton.hide()
        self.ScenariosButton.hide()
        self.ScenarioSunny.show()
        self.ScenarioSunny.setIcon(QtGui.QIcon("Sunny.jpg"))
        self.ScenarioSunny.setIconSize(QtCore.QSize(Resolution.Scenariox,Resolution.Scenarioy))
        self.ScenarioSunny.clicked.connect(self.SunnyScenario)
        self.ScenarioSunny.setFixedSize(Resolution.Scenariox,Resolution.Scenarioy)
        self.ScenarioSunny.setGeometry(0,Resolution.y/24,Resolution.Scenariox,Resolution.Scenarioy)
        self.ScenarioWindy.show()
        self.ScenarioWindy.setIcon(QtGui.QIcon("Windy.jpg"))
        self.ScenarioWindy.setIconSize(QtCore.QSize(Resolution.Scenariox,Resolution.Scenarioy))
        self.ScenarioWindy.clicked.connect(self.WindyScenario)
        self.ScenarioWindy.setFixedSize(Resolution.Scenariox,Resolution.Scenarioy)
        self.ScenarioWindy.setGeometry(0, Resolution.Scenarioy+Resolution.y/24,Resolution.Scenariox,Resolution.Scenarioy)
        self.ScenarioNight.show()
        self.ScenarioNight.setIcon(QtGui.QIcon("Night.jpg"))
        self.ScenarioNight.setIconSize(QtCore.QSize(Resolution.Scenariox,Resolution.Scenarioy))
        self.ScenarioNight.clicked.connect(self.NightScenario)
        self.ScenarioNight.setFixedSize(Resolution.Scenariox,Resolution.Scenarioy)
        self.ScenarioNight.setGeometry(Resolution.Scenariox+1,Resolution.y/24, Resolution.Scenariox,Resolution.Scenarioy)
        self.ScenarioDay.show()
        self.ScenarioDay.setIcon(QtGui.QIcon("Day.jpg"))
        self.ScenarioDay.setIconSize(QtCore.QSize(Resolution.Scenariox, Resolution.Scenarioy))
        self.ScenarioDay.clicked.connect(self.DayScenario)
        self.ScenarioDay.setFixedSize(Resolution.Scenariox, Resolution.Scenarioy)
        self.ScenarioDay.setGeometry(Resolution.Scenariox + 1,Resolution.Scenarioy+Resolution.y/24, Resolution.Scenariox, Resolution.Scenarioy)
        self.ScenarioEV.setIcon(QtGui.QIcon("EV.jpg"))
        self.ScenarioEV.setIconSize(QtCore.QSize(Resolution.Scenariox, Resolution.Scenarioy))
        self.ScenarioEV.clicked.connect(self.EVScenario)
        self.ScenarioEV.setFixedSize(Resolution.Scenariox, Resolution.Scenarioy)
        self.ScenarioEV.setGeometry(2*Resolution.Scenariox + 1,Resolution.y/24, Resolution.Scenariox,Resolution.Scenarioy)
        self.ScenarioEV.show()
        self.ScenarioHeatPumps.setIcon(QtGui.QIcon("HeatPumps.jpg"))
        self.ScenarioHeatPumps.setIconSize(QtCore.QSize(Resolution.Scenariox, Resolution.Scenarioy))
        self.ScenarioHeatPumps.clicked.connect(self.HeatPumpsScenario)
        self.ScenarioHeatPumps.setFixedSize(Resolution.Scenariox, Resolution.Scenarioy)
        self.ScenarioHeatPumps.setGeometry(2 * Resolution.Scenariox + 1, Resolution.Scenarioy + Resolution.y/24, Resolution.Scenariox,Resolution.Scenarioy)
        self.ScenarioHeatPumps.show()
        self.ScenarioSummer.setIcon(QtGui.QIcon("Summer.jpg"))
        self.ScenarioSummer.setIconSize(QtCore.QSize(Resolution.Scenariox, Resolution.Scenarioy))
        self.ScenarioSummer.clicked.connect(self.SummerScenario)
        self.ScenarioSummer.setFixedSize(Resolution.Scenariox, Resolution.Scenarioy)
        self.ScenarioSummer.setGeometry(3 * Resolution.Scenariox + 1, Resolution.Scenarioy + Resolution.y/24, Resolution.Scenariox,Resolution.Scenarioy)
        self.ScenarioSummer.show()
        self.ScenarioWinter.setIcon(QtGui.QIcon("Winter.jpg"))
        self.ScenarioWinter.setIconSize(QtCore.QSize(Resolution.Scenariox, Resolution.Scenarioy))
        self.ScenarioWinter.clicked.connect(self.WinterScenario)
        self.ScenarioWinter.setFixedSize(Resolution.Scenariox, Resolution.Scenarioy)
        self.ScenarioWinter.setGeometry(3 * Resolution.Scenariox + 1, Resolution.y/24, Resolution.Scenariox,Resolution.Scenarioy)
        self.ScenarioWinter.show()
        self.BackFromScenario.setText("Back to Main page")
        self.BackFromScenario.clicked.connect(self.MainPage)
        self.BackFromScenario.setGeometry(0,0,Resolution.x-Resolution.x/24,Resolution.y/24)
        self.BackFromScenario.show()
    def VoltagePageHide(self):
        self.LowVoltageButton.hide()
        self.AdminButton.hide()
        self.MediumVoltageButton.hide()
        self.HighVoltageButton.hide()
        self.BackFromVoltages.hide()
        self.PowerSlider.hide()
    def HideScenarios(self):
        self.ScenarioEV.hide()
        self.ScenarioDay.hide()
        self.ScenarioNight.hide()
        self.ScenarioSummer.hide()
        self.ScenarioWinter.hide()
        self.ScenarioHeatPumps.hide()
        self.ScenarioWindy.hide()
        self.ScenarioSunny.hide()
        self.BackFromScenario.hide()
    def HideMainPage(self):
        self.ScenariosButton.hide()
        self.IndividualAdjustmentsButton.hide()
        self.BackToTutorial.hide()
    def HideVoltagePage(self):
        self.LowVoltageButton.hide()
        self.MediumVoltageButton.hide()
        self.HighVoltageButton.hide()
        self.BackFromVoltages.hide()
        self.AdminButton.hide()
    def HideBuildingPages(self):
        self.LVlist.hide()
        self.HVlist.hide()
        self.MVlist.hide()
        self.PowerText.hide()
        self.PowerLabel.hide()
        self.PowerText.hide()
        self.SubmitPayloadButton.hide()
        self.VoltagePictureButton.hide()

    def ShowVoltage(self):
        self.BackFromBuildingSelection.hide()
        self.HideAdminPage()
        self.HideBuildingPages()
        self.HideMainPage()
        self.VoltagePictureButton.setGeometry(Resolution.x / 2, Resolution.y / 16, 445, 459)
        self.VoltagePictureButton.setIconSize(QtCore.QSize(445, 459))
        self.VoltagePictureButton.setFixedSize(445, 459)
        self.PowerLabel.setGeometry(Resolution.x / 24, Resolution.y / 3, Resolution.x / 8, Resolution.y / 8)
        self.PowerSlider.setGeometry(Resolution.x /4, Resolution.y/12, Resolution.x / 4, Resolution.y / 2)
        self.PowerSlider.valueChanged.connect(self.Slider)
        self.PowerSlider.setOrientation(QtCore.Qt.Vertical)
        self.PowerText.setText("Power in kW")
        self.PowerLabel.setReadOnly(True)
        self.PowerText.setGeometry(Resolution.x /24, Resolution.y/4, Resolution.x / 8,Resolution.y / 8)
        self.BackFromBuildingSelection.setGeometry(Resolution.x-(Resolution.x/7),Resolution.y/24,Resolution.x/7,Resolution.y/7)
        self.BackFromBuildingSelection.setText("Voltage Selection")
        self.BackFromBuildingSelection.clicked.connect(self.ShowVoltage)
        self.LowVoltageButton.setText("Low Voltage Buildings")
        self.LowVoltageButton.clicked.connect(self.LowVoltagePage)
        self.LowVoltageButton.setGeometry(Resolution.x/3, 0, Resolution.x/3, Resolution.y/3)
        self.AdminButton.setGeometry(2*(Resolution.x/3),Resolution.y/3,Resolution.x/3,Resolution.y/3)
        self.AdminButton.setText("Admin Mode")
        self.AdminButton.show()
        self.AdminButton.clicked.connect(self.AdminPageLocked)
        self.BackFromVoltages.setGeometry(0,Resolution.y/3,Resolution.x/3,Resolution.y/3)
        self.BackFromVoltages.setText("Back to Menu")
        self.BackFromVoltages.show()
        self.BackFromVoltages.clicked.connect(self.MainPage)
        self.MediumVoltageButton.setText("Medium Voltage Buildings")
        self.MediumVoltageButton.clicked.connect(self.MediumVoltagePage)
        self.MediumVoltageButton.setGeometry(Resolution.x / 3, Resolution.y/3, Resolution.x / 3, Resolution.y / 3)
        self.HighVoltageButton.setText("High Voltage Buildings")
        self.HighVoltageButton.clicked.connect(self.HighVoltagePage)
        self.HighVoltageButton.setGeometry(Resolution.x / 3, 2*(Resolution.y / 3), Resolution.x / 3, Resolution.y / 3)
        self.LowVoltageButton.show()
        self.MediumVoltageButton.show()
        self.HighVoltageButton.show()
        self.SubmitPayloadButton.clicked.connect(self.TPage1)
        MQTT.Topic = "Error"
    def LowVoltagePage(self):
        self.HideVoltagePage()
        self.BackFromBuildingSelection.show()
        self.PowerText.show()
        self.PowerLabel.show()
        self.PowerSlider.show()
        self.SubmitPayloadButton.setGeometry(Resolution.x / 24, Resolution.y / 2, Resolution.x / 4, Resolution.y / 4)
        self.SubmitPayloadButton.setText("Send Power")
        self.SubmitPayloadButton.show()
        self.SubmitPayloadButton.clicked.disconnect()
        self.SubmitPayloadButton.clicked.connect(lambda :self.PublishMQTT(MQTT.Topic, ('p_set' +' '+MQTT.Payload)))
        self.LVlist.setGeometry(Resolution.x / 24, Resolution.y / 24, Resolution.x / 4, Resolution.y / 4)
        self.VoltagePictureButton.show()
        self.LVlist.show()
        self.LVlist.activateWindow()
        self.LVlist.activated[str].connect(self.LVlistselecteditem)
    def AdminPageLocked(self):
        self.VoltagePageHide()
        self.AdminButton.hide()
        self.PasswordButton.setGeometry(Resolution.x/3,Resolution.y/3+Resolution.y/24,Resolution.x/3,Resolution.y/6)
        self.Password.setGeometry(Resolution.x/3,Resolution.y/3,Resolution.x/3,Resolution.y/24)
        self.Password.show()
        self.PasswordButton.setText("Submit Password")
        self.PasswordButton.show()
        self.PasswordButton.clicked.connect(self.Unlock)
    def Unlock(self):
        Password=self.Password.text()
        if Password =="SmartTable":
            self.AdminPageUnlocked()
        else:
            self.Password.setText("Wrong Password")
    def AdminPageUnlocked(self):
        self.PasswordButton.hide()
        self.AdminLabel.setGeometry(Resolution.x/2.7,0,Resolution.x/3,Resolution.y/6)
        self.AddBuildingRFIDLabel.setGeometry(Resolution.x/4,Resolution.y/16,Resolution.x/6,Resolution.y/6)
        self.AddbuildingNameLabel.setGeometry(Resolution.x/1.65,Resolution.y/16,Resolution.x/6,Resolution.y/6)
        self.AddBuildingNameTextBox.setGeometry(Resolution.x/1.8,Resolution.y/16+Resolution.y/10,Resolution.x/6,Resolution.y/12)
        self.AddBuildingRFIDTextBox.setGeometry(Resolution.x/5.2,Resolution.y/16+Resolution.y/10,Resolution.x/6,Resolution.y/12)
        self.AddbuildingVoltageLabel.setGeometry(Resolution.x/5.8,Resolution.y/3.8,Resolution.x/6,Resolution.y/6)
        self.AddBuildingVoltageTextBox.setGeometry(Resolution.x/6,Resolution.y/3.8+Resolution.y/10,Resolution.x/12,Resolution.y/12)
        self.AddbuildingTypeLabel.setGeometry(Resolution.x/3.3,Resolution.y/3.8,Resolution.x/6,Resolution.y/6)
        self.AddBuildingTypeTextBox.setGeometry(Resolution.x/3.5,Resolution.y/3.8+Resolution.y/10,Resolution.x/12,Resolution.y/12)
        self.AddbuildingMinimumPowerLabel.setGeometry(Resolution.x/2.45,Resolution.y/3.8,Resolution.x/6,Resolution.y/6)
        self.AddBuildingMinimumPowerTextBox.setGeometry(Resolution.x/2.45,Resolution.y/3.8+Resolution.y/10,Resolution.x/12,Resolution.y/12)
        self.AddbuildingSetPowerLabel.setGeometry(Resolution.x/1.85,Resolution.y/3.8,Resolution.x/6,Resolution.y/6)
        self.AddBuildingSetPowerTextBox.setGeometry(Resolution.x/1.85,Resolution.y/3.8+Resolution.y/10,Resolution.x/12,Resolution.y/12)
        self.AddbuildingMaximumPowerLabel.setGeometry(Resolution.x/1.5,Resolution.y/3.8,Resolution.x/6,Resolution.y/6)
        self.AddBuildingMaximumPowerTextBox.setGeometry(Resolution.x/1.5,Resolution.y/3.8+Resolution.y/10,Resolution.x/12,Resolution.y/12)
        self.AddBuildingButton.setGeometry(Resolution.x/5.2,Resolution.y/2+Resolution.y/10,Resolution.x/6,Resolution.y/6)
        self.AdminRestartButton.setGeometry(Resolution.x/1.8,Resolution.y/2+Resolution.y/10,Resolution.x/6,Resolution.y/6)
        self.ConfigButton.setGeometry(Resolution.x/1.4,Resolution.y/2+Resolution.y/10,Resolution.x/6,Resolution.y/6)
        self.ConfigButton.show()
        self.ConfigButton.clicked.connect(self.OptionsPage)
        self.ConfigButton.setText("Options")
        self.AddBuildingButton.show()
        self.AddBuildingButton.clicked.connect(self.AddBuilding)
        self.AdminRestartButton.setText("Restart App")
        self.AdminRestartButton.clicked.connect(self.ShowVoltage) #somtin aint right here
        self.AddBuildingButton.setText("Add Building")
        self.AdminRestartButton.show()
        self.AddBuildingSetPowerTextBox.show()
        self.AddBuildingMinimumPowerTextBox.show()
        self.AddBuildingNameTextBox.show()
        self.AddBuildingRFIDTextBox.show()
        self.AddBuildingMaximumPowerTextBox.show()
        self.AddBuildingVoltageTextBox.show()
        self.AddbuildingSetPowerLabel.setText("Set Power")
        self.AddbuildingSetPowerLabel.show()
        self.AddbuildingMinimumPowerLabel.setText("Min Power")
        self.AddbuildingTypeLabel.setText("Type")
        self.AddBuildingRFIDLabel.setText("RFID")
        self.AddbuildingNameLabel.setText("Name")
        self.AddbuildingMaximumPowerLabel.setText("Max Power")
        self.AddbuildingMaximumPowerLabel.show()
        self.AddbuildingVoltageLabel.setText("Voltage")
        self.AddbuildingMinimumPowerLabel.show()
        self.AddbuildingNameLabel.show()
        self.AddbuildingVoltageLabel.show()
        self.AddbuildingTypeLabel.show()
        self.AddBuildingTypeTextBox.show()
        self.AdminLabel.setText("Welcome to Admin Mode")
        self.AdminLabel.show()
        self.AddBuildingRFIDLabel.show()
        self.Password.hide()
    def OptionsPage(self):
        self.HideAdminPage()
        self.ConfigResolutionX.setGeometry(Resolution.x/5.2,Resolution.y/16+Resolution.y/10,Resolution.x/6,Resolution.y/12)
        self.ConfigBroker.setGeometry(Resolution.x/1.8,Resolution.y/16+Resolution.y/10,Resolution.x/6,Resolution.y/12)
        self.ConfigResolutionY.setGeometry(Resolution.x/5.2,Resolution.y/8+Resolution.y/10,Resolution.x/6,Resolution.y/12)
        self.ConfigPort.setGeometry(Resolution.x/1.8,Resolution.y/8+Resolution.y/10,Resolution.x/6,Resolution.y/12)
        self.SendConfig.setGeometry(Resolution.x/2.8,Resolution.y/2+Resolution.y/10,Resolution.x/6,Resolution.y/6)
        self.ConfigResolutionX.setText(str(Resolution.x))
        self.ConfigResolutionY.setText(str(Resolution.y))
        self.ConfigPort.setText(str(MQTT.port))
        self.ConfigBroker.setText(MQTT.broker)
        self.SendConfig.clicked.connect(self.WriteConfigfile)
        self.ConfigBroker.show()
        self.ConfigPort.show()
        self.SendConfig.show()
        self.SendConfig.setText("Change")
        self.ConfigResolutionX.show()
        self.ConfigResolutionY.show()

    def MediumVoltagePage(self):
        self.HideVoltagePage()
        self.BackFromBuildingSelection.show()
        self.PowerText.show()
        self.PowerLabel.show()
        self.PowerSlider.show()
        self.SubmitPayloadButton.setGeometry(Resolution.x / 24, Resolution.y / 2, Resolution.x / 4, Resolution.y / 4)
        self.SubmitPayloadButton.clicked.disconnect()
        self.SubmitPayloadButton.clicked.connect(lambda: self.PublishMQTT(MQTT.Topic, ('p_set' + ' ' + MQTT.Payload)))
        self.SubmitPayloadButton.setText("Send Power")
        self.SubmitPayloadButton.show()

        self.MVlist.setGeometry(Resolution.x / 24, Resolution.y / 24, Resolution.x / 4, Resolution.y / 4)
        self.MVlist.show()
        self.MVlist.activateWindow()
        self.MVlist.activated[str].connect(self.MVlistselecteditem)

    def HighVoltagePage(self):
        self.HideVoltagePage()
        self.BackFromBuildingSelection.show()
        self.PowerText.show()
        self.PowerLabel.show()
        self.PowerSlider.show()
        self.SubmitPayloadButton.setGeometry(Resolution.x / 24, Resolution.y / 2, Resolution.x / 4, Resolution.y / 4)
        self.SubmitPayloadButton.setText("Send Power")
        self.SubmitPayloadButton.show()
        self.SubmitPayloadButton.clicked.disconnect()
        self.SubmitPayloadButton.clicked.connect(lambda: self.PublishMQTT(MQTT.Topic, ('p_nom' + ' ' + MQTT.Payload)))
        self.HVlist.setGeometry(Resolution.x / 24, Resolution.y / 24, Resolution.x / 4, Resolution.y / 4)
        self.HVlist.show()
        self.HVlist.activateWindow()
        self.HVlist.activated[str].connect(self.HVlistselecteditem)

    def LVlistselecteditem(self,text):

        LVrfid_list = self.LV_dict.keys()
        for x in LVrfid_list:
            module= self.LV_dict.get(x)
            if module.get("name")== text:
                min=module.get("p_min")
                max=module.get("p_max")
                Picture=module.get("name")+".jpg"
                print(Picture)
                MQTT.Topic="sendToPc/"+x
                self.PowerSlider.setMinimum(int(min))
                self.PowerSlider.setMaximum(int(max))
                self.VoltagePictureButton.setIcon(QtGui.QIcon(Picture))
                self.VoltagePictureButton.show()
    def MVlistselecteditem(self,text):
        MVrfid_list = self.MV_dict.keys()
        for x in MVrfid_list:
            module = self.MV_dict.get(x)
            if module.get("name") == text:
                min = module.get("p_min")
                max = module.get("p_max")
                MQTT.Topic = "sendToPc/" + x
                Picture = module.get("name") + ".jpg"
                self.PowerSlider.setMinimum(int(min))
                self.PowerSlider.setMaximum(int(max))
                self.VoltagePictureButton.setIcon(QtGui.QIcon(Picture))
                self.VoltagePictureButton.show()
    def HVlistselecteditem(self,text):
        HVrfid_list = self.HV_dict.keys()
        for x in HVrfid_list:
            module = self.HV_dict.get(x)
            if module.get("name") == text:
                min = module.get("p_min")
                max = module.get("p_max")
                MQTT.Topic = "sendToPc/" + x
                Picture = module.get("name") + ".jpg"
                self.PowerSlider.setMinimum(int(min))
                self.PowerSlider.setMaximum(int(max))
                self.VoltagePictureButton.setIcon(QtGui.QIcon(Picture))
                self.VoltagePictureButton.show()
    def Slider(self):
        value= self.PowerSlider.value()
        strval=str(value)
        MQTT.Payload = strval
        self.PowerLabel.setText(strval)
    def AddBuilding(self):
        Password = self.Password.text()
        if Password == "SmartTable":
            self.AdminPageUnlocked()
        else:
            self.Password.setText("Wrong Password")
        NewBuilding=('name','voltage','p_set','type','p_min','p_max')
        name=self.AddBuildingNameTextBox.text()
        RFID=self.AddBuildingRFIDTextBox.text()
        voltage=self.AddBuildingVoltageTextBox.text()
        p_set=self.AddBuildingSetPowerTextBox.text()
        type=self.AddBuildingTypeTextBox.text()
        p_min=self.AddBuildingMinimumPowerTextBox.text()
        p_max=self.AddBuildingMaximumPowerTextBox.text()
        Thisdict=dict.fromkeys(NewBuilding)
        Thisdict["name"]=name
        Thisdict["voltage"]=voltage
        Thisdict["p_set"]=p_set
        Thisdict["type"]=type
        Thisdict["p_min"]=p_min
        Thisdict["p_max"]=p_max

        self.data_dict.update({RFID:Thisdict})
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(dir_path, "data_file.json")
        with open(file_path, 'w') as out_file:
            json.dump(self.data_dict, out_file)
        self.Listsinitialization()
    def PublishMQTT(self,TopicValue, PayloadValue):
        self.client1.publish(TopicValue, PayloadValue)
    def SunnyScenario(self):
        MQTT.Topic="sendToPc/Scenario/sunny"
        MQTT.Payload='Sunny'
        self.PublishMQTT(MQTT.Topic,MQTT.Payload)
    def WindyScenario(self):
        MQTT.Topic="sendToPc/Scenario/windy"
        MQTT.Payload='Windy'
        self.PublishMQTT(MQTT.Topic,MQTT.Payload)
    def DayScenario(self):
        MQTT.Topic="sendToPc/Scenario/day"
        MQTT.Payload='Day'
        self.PublishMQTT(MQTT.Topic,MQTT.Payload)
    def NightScenario(self):
        MQTT.Topic="sendToPc/Scenario/night"
        MQTT.Payload='Night'
        self.PublishMQTT(MQTT.Topic,MQTT.Payload)
    def EVScenario(self):
        MQTT.Topic="sendToPc/Scenario/ev"
        MQTT.Payload='EV'
        self.PublishMQTT(MQTT.Topic,MQTT.Payload)
    def HeatPumpsScenario(self):
        MQTT.Topic="sendToPc/Scenario/heatpumps"
        MQTT.Payload='HeatPumps'
        self.PublishMQTT(MQTT.Topic,MQTT.Payload)
    def WinterScenario(self):
        MQTT.Topic="sendToPc/Scenario/winter"
        MQTT.Payload='Winter'
        self.PublishMQTT(MQTT.Topic,MQTT.Payload)
    def SummerScenario(self):
        MQTT.Topic="sendToPc/Scenario/summer"
        MQTT.Payload='Summer'
        self.PublishMQTT(MQTT.Topic,MQTT.Payload)
    def Listsinitialization(self):
        self.LVlist.clear()
        self.MVlist.clear()
        self.HVlist.clear()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(dir_path, "data_file.json")

        with open(file_path) as data_file:
            self.data_dict = json.load(data_file)
            rfid_list=self.data_dict.keys()
            i=0
        self.LV_dict = dict.fromkeys(rfid_list)
        self.MV_dict = dict.fromkeys(rfid_list)
        self.HV_dict = dict.fromkeys(rfid_list)
        for x in rfid_list:
            module= self.data_dict.get(x)

            if module.get("voltage")== "LV":
                self.LV_dict[x]=module
                item=module.get("name")
                self.LVlist.insertItem(i, item)
            elif module.get("voltage")== "MV":
                self.MV_dict[x] = module
                item = module.get("name")
                self.MVlist.insertItem(i, item)
            elif module.get("voltage") == "HV":
                self.HV_dict[x] = module
                item = module.get("name")
                self.HVlist.insertItem(i, item)
                i=i+1
        for x in rfid_list:
            if self.LV_dict[x] == None:
                self.LV_dict.pop(x)
            if self.MV_dict[x] == None:
                self.MV_dict.pop(x)
            if self.HV_dict[x] == None:
                self.HV_dict.pop(x)
    def Configfile(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(dir_path, "config.txt")

        with open("config.txt") as config_file:
            self.read_data=[line.rstrip() for line in config_file]
            Resolution.x=int(self.read_data[1])
            Resolution.y=int(self.read_data[2])
            Resolution.Scenariox = Resolution.x / 4
            Resolution.Scenarioy = Resolution.y / 2
            MQTT.broker=(self.read_data[4])
            MQTT.port=int((self.read_data[5]))
    def WriteConfigfile(self):
        print("Data written")
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(dir_path, "config.txt")
        write_data=[]
        write_data.insert(0,"Resolution\n")
        write_data.insert(1,self.ConfigResolutionX.text()+"\n")
        write_data.insert(2,self.ConfigResolutionY.text()+"\n")
        write_data.insert(3,"MQTT\n")
        write_data.insert(4,self.ConfigBroker.text()+"\n")
        write_data.insert(5,self.ConfigPort.text()+"\n")
        #fw.write(line + '\n' for line in line_list)
        with open(file_path,'w') as config_file:
            config_file.writelines(write_data)



def on_publish(client, userdata, result):  # create function for callback
    print("data published \n")
    pass


def Main():

    app= QApplication(sys.argv)
    win = SmartTableWindow()
    win.show()
    sys.exit(app.exec_())

Main()
