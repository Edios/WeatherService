import requests

from WeatherService.DataModel import Holiday
from WeatherService.Utils import parse_date


class WeatherService:

    @staticmethod
    def get_weather_on_date(date:str)->float:
        #assume that date comes in that pattern: "2021-04-05"
        #https://www.metaweather.com/api/location/523920/2019/4/27/
        year,month,day= parse_date(date)
        res=requests.get(f"https://www.metaweather.com/api/location/523920/{year}/{month}/{day}/").json()
        return res[0]["the_temp"]

class HolidayService:

    @staticmethod
    def get_country_holidays_name(year:str="2022")->list[Holiday]:
        res=requests.get(f"https://date.nager.at/api/v3/PublicHolidays/{year}/PL").json()
        holiday_list=[]
        for holiday in res:
            single_holiday=Holiday()
            single_holiday.name=holiday["localName"]
            single_holiday.date=holiday["date"]
            holiday_list.append(single_holiday)
        return holiday_list

holiday=HolidayService()
holidayList=holiday.get_country_holidays_name()
#Get holiday names
holidayNames=[holiday.name for holiday in holidayList]
#This need to be picked from interface
#In this example im using Easter Sunday cuz its moving
choosed_holiday=holidayList[2]
#Taking date from holiday
years=[str(x) for x in range(2016,2022)]
holidayDates=[]
for year in years:
    date=holiday.get_country_holidays_name(year)
    list_index=holidayList.index(choosed_holiday)
    holidayDates.append(date[list_index].date)
#Get temperature for holidayDates
weather=WeatherService()
weatherOnHolidayDay=[weather.get_weather_on_date(day) for day in holidayDates]
#other way
weatherOnHolidayDay2=list(map(weather.get_weather_on_date,holidayDates))
#TODO: Map holidayDates to


