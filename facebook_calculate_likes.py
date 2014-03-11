 #This is a test by Timo
# First, let's query for all of the likes in your social
# network and store them in a slightly more convenient
# data structure as a dictionary keyed on each friend's
# name.
import facebook
from prettytable import PrettyTable
from collections import Counter
import secret

# Create a connection to the Graph API with your access token
<<<<<<< HEAD
g = facebook.GraphAPI('CAACEdEose0cBAHvKoZAIcBdPK8ZCR08xFh4EZAzqWS0b6eiHvD9XyxpSNBvZCK3lYnWs8kkh0Ff6q78bKFVZCsE7ffKfosGlkL4PsHubbX5oPjSRQVTOAR1gHTnQbijdXEWea55wbFucMfMPFscRvo3YI5XIRMH1L40FmbrWTXAAOOr8lm2kxWLmziAfsBQgZD')
=======
g = facebook.GraphAPI(secret.ACCESS_TOKEN)
>>>>>>> 70cebda96c7425217d8e7bb15098575070acbc99

friends = g.get_connections("me", "friends")['data']

likes = { friend['name'] : g.get_connections(friend['id'], "likes")['data']
        for friend in friends }
#print likes

friends_likes = Counter([like['name']
        for friend in likes
                for like in likes[friend]
                        if like.get('name')])

pt = PrettyTable(field_names=['Name', 'Freq'])
pt.align['Name'], pt.align['Freq'] = 'l', 'r'
[ pt.add_row(fl) for fl in friends_likes.most_common(10) ]

print 'Top 10 likes amongst friends'
print pt


# Analyze all like categories by frequency
friends_likes_categories = Counter([like['category']
        for friend in likes
                for like in likes[friend]])

pt2 = PrettyTable(field_names=['Category', 'Freq'])
pt2.align['Category'], pt2.align['Freq'] = 'l', 'r'
[ pt2.add_row(flc) for flc in friends_likes_categories.most_common(10) ]

print "Top 10 like categories for friends"
print pt2