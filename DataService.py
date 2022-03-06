import requests

from WeatherService.DataModel import Holiday
from WeatherService.Utils import parse_date


class WeatherService:

    @staticmethod
    def get_weather_on_date(date:str):
        #assume that date comes in that pattern: "2021-04-05"
        #https://www.metaweather.com/api/location/523920/2019/4/27/
        day,month,year= parse_date(date)
        res=requests.get(f"https://www.metaweather.com/api/location/523920/{year}/{month}/{day}/").json()
        return res[0]["the_temp"]

class CountriesService:

    @staticmethod
    def get_country_holidays_name():
        res=requests.get(f"https://date.nager.at/api/v3/PublicHolidays/2022/PL").json()
        holiday_list=[]
        for holiday in res:
            single_holiday=Holiday()
            single_holiday.name=holiday["name"]
            single_holiday.date=holiday["date"]
            holiday_list.append(single_holiday)
        return holiday_list

    # @staticmethod
    # def get_available_countries():
    #     res=requests.get("https://date.nager.at/api/v2/AvailableCountries")
    #     return res.json()

