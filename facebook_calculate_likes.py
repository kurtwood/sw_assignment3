# First, let's query for all of the likes in your social
# network and store them in a slightly more convenient
# data structure as a dictionary keyed on each friend's
# name.
import facebook
import secret # This file contains the AUTH token
import operator
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
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
print reordered_likes_per_category

like_per_category_per_person = dict() # new dictionnary
like_per_category_per_person['Mean'] = dict()

for friend in friends:
    # one empty dictionnary per friend
    like_per_category_per_person[friend['name']] = dict()

number_of_friends = float(len(friends))

for categ in reordered_likes_per_category:
    # for all relevant categories
    categ_counter = 0
    for name in {friend['name'] for friend in friends}:
        # for all friends, identified by name
        counter = 0
        for person in reordered_likes_per_category[categ]:
            if person == name:
                counter += 1
            # count how many times they like a thing of that category
        like_per_category_per_person[name][categ] = counter
        categ_counter += counter
    like_per_category_per_person['Mean'][categ] = categ_counter / number_of_friends

statuses = { friend['name'] : g.get_connections(friend['id'], "statuses")['data']
        for friend in friends }
#print statuses
#json.dumps(statuses, sort_keys=True, indent=2)

likers = dict()
for categ in reordered_likes_per_category:
    likers[categ] = []

mean = like_per_category_per_person['Mean']

for person in like_per_category_per_person:
    if (person != 'Mean'):
        for categ in reordered_likes_per_category:
            if (like_per_category_per_person[person][categ] > mean[categ]):
                likers[categ].append(person)

friends_likes = Counter([like['name']
        for friend in likes
                for like in likes[friend]
                        if like.get('name')])

likers_number_of_statuses = dict()
# in the end : { category : number of statuses of all people who are active in that category }

for categ in likers:
    status_counter = 0
    for friend in likers[categ]:
        status_counter += len(statuses[friend])
    likers_number_of_statuses[categ] = status_counter

# put them in order
likers_number_of_statuses_ordered = sorted(likers_number_of_statuses.iteritems(), key=operator.itemgetter(1))

# prepare the graph
categories = []
number_of_statuses_per_category = []
error = []
for i in likers_number_of_statuses_ordered:
    categories.append(i[0])
    number_of_statuses_per_category.append(i[1])
    error.append(0)

y_pos = np.arange(len(categories)) # for the full graph
plt.barh(y_pos, number_of_statuses_per_category, xerr=error, align='center', alpha=0.4)
plt.yticks(y_pos, categories)
plt.xlabel('Number of likes for all people active in a given category')
plt.title('SW - Assignment 3')
plt.show()

"""pt = PrettyTable(field_names=['Name', 'Freq'])
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

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=90)

#plt.show()
"""