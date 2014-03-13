# First, let's query for all of the likes in your social
# network and store them in a slightly more convenient
# data structure as a dictionary keyed on each friend's
# name.
import facebook
import secret # This file contains the AUTH token
from functools import reduce
from prettytable import PrettyTable
from collections import Counter

def reorder(result, item):
    for y in item[1]:
        result.setdefault(y['category'], list()).append(item[0])
    return result

# Create a connection to the Graph API with your access token

g = facebook.GraphAPI(secret.ACCESS_TOKEN)

friends = g.get_connections("me", "friends")['data']

likes = { friend['name'] : g.get_connections(friend['id'], "likes")['data']
        for friend in friends }
print "========= LIKES"
print likes

reordered_likes_per_category = reduce(reorder, likes.items(), {})
print "========= NEW LIST"
print reordered_likes

statuses = { friend['name'] : g.get_connections(friend['id'], "statuses")['data']
        for friend in friends }
#print statuses
#json.dumps(statuses, sort_keys=True, indent=2)

friends_likes = Counter([like['name']
        for friend in likes
                for like in likes[friend]
                        if like.get('name')])

pt = PrettyTable(field_names=['Name', 'Freq'])
pt.align['Name'], pt.align['Freq'] = 'l', 'r'
[ pt.add_row(fl) for fl in friends_likes.most_common(10) ]

print '====== Top 10 likes amongst friends'
print pt


# Analyze all like categories by frequency
friends_likes_categories = Counter([like['category']
        for friend in likes
                for like in likes[friend]])

pt2 = PrettyTable(field_names=['Category', 'Freq'])
pt2.align['Category'], pt2.align['Freq'] = 'l', 'r'
[ pt2.add_row(flc) for flc in friends_likes_categories.most_common(10) ]

print "====== Top 10 like categories for friends"
print pt2