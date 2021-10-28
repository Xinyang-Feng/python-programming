import csv
from matplotlib import pyplot as plt
from datetime import datetime
# 1
# filename = 'sitka_weather_2018_full.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     type(reader)
#     header_row = next(reader) # The header row is "skipped" as a result of calling next()

#     # To make it easier to understand the file header data,
#     # print each header and its position in the list
#     for index, column_header in enumerate(header_row):
#         print(index, column_header)

#     # Get dates, high and low temperature from file.
#     dates, highs, lows = [], [], []
#     for row in reader:
#         current_date = datetime.strptime(row[2], "%Y-%m-%d")
#         dates.append(current_date)

#         high = row[8] 
#         highs.append(high)

#         low = row[9]
#         lows.append(low)


# # Plot data
# fig = plt.figure(dpi=128, figsize=(10, 6))
# plt.plot(dates, highs, c='red', alpha=0.5) # Plot y versus x as lines and/or markers.
# plt.plot(dates, lows, c='blue', alpha=0.5)
# plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# # Format plot.
# plt.title("Daily high and low temperatures", fontsize=24)
# plt.xlabel('', fontsize=10)
# fig.autofmt_xdate()
# plt.ylabel("Temperature(F)", fontsize=10)
# plt.tick_params(axis='both', which='major', labelsize=10)

# plt.show()

# 2
filename1 = "death_valley_2018_full.csv"
with open(filename1) as f:
    reader = csv.reader(f)
    header_row = next(reader) # The header row is "skipped" as a result of calling next()

    # To make it easier to understand the file header data,
    # print each header and its position in the list
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # Get dates, high and low temperature from file.
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            high = row[7]
            low = row[8]
        except ValueError:
            print(current_date, 'missing_data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5) # Plot y versus x as lines and/or markers.
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
plt.title("Daily high and low temperatures\nDeath Vally", fontsize=20)
plt.xlabel('', fontsize=10)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.show()




















