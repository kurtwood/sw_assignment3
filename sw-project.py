# Import the SDK
import facebook
# import the secret token
import secret
# For date and time operations
from datetime import datetime, date, time

# open connection
g = facebook.GraphAPI(secret.ACCESS_TOKEN)

# retrieve friends
friends = g.get_connections("me", "friends")['data']

# retrieve their likes
likes = { friend['name'] : g.get_connections(friend['id'], "likes")['data']
        for friend in friends }

statuses = { friend['name'] : g.get_connections(friend['id'], "statuses")['data']
        for friend in friends }
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