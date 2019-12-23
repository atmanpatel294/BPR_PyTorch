import random 

def bpr(user, bpr_dict,items,user_items):
    unseen_items = None
    if bpr_dict[user]==set():
        unseen_items = set(items).difference(user_items[user])
        bpr_dict[user] = unseen_items
    else:
        unseen_items = bpr_dict[user]
    return int(random.choice(list(unseen_items)))

def sbpr(user,user_saved_items,sbpr_friend_dict,sbpr_negative_dict,
        bpr_dict,top_comm,user_items,items):
    if user not in top_comm:
        bpr_item = bpr(user,bpr_dict,items,user_items)
        return (bpr_item,bpr_item)
    
    random_friend_item = None
    similar_interests = None
    
    friends = top_comm[user]

    friend_items = set()
    similar_interests = 1
    if user_saved_items[user] == set():
        if sbpr_friend_dict[user] == list():
            for friend in friends:
                friend_items = friend_items.union(user_items[friend])
            friends_items = list(friend_items.difference(user_items[user]))
            sbpr_friend_dict[user] = friends_items
        else:
            friends_items = sbpr_friend_dict[user]
    else:
        friends_items = user_saved_items[user]
    if friends_items:
        random_friend_item = int(random.choice(friends_items))
    else:
        bpr_item = bpr(user,bpr_dict,items,user_items)
        return ([bpr_item,bpr_item])
   
    if sbpr_negative_dict[user] == list(): 
        unseen_items = list(set(items).difference(friend_items.union(user_items[user])))
        sbpr_negative_dict[user] = unseen_items
    else:
        unseen_items = sbpr_negative_dict[user]
    random_item = int(random.choice(unseen_items))
    return (random_friend_item,int(random_item))