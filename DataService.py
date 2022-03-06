import requests

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
    def get_country_holidays_name(country_code):
        res=requests.get(f"https://date.nager.at/api/v3/PublicHolidays/2022/{country_code}").json()
        return res

    @staticmethod
    def get_available_countries():
        res=requests.get("https://date.nager.at/api/v2/AvailableCountries")
        return res.json()

# x=WeatherService().get_available_countries()
#
#
# print(x)