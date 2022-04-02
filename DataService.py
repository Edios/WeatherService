import requests
from DataModel import Holiday
from Utils import parse_date


class DataRetrievalService:

    @staticmethod
    def get_weather_on_date(date: str) -> float:
        # assume that date comes in that pattern: "2021-04-05"
        year, month, day = parse_date(date)
        res = requests.get(f"https://www.metaweather.com/api/location/523920/{year}/{month}/{day}/").json()
        return res[0]["the_temp"]

    @staticmethod
    def get_country_holidays_list(year: str = "2022") -> list:
        res = requests.get(f"https://date.nager.at/api/v3/PublicHolidays/{year}/PL").json()
        holiday_list = []
        for holiday in res:
            holiday_list.append(Holiday(holiday["localName"], holiday["date"]))
        return holiday_list