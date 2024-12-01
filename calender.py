import pandas as pd
from datetime import datetime, timedelta


# Pandas Settings
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Date Stuff
first_day = datetime.today()
last_day = first_day + timedelta(days=30)
dates = pd.date_range(first_day, last_day, freq='D').strftime('%d-%m-%Y').tolist()

try:
    df = pd.read_csv("takvim_uygulamasi.csv")
    df.to_csv("takvim_uygulamasi.csv", index=False)
except FileNotFoundError:
    df = pd.DataFrame(columns=dates)

def generate_calendar_html():
    calendar_html = df.to_html(classes='calendar', index=False)
    return calendar_html