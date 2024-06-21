import time
class Schedule:
    def __init__(self,person,morning,noon,evening,night):
        self.person = person
        self.morning = morning
        self.noon = noon
        self.evening = evening
        self.night = night
        self.morning_time()
    def morning_time(self):
        print(f"{self.person } {self.morning} da uygondi va yuvinib ovqatini yedi")
        time.sleep(2.4)
        self.noon_time()
    def noon_time(self):
        print(f"{self.person} {self.noon} da  ovqatini yeb ingliz tiliga ketdi")
        time.sleep(2.4)
        self.evening_time()
    def evening_time(self):
        print(f"{self.person} {self.evening} da  darslarini qilib,IT ga yol oldi")
        time.sleep(2.5)
        self.night_time()
    def night_time(self):
        print(f"{self.person} ovqatlanib, yoqtirgan kinosini korib uxlashga bordi soat {self.night} da")
obj = Schedule("Sarvar",7,13,17,23)






