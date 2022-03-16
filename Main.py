# TODO: Tinker GUI
# from WeatherService.HolidayTemperatureStatistics import HolidayTemperatureStatistics
from tkinter.ttk import Combobox

from WeatherService.DataModel import TemperatureStatistic
from WeatherService.DataService import DataRetrievalService
#
# holiday_list = DataRetrievalService().get_country_holidays_list()
# years = [x for x in range(2016, 2022)]
#
# #Mock for choosed holiday index
# choosed_holiday=holiday_list[2]
# holiday_index=holiday_list.index(choosed_holiday)
#
# temp_stats=HolidayTemperatureStatistics(holiday_index,years)
# temp_stats.get_temperature_statistic()
#
# list_of_dates=[stat.date for stat in temp_stats.temperatureStatistics]
# list_of_temperatures=[stat.temperature for stat in temp_stats.temperatureStatistics]
# print(list_of_dates,list_of_temperatures)
import tkinter
from tkinter import Tk, Label, messagebox

from WeatherService.HolidayTemperatureStatistics import HolidayTemperatureStatistics
from WeatherService.Utils import get_item_index_in_list


class HolidayTemperatureStatisticGUI:
    holidayList:list
    selectedHolidayIndex:int
    yearsList:list[int]
    startingYear:int
    selectedYearsRange:list[int]
    temperatureStatistics:list[TemperatureStatistic]

    def __init__(self, master: tkinter.Tk):
        self.holidayList = DataRetrievalService().get_country_holidays_list()
        self.yearsList=[year for year in range(2000,2022)]
        # GUI
        self.master = master
        self.master.title("Holiday Temperature Statistic")
        self.master.geometry("1000x600")
        self.label = Label(master, text="Holiday Temperature Statistic")
        self.label.grid(row=0,column=0,sticky="we")

        self.left_frame = tkinter.Frame(master, bg="green", highlightbackground="black", highlightthickness=2)
        self.left_frame.grid(row=1, column=0)

        self.right_frame = tkinter.Frame(master, bg="gray", highlightbackground="black", highlightthickness=2)
        self.right_frame.grid(row=1, column=1)

        self.plot_frame = tkinter.Frame(master, bg="gray", highlightbackground="black", highlightthickness=2)
        self.plot_frame.grid(row=2, column=1)

        #Holiday combobox
        self.holiday_combobox=Combobox(self.left_frame,values=self.holidayList)
        self.holiday_combobox.grid(row=0,column=0)
        self.holiday_combobox.bind("<<ComboboxSelected>>",self.set_holiday_index)
        # YearRangeFrom
        self.year_range_from_combobox=Combobox(self.right_frame,values=self.yearsList)
        self.year_range_from_combobox.grid(row=0,column=0)
        self.year_range_from_combobox.bind("<<ComboboxSelected>>",self.set_starting_year)
        # YearRangeTo
        self.year_range_from_combobox=Combobox(self.right_frame,values=self.yearsList)
        self.year_range_from_combobox.grid(row=0,column=1)
        self.year_range_from_combobox.bind("<<ComboboxSelected>>",self.set_selected_years_range)
        # btn Show Plot
        btn = tkinter.Button(self.right_frame, width=30, height=2, text="Generate plot", command=self.generate_plot)
        btn.grid(row=1, column=0)

    def set_holiday_index(self,item):
        selected_item=item.widget.get()
        self.selectedHolidayIndex=get_item_index_in_list(selected_item, self.holidayList)

    def set_starting_year(self,item):
        selected_item=item.widget.get()
        self.startingYear=int(selected_item)

    def set_selected_years_range(self,item):
        selected_year = int(item.widget.get())
        difference= selected_year - self.startingYear
        validation_error=False
        if difference<=1:
            messagebox.showerror(title="Value Error",message="Uncorrect years values")
            validation_error=True
        if not validation_error:
            self.selectedYearsRange=[year for year in range(self.startingYear,self.startingYear+difference)]

    def set_temperature_statistic(self):
        temp_stats=HolidayTemperatureStatistics(self.selectedHolidayIndex,self.selectedYearsRange)
        self.temperatureStatistics=temp_stats.get_temperature_statistic()

    def generate_plot(self):
        self.set_temperature_statistic()
        # TODO: Add validation: Holiday must be choosed, Years must be picked. Data from statistic must be present



root = Tk()
my_gui = HolidayTemperatureStatisticGUI(root)
root.mainloop()
