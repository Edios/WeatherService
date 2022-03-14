from dataclasses import dataclass


@dataclass
class Holiday:
    name:str
    date:str


@dataclass
class TemperatureStatistic:
    date:str
    temperature:float