import numpy as np
import pandas as pd
import time

class User():

    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.numofpoints = 0

    def setUsername(self,username):
        self.username = username

    def setPassword(self,password):
        self.password = password

    def addpoints(self, addpoints):
       self.numofpoints = self.numofpoints+addpoints


class Challenge():

    def __init__(self,objective,duration,points):

        self.users = []
        self.objective = objective
        self.duration = duration
        self.energyval = points
        self.numofusers = 0


    def adduser(self,user):
        self.users.append(user.username)
    
    

    