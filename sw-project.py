# Import the SDK
import facebook
# import the secret token
#import secret
# For date and time operations
from datetime import datetime, date, time
# To use the cmdline arguments
import sys

# open connection
#g = facebook.GraphAPI(secret.ACCESS_TOKEN)
g = facebook.GraphAPI(sys.argv[1])

# retrieve friends
friends = g.get_connections("me", "friends")['data']
if len(friends) > 50:
    friends = friends[:50]

# retrieve their likes
likes = {friend['name']: g.get_connections(friend['id'], "likes")['data']
         for friend in friends}

statuses = {friend['name']: g.get_connections(friend['id'], "statuses")['data']
            for friend in friends}
# take a look at a 'created_time' value of a random like, cf http://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
fb_date_format = "%Y-%m-%dT%H:%M:%S+0000"

likes_times = []

for friend in likes:
    for like in likes[friend]:
        likes_times.append(datetime.strptime(like['created_time'], fb_date_format))

statuses_times = []

for friend in statuses:
    for status in statuses[friend]:
        statuses_times.append(datetime.strptime(status['updated_time'], fb_date_format))

# Retrieve the number of Statuses per day for the last 7 days
now = datetime.now()

# How many...
seconds_per_week = 7 * 24 * 60 * 60

statuses_last_week = []
for i in range(0, 7):
    statuses_last_week.append(0)

for status_time in statuses_times:
    if (now - status_time).total_seconds() < seconds_per_week:
        statuses_last_week[status_time.weekday()] += 1

likes_last_week = []
for i in range(0, 7):
    likes_last_week.append(0)

for like_time in likes_times:
    if (now - like_time).total_seconds() < seconds_per_week:
        likes_last_week[like_time.weekday()] += 1

activity_last_week = []
for i in range(7):
    activity_last_week.append(likes_last_week[i] + statuses_last_week[i])

statuses_per_weekday = []
for i in range(0, 7):
    statuses_per_weekday.append([])

for status_time in statuses_times:
    statuses_per_weekday[status_time.weekday()].append(status_time)

likes_per_weekday = []
for i in range(0, 7):
    likes_per_weekday.append([])

for like_time in likes_times:
    likes_per_weekday[like_time.weekday()].append(like_time)


def get_number(day, hour_from, hour_to, sorted_list):
    result = 0
    for time in sorted_list[day]:
        if (time.hour < hour_to) and (time.hour >= hour_from):
            result += 1
    return result


return_list_total = []

for day in range(7):
    for hour in range(6):
        return_list_total.append(get_number(day, 4 * hour, 4 * (hour + 1), likes_per_weekday) +
                           get_number(day, 4 * hour, 4 * (hour + 1), statuses_per_weekday))

print (activity_last_week)
print (return_list_total)
