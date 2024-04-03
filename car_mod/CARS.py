#-*-coding:utf-8-*-
"""
CreatedonMonApr122:08:542024

@author:mspea
"""

class Car ():
    
    def __init__(self,*args):
        self.price = args[0]
        self.make = args[1]
        self.model = args[2]
        self.year = args[3]
        self.category = args[4]
        self.leather = args[5]
        self.fuel = args[6]
        self.cyl = args[7]
        self.gear = args[8]
        self.drive = args[9]
        self.charger120 = args[10]
        self.charge140 = args[11]
        self.fe = args[12]
        self.fuel_cost = args[13]
        self.alt_fuel_cost = args[14]
        self.fuel_type = args[15]
        self.elect_range = args[16]
        self.gas_range = args[17]
        self.u_city = args[18]
        self.u_highway = args[19]
        self.alt_u_city = args[20]
        self.alt_u_highway = args[21]
        self.veh_class = args[22]
        self.avg_saving = args[23]
        self.atv_type = args[24]
        self.ev_motor = args[25]
        self.hybrid_avg_mpg = args[26]
        self.key = args[27]
        self.start_stop = args[28]


car_stats = ['11917','HONDA','StepWagon','2005','Minivan','No','Petrol','4','Automatic'
,'4x4','N/A','N/A','N/A','2400','N/A','Regular','N/A','N/A','23.3333','N/A','35','N/A'
,'TwoSeaters','-3000','N/A','N/A','N/A','N/A','1']



car1 = Car(*car_stats)

print(car1.make)