import os
import pandas as pd
from io import StringIO
from datetime import datetime
import matplotlib.ticker as mtick



def percentage_string_to_number(x):
    return float(x.strip('%'))/100

def plot_area(variable, ax, to_show, title):
    to_show.pivot(index="time", columns="name", values=variable).plot.area(ax=ax)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
    ax.set_title(title + str(datetime.now())) 

def run_and_get_docker_stats():
    stream = os.popen(
        'sudo docker stats --no-stream --format "{{ .Container }}, {{ .Name }}, {{ .MemUsage }}, {{ .MemPerc }}, {{ .CPUPerc }}, {{.NetIO}}" | tee')
    output = stream.read()
    return output

def read_pandas_dataframe(output):
    stats = pd.read_csv(StringIO(output), header=None, names=["container_id", "name", "memory_usage",
                                                              "memory_percentage", "cpu_percentange",
                                                              "network_io"],
                        converters={'memory_percentage': percentage_string_to_number,
                                    'cpu_percentange': percentage_string_to_number})
    stats["time"] = datetime.now()
    return stats


