from tkinter.ttk import Combobox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from WeatherService.DataModel import TemperatureStatistic
from WeatherService.DataService import DataRetrievalService
import tkinter
from tkinter import Tk, Label, messagebox
from WeatherService.HolidayTemperatureStatistics import HolidayTemperatureStatistics
from WeatherService.Utils import get_item_index_in_list


class HolidayTemperatureStatisticGUI:
    holidayList: list
    selectedHolidayIndex: int
    yearsList: list[int]
    startingYear: int
    selectedYearsRange: list[int]
    temperatureStatistics: list[TemperatureStatistic]

    def __init__(self, master: tkinter.Tk):
        self.holidayList = DataRetrievalService().get_country_holidays_list()
        # For Warsaw location statistic are gathered from ~~2014
        self.yearsList = [year for year in range(2014, 2023)]
        # GUI
        self.master = master
        self.master.title("Holiday Temperature Statistics")
        self.master.geometry("1200x800")
        self.label = Label(master, text="Holiday Temperature Statistics")
        self.label.grid(row=0, column=0, sticky="we")

        self.right_frame = tkinter.Frame(master, bg="gray", highlightbackground="black", highlightthickness=1)
        self.right_frame.grid(row=1, column=2)

        self.plot_frame = tkinter.Frame(master, bg="gray", highlightbackground="black", highlightthickness=2)
        self.plot_frame.grid(row=2, column=2)

        # Holiday combobox
        self.label = Label(self.right_frame, text="Holiday day:")
        self.label.grid(row=0, column=0,ipady=1)
        self.holiday_combobox = Combobox(self.right_frame, values=self.holidayList)
        self.holiday_combobox.grid(row=0, column=1,ipady=1, sticky="we")
        self.holiday_combobox.bind("<<ComboboxSelected>>", self.set_holiday_index)
        # YearRangeFrom
        self.label = Label(self.right_frame, text="Starting year")
        self.label.grid(row=1, column=0, ipady=1)
        self.year_range_from_combobox = Combobox(self.right_frame, values=self.yearsList)
        self.year_range_from_combobox.grid(row=1, column=1)
        self.year_range_from_combobox.bind("<<ComboboxSelected>>", self.set_starting_year)
        # YearRangeTo
        self.label = Label(self.right_frame, text="Ending year:")
        self.label.grid(row=2, column=0)
        self.year_range_from_combobox = Combobox(self.right_frame, values=self.yearsList)
        self.year_range_from_combobox.grid(row=2, column=1)
        self.year_range_from_combobox.bind("<<ComboboxSelected>>", self.set_selected_years_range)
        # btn Show Plot
        btn = tkinter.Button(self.right_frame, width=30, height=2, text="Generate plot", command=self.generate_plot)
        btn.grid(row=3, column=0)

    def set_holiday_index(self, item):
        selected_item = item.widget.get()
        self.selectedHolidayIndex = get_item_index_in_list(selected_item, self.holidayList)

    def set_starting_year(self, item):
        selected_item = item.widget.get()
        self.startingYear = int(selected_item)

    def set_selected_years_range(self, item):
        selected_year = int(item.widget.get())
        difference = selected_year - self.startingYear
        validation_error = False
        if difference <= 1:
            messagebox.showerror(title="Value Error", message="Incorrect years values")
            validation_error = True
        if not validation_error:
            self.selectedYearsRange = [year for year in range(self.startingYear, self.startingYear + difference)]

    def set_temperature_statistic(self):
        temp_stats = HolidayTemperatureStatistics(self.selectedHolidayIndex, self.selectedYearsRange)
        self.temperatureStatistics = temp_stats.get_temperature_statistic()

    def generate_plot(self):
        self.set_temperature_statistic()
        # TODO: Add validation: Holiday must be chosen, Years must be picked. Data from statistic must be present
        x = [stat.date for stat in self.temperatureStatistics]
        y = [stat.temperature for stat in self.temperatureStatistics]
        fig = Figure(figsize=(9, 5), dpi=100)
        plot1 = fig.add_subplot(111)
        width = .5
        plot1.bar(x, y, width)
        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0)


root = Tk()
gui = HolidayTemperatureStatisticGUI(root)
root.mainloop()
