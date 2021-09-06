import time
import cv2
import RPi.GPIO as GPIO
import pigpio

class Steer:

    def __init__(self):
      self.pwm = []

      # Motor1, Motor2, Motor3, Motor4, ThrottleL, ThrottleF
      self.outputPins = [22, 24, 26, 28, 16, 18]
      self.Motor1, self.Motor2, self.Motor3, self.Motor4, self.ThrottleL, self.ThrottleF = [22, 24, 26, 28, 16, 18]

      
    def driveSetup(self):
      GPIO.setmode(GPIO.BCM)
      self.pi = pigpio.pi()

      self.pi.set_servo_pulsewidth(24, 1500)
      time.sleep(2)

      self.pi.set_servo_pulsewidth(24, 1000)
      time.sleep(2)

      self.pi.set_servo_pulsewidth(24, 1200)
      time.sleep(2)

    def targetEvaluation(targetList):
        print(targetList)

    def testPWM(self):
      for i in self.outputPins:
        for dutyCycle in range(0, 21, 2):
          self.pwm[i].ChangeDutyCycle(dutyCycle)
          time.sleep(0.05)

    def forward(self, PWM, acceleration):
      forwardPins = [self.Motor2, self.Motor4]
      for i in forwardPins:
        for dutyCycle in range(0, PWM +1, acceleration):
          self.pwm[i].ChangeDutyCycle(dutyCycle)
          time.sleep(0.05)

    def turn(self, PWM, acceleration, angle):
      turnPins = [self.Motor2, self.Motor4]
      if angle > 0:
        for i in turnPins:
          for dutyCycle in range(0, PWM +1, acceleration):
            self.pwm[turnPins[1]].ChangeDutyCycle(dutyCycle)
            time.sleep(0.05)
      if angle < 0:
        for i in turnPins:
          for dutyCycle in range(0, PWM +1, acceleration):
            self.pwm[turnPins[0]].ChangeDutyCycle(dutyCycle)
            time.sleep(0.05)


    def shutdown(self):
      self.pi.set_servo_pulsewidth(24, 0)
      self.pi.stop()
      self.pwm.stop()
      GPIO.cleanup()