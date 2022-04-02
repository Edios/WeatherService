from dataclasses import field, dataclass

from DataModel import Holiday, TemperatureStatistic
from DataService import DataRetrievalService

@dataclass
class HolidayTemperatureStatistics:
    choosedHolidayIndex: int
    yearsRange:list[int]
    allHolidays:list[Holiday]=field(init=False)
    # Secret sauce
    temperatureStatistics:list[TemperatureStatistic]=field(init=False)

    def __post_init__(self):
        self.dataService = DataRetrievalService()
        self.allHolidays=self.dataService.get_country_holidays_list()

    def get_holidays_days(self)->list:
        holidayDates=[]
        for year in self.yearsRange:
            date = self.dataService.get_country_holidays_list(str(year))
            holidayDates.append(date[self.choosedHolidayIndex].date)
        return holidayDates

    def get_temperature_statistic(self)->list:
        # Holidays can occur on different days every year.
        holidays_dates = self.get_holidays_days()
        # Map holidays with
        weather_on_holiday_day = list(map(self.dataService.get_weather_on_date, holidays_dates))
        self.temperatureStatistics = [TemperatureStatistic(single_statistic[0], single_statistic[1]) for single_statistic in
                                      list(zip(holidays_dates, weather_on_holiday_day))]
        return self.temperatureStatistics