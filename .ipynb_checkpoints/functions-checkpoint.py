import os
import pandas as pd
from io import StringIO


def percentage_string_to_number(x):
    return float(x.strip('%'))/100

def run_and_get_docker_stats():
    stream = os.popen(
        'docker stats --no-stream --format "{{ .Container }}, {{ .Name }}, {{ .MemUsage }}, {{ .MemPerc }}, {{ .CPUPerc }}, {{.NetIO}}" | tee')
    output = stream.read()
    return output

def read_pandas_dataframe(output, docker_project: str):
    stats = pd.read_csv(StringIO(output), header=None, names=["container_id", "name", "memory_usage",
                                                              "memory_percentage", "cpu_percentange",
                                                              "network_io"],
                        converters={'memory_percentage': percentage_string_to_number,
                                    'cpu_percentange': percentage_string_to_number})
    return stats


