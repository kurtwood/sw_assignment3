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

