import pandas as pd

def generate_calendar_html(events=None):
    events = [
            {'name': 'Teem Meeting 1', 'date': '2024-11-21'},
            {'name': 'Built Base Website', 'date': '2024-11-25'},
            {'name': 'Teem Meeting 2', 'date': '2024-11-26'},
            {'name': 'Teem Meeting 3', 'date': '2024-12-03'},
            {'name': 'Final Delivery', 'date': '2024-12-05'}
        ]
    # Create a date range for November and December 2024
    start_date = '2024-11-01'
    end_date = '2024-12-31'
    dates = pd.date_range(start_date, end_date, freq='D')

    # Create a DataFrame with the dates
    df = pd.DataFrame(dates, columns=['Date'])
    df['Day'] = df['Date'].dt.day
    df['DayOfWeek'] = df['Date'].dt.dayofweek  # 0=Monday, 6=Sunday

    # Create the calendar for each month
    calendars = []
    for month in [11, 12]:
        # Filter for the current month
        month_df = df[df['Date'].dt.month == month]
        
        # Determine the first day of the month
        first_day = month_df.iloc[0]['DayOfWeek']
        
        # Create an empty list for the calendar grid
        calendar_grid = []
        
        # Add blank cells for days before the first day of the month
        blank_days = [''] * first_day
        calendar_grid.extend(blank_days)
        
        # Add the actual days
        calendar_grid.extend(month_df['Day'].tolist())
        
        # Fill the last week with blanks if necessary
        while len(calendar_grid) % 7 != 0:
            calendar_grid.append('')
        
        # Reshape the list into weeks (each week contains 7 days)
        weeks = [calendar_grid[i:i+7] for i in range(0, len(calendar_grid), 7)]
        
        # Convert weeks into DataFrame
        month_calendar_df = pd.DataFrame(weeks, columns=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
        
        # Add events to the calendar
        if events:
            for event in events:
                event_date = pd.to_datetime(event['date'])
                if event_date.month == month:
                    day_idx = event_date.day - 1 + first_day
                    month_calendar_df.iloc[day_idx // 7, day_idx % 7] = f"{month_calendar_df.iloc[day_idx // 7, day_idx % 7]}: {event['name']}"
        
        # Convert DataFrame to HTML and store it
        calendars.append(month_calendar_df.to_html(classes='calendar', index=False, header=True, na_rep=''))

    # Join November and December calendars into one
    calendar_html = f"<h2>November 2024</h2>{calendars[0]}<h2>December 2024</h2>{calendars[1]}"

    return calendar_html