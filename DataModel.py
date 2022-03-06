from dataclasses import field


class Holiday:
    name:str
    date:str

class TemperatureStatistic:
    date:str
    temperature:int

class HolidayTemperatureStatistics:
    date_from:str
    date_to:str
    #Represent Holiday specific day
    date:str
    temperatures:list[TemperatureStatistic]=field(init=False)

    def get_temperatures(self):

        pass