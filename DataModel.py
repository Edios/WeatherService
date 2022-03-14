from dataclasses import field, dataclass


@dataclass
class Holiday:
    name:str
    date:str

@dataclass
class TemperatureStatistic:
    date:str
    temperature:int

@dataclass
class HolidayTemperatureStatistics:
    temperatureStatistics:list[TemperatureStatistic]=field(init=False)

    def get_temperatures(self):

        pass