#TODO: Tinker GUI
from WeatherService.HolidayTemperatureStatistics import HolidayTemperatureStatistics
from WeatherService.DataService import DataRetrievalService

holiday_list = DataRetrievalService().get_country_holidays_list()
years = [x for x in range(2016, 2022)]

#Mock for choosed holiday index
choosed_holiday=holiday_list[2]
holiday_index=holiday_list.index(choosed_holiday)

temp_stats=HolidayTemperatureStatistics(holiday_index,years)

list_of_dates=[stat.date for stat in temp_stats.temperatureStatistics]
list_of_temperatures=[stat.temperature for stat in temp_stats.temperatureStatistics]
print(list_of_dates,list_of_temperatures)