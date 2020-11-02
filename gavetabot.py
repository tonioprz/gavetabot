from Raspi_MotorHAT import Raspi_MotorHAT 
import atexit


class Robot:
    def __init__(self):
        mh = Raspi_MotorHAT(addr=0x6f) #direccion de la placa controladora
        self.m1 = mh.getMotor(1) #obtenemos objetos motor DC
        self.m2 = mh.getMotor(2)
        self.m1.setSpeed(0)
        self.m2.setSpeed(0)
        
    def turnOffMotors(self):
        self.m1.run(Raspi_MotorHAT.RELEASE)
        self.m2.run(Raspi_MotorHAT.RELEASE)

    atexit.register(turnOffMotors)

    def setMotorSpeed(self,sp1,sp2):
        if sp1<0: sp1 = -sp1
        if sp2<0: sp2 = -sp2
        self.m1.setSpeed(sp1)
        self.m2.setSpeed(sp2)

    def setFullBrake(self):
        self.m1.run(Raspi_MotorHAT.BRAKE)
        self.m2.run(Raspi_MotorHAT.BRAKE)

    def setForward(self):
        self.m1.run(Raspi_MotorHAT.FORWARD)
        self.m2.run(Raspi_MotorHAT.FORWARD)

    def setRotationRight(self):
        self.m1.run(Raspi_MotorHAT.FORWARD)
        self.m2.run(Raspi_MotorHAT.BACKWARD)

    def setRotationLeft(self):
        self.m1.run(Raspi_MotorHAT.BACKWARD)
        self.m2.run(Raspi_MotorHAT.FORWARD)

    def Move(self,sp1,sp2):
        if sp1>0: self.m1.run(Raspi_MotorHAT.FORWARD)
        if sp1<0: self.m1.run(Raspi_MotorHAT.BACKWARD)
        if sp1==0: self.m1.run(Raspi_MotorHAT.BRAKE)

        if sp2>0: self.m1.run(Raspi_MotorHAT.FORWARD)
        if sp2<0: self.m1.run(Raspi_MotorHAT.BACKWARD)
        if sp2==0: self.m1.run(Raspi_MotorHAT.BRAKE)
        