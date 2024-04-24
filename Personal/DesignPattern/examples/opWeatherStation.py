from abc import ABC, abstractmethod

# Interfaces
class Observer(ABC):
    @abstractmethod
    def update(self):
        pass

class Observable(ABC):
    @abstractmethod
    def registerObserver(self, o :Observer):
        pass

    @abstractmethod
    def removeObserver(self, o :Observer):
        pass

    @abstractmethod
    def notifyObserver(self):
        pass

class DisplayElement(ABC):
    @abstractmethod
    def display(self):
        pass


# Concrete classes
class WeatherData(Observable):
    def __init__(self):
        self.observers = []
        self.temparature = None
        self.humidity = None

    def registerObserver(self, o :Observer):
        self.observers.append(o)

    def removeObserver(self, o :Observer):
        if o in self.observers:
            self.observers.remove(o)

    def notifyObservers(self):
        for o in self.observers:
            o.update()

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temparature, humidity):
        self.temparature = temparature
        self.humidity = humidity
        self.measurementsChanged()

    def getTemparature(self):
        return self.temparature

    def getHumidity(self):
        return self.humidity

class CurrentConditonDisplay(Observer):
    def __init__(self, weatherDataObject :Observable):
        self.temparature = None
        self.humidity = None
        self.weatherData = weatherDataObject
        self.weatherData.registerObserver(self)

    def display(self):
        print(f"Current conditions: {self.temparature} degree C and {self.humidity}% humidity")

    def update(self):
        self.temparature = self.weatherData.getTemparature()
        self.humidity = self.weatherData.getHumidity()
        self.display()

class StatisticsDisplay(Observer):
    def __init__(self, weatherDataObject :Observable):
        self.temparatures = set()
        self.maxTemparature = None
        self.minTemparature = None
        self.avgTemparature = None
        self.weatherData = weatherDataObject
        self.weatherData.registerObserver(self)

    def display(self):
        print(f"Avg/Max/Min temperature = {self.avgTemparature}/{self.maxTemparature}/{self.minTemparature}")

    def update(self):
        self.temparatures.add(self.weatherData.getTemparature())
        self.maxTemparature = max(self.temparatures)
        self.minTemparature = min(self.temparatures)
        self.avgTemparature = round(sum(self.temparatures) / len(self.temparatures), 2)

        self.display()


if __name__ == "__main__":
    weatherData = WeatherData()
    currentConditonDisplay = CurrentConditonDisplay(weatherData)
    statisticsDisplay = StatisticsDisplay(weatherData)

    weatherData.setMeasurements(80, 65)
    weatherData.setMeasurements(82, 70);
    weatherData.setMeasurements(100, 90);
    weatherData.setMeasurements(78, 90);