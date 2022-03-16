from dataclasses import dataclass


@dataclass
class Holiday:
    name:str
    date:str

    def __str__(self):
        return self.name


@dataclass
class TemperatureStatistic:
    date:str
    temperature:float