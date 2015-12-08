import tweepy

consumer_key = "LFWvQkfmAC0WQoGAxC2jGOea3";
#eg: consumer_key = "LFWvQkfmAC0WQoGAxC2jGOea3";


consumer_secret = "ZLzQBXdpBY1gERO8du5R2jNs8JQlXpN2VtFJ0nm42sdKBKpe48";
#eg: consumer_secret = "ZLzQBXdpBY1gERO8du5R2jNs8JQlXpN2VtFJ0nm42sdKBKpe48";

access_token = "4489773074-zIsQyDjSSVCwAadtqEEvhKdsCe7t2zHABt65lYc";
#eg: access_token = "4489773074-zIsQyDjSSVCwAadtqEEvhKdsCe7t2zHABt65lYc";

access_token_secret = "Tcto4ynVOSFiqffiadktt4CkjVR1f56Dw9EX15VVH6bnd";
#eg: access_token_secret = "Tcto4ynVOSFiqffiadktt4CkjVR1f56Dw9EX15VVH6bnd";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



