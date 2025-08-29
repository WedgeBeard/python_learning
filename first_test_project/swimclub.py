FOLDER = "swimdata/"
import statistics

def read_swim_data(filename):
    """Return swim data from a file.
    
    Given the name of a swimmer's file (in filename), extract all the required
    data, then return it to the caller as a tuple.
    """
    swimmer, age, distance, stroke = filename.removesuffix(".txt").split("-")
    with open(FOLDER + filename) as file:
        line = file.readlines()
        times = line[0].strip().split(",")
    converted = []
    for t in times:
        # The swim data coule be less than 1 minute, guard against it here.
        if ":" in t:
            minutes, rest = t.split(":")
        else:
            minutes = 0
            rest = t
        seconds, milliseconds = rest.split(".")
        converted.append((int(minutes) * 6000) + (int(seconds) * 100) + int(milliseconds))
    avg = statistics.mean(converted)
    avg_minutes = int(avg/6000)
    avg_seconds = int(int(avg - (6000*avg_minutes))/100)
    avg_milliseconds = round(avg - avg_minutes*6000 - avg_seconds * 100)
    avg_str = (f"{avg_minutes}:{avg_seconds}.{avg_milliseconds}")
    return swimmer, age, distance, stroke, times, avg_str, converted # Returned as a tuple.