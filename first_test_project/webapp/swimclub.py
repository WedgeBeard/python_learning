import statistics
import normalizer

FOLDER = "swimdata/"
CHARTS = "charts/"

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
    avg_str = (f"{avg_minutes}:{avg_seconds:0<2}.{avg_milliseconds}")
    return swimmer, age, distance, stroke, times, avg_str, converted # Returned as a tuple.

def produce_bar_charts(filename):
    """Given the name of a swimmer's file, produce a HTML/SVG-based bar chart.
    
    Save the chart to the CHARTS folder. Return the path tp the bar chart file.
    """
    (swimmer, age, distance, stroke, times, average, converts) = read_swim_data(filename)
    title = (f"{swimmer} (Under {age}) {distance} {stroke}")
    times.reverse()
    converts.reverse()
    
    header = (f"""<!DOCTYPE html>
    <html>
        <head>
            <title>
                {title}
            </title>
        </head>
        <body>
            <h3>{title}</h3>""")
    
    max_in = max(converts)
    body = ""
    
    for n, t in enumerate(converts):
        normalized = normalizer.get_normalized(converts[n], max_in, 0, 0, 350)
        body += f"""
                <svg height="30" width="400">
                    <rect height="30" width="{normalized}" style="fill:rgb(0,0,255);" />
                </svg>{times[n]}<br />"""
    
    footer = f"""
            <p>Average time: {average}</p>
        </body>
    </html>
        """
    webpage = header + body + footer
    outfile = (f"charts/{filename.removesuffix('.txt')}.html")

    with open(outfile, "w") as tf:
        print(webpage, file=tf)

    return outfile