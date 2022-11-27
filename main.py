import tweepy

#Credentials
client_id = "CLIENT ID"
client_secret = "CLIENT Secret"
#API key
consumer_key = "FROM API KEY"
#API Key Secret
consumer_secret = "FROM API SECRET"
access_token = "ACCESS TOKEN"
access_token_secret = "ACCESS TOKEN SECRET"
bearer_token = "*******"
# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# Create API object
#api = tweepy.API(auth)

"""   
# using get_user with user name
username = "igrapel"
user = client.get_user(username=username)
print(f"The user name for user name {username} is {user.data.id}.")

# using get_user with id
id = "869660137"
user = client.get_user(id=id)
print(f"The user name for user id {id} is {user.data.name}.")

"""

def exercise1(name):
    # Fetch user data
    # Authentication
    client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)
    user=client.get_user(username=name).data

    # Extract the user id and user name
    user_id = user.id
    user_name = user.name

    # Fetch tweets by the user
    tweets = client.get_users_tweets(id=user_id, tweet_fields=['id', 'text', 'created_at', 'context_annotations'])

    print(f"Here are the recent tweets by {user_name}:\n")

    for tweet in tweets.data:
        print("Id: ", tweet.id)
        print("Author: ", user_name)
        print("Creation Date: ", tweet.created_at)
        print("Text: ", tweet.text)
        #print(tweet.created_at,'\n', tweet.text,"\n", tweet.id,"\n", tweet.text, "\n")

def exercise3(text):
    client = tweepy.Client(consumer_key=consumer_key,
                           consumer_secret=consumer_secret,
                           access_token=access_token,
                           access_token_secret=access_token_secret)
    # Replace the text with whatever you want to Tweet about
    response = client.create_tweet(text=text)
    print(response)

# Driver code
if __name__ == '__main__':
    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.
    exercise3("auth2 testing")
    print("hi")
    exercise1("BBCBreaking")
