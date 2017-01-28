from urllib.request import urlretrieve
import vk, os, time, math

session = vk.Session()
vkAPI = vk.API(session)

# userID = input('Enter user id: ')
userID = 'giltanas'
userID = vkAPI.utils.resolveScreenName(screen_name=userID)['object_id'] 

subscriptionsList = vkAPI.users.getSubscriptions(user_id = userID)['groups']['items']
groupList = ['-'+ str(x) for x in subscriptionsList]

posts = {}
newsFeed = vkAPI.newsfeed.get(filters='post', source_ids=','.join(groupList), count=100, timeout=10)
'''posts.update({x['post_id']: x['source_id'] for x in newsFeed['items']})

likedPosts = []

for post in posts.items():
    try:
        isLiked = vkAPI.likes.isLiked(user_id = userID, item_id = post[0], type = 'post', owner_id = post[1], timeout = 5)['liked']
    except Exception:
        print(str(Exception))'''