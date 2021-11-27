import pandas as pd

consumers = pd.read_csv('consumers.csv', sep=';')


def get_consumers_for_label(label):
    return list(consumers[consumers['Buying_type'].str.contains(str(label))]['Name'])
