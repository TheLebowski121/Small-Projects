from datetime import datetime

def calculate_time_elapsed(start_date, end_date):
    # Convert the date strings to datetime objects
    start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
    end_datetime = datetime.strptime(end_date, "%Y-%m-%d")

    # Calculate the difference between the two datetime objects
    time_difference = end_datetime - start_datetime

    # Extract the days, hours, and minutes from the time difference
    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return days, hours, minutes

# Example usage
start_date = input("Inputstart Date Y/M/D")
end_date = input("Input End Date Y/M/D")
days_elapsed, hours_elapsed, minutes_elapsed = calculate_time_elapsed(start_date, end_date)

print(f"Time elapsed: {days_elapsed} days, {hours_elapsed} hours, {minutes_elapsed} minutes")
