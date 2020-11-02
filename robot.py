from Raspi_MotorHAT import Raspi_MotorHAT 
import atexit

mh = Raspi_MotorHAT(addr=0x6f) #direccion de la placa controladora
m1 = mh.getMotor(1) #obtenemos objetos motor DC
m2 = mh.getMotor(2)

def turnOffMotors():
    m1.run(Raspi_MotorHAT.RELEASE)
    m2.run(Raspi_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

def setMotorSpeed(sp1,sp2):
    m1.setSpeed(sp1)
    m2.setSpeed(sp2)

def setFullBrake():
    m1.run(Raspi_MotorHAT.BRAKE)
    m2.run(Raspi_MotorHAT.BRAKE)

def setForward():
    m1.run(Raspi_MotorHAT.FORWARD)
    m2.run(Raspi_MotorHAT.FORWARD)

