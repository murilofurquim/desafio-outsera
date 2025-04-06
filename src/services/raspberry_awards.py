from src.database import database

class RaspberryAwards:
    producer: str
    interval: int
    previousWin: str
    folowingWin: str

    def __init__(self, producer, interval, previousWin, folowingWin):
        self.producer = producer
        self.interval = interval
        self.previousWin = previousWin
        self.folowingWin = folowingWin

class Intervals:
    min: list[RaspberryAwards]
    max: list[RaspberryAwards]

def get_raspberry_min_max_awards():
    intervals = Intervals()
    min, max = database.get_dados()
    intervals.min = [RaspberryAwards(producer=x[0], interval=x[3], previousWin=x[2], folowingWin=x[1]) for x in min]
    intervals.max = [RaspberryAwards(producer=x[0], interval=x[3], previousWin=x[2], folowingWin=x[1]) for x in max]

    return intervals