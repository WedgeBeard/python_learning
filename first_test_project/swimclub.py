FOLDER = "swimdata/"
import statistics

def read_swim_data(filename):
    swimmer, age, distance, stroke = filename.removesuffix(".txt").split("-")
    with open(FOLDER + filename) as file:
        line = file.readlines()
        times = line[0].strip().split(",")
    converted = []
    for t in times:
        minutes, rest = t.split(":")
        seconds, milliseconds = rest.split(".")
        converted.append((int(minutes) * 6000) + (int(seconds) * 100) + int(milliseconds))
    sum = 0
    avg = statistics.mean(converted)
    avg_minutes = int(avg/6000)
    avg_seconds = int(int(avg - (6000*avg_minutes))/100)
    avg_milliseconds = round(avg - avg_minutes*6000 - avg_seconds * 100)
    avg_str = (str(avg_minutes) + ":" + str(avg_seconds) + "." + str(avg_milliseconds))
    return swimmer, age, distance, stroke, times, avg_str