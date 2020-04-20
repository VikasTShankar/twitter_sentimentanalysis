from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt


def percentage(part, whole):
    return 100 * float(part)/float(whole)


consumerKey = "spoWaGIMt93hWbHnMBA54uSkZ"
consumerSecret = "c0JO4tIKKuiCmwYo64uTfkSyx1sBfN0tNytZIn4q5XK0WeWP0z"
accessToken = "1052476492347625472-6h7CvR9XvRzXM6iglPgstZkYJ8q2Vz"
accessTokenSecret = "SxXIuEDC33oA8Tgo2Rp1jkCr74k5kH5Qi2X20Mk73ZQGX"
auth = tweepy.OAuthHandler(consumer_key=consumerKey, consumer_secret=consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

# input for term to be searched and how many tweets to search
searchTerm = input("Enter Keyword/HashTag/Event to search about: ")
NoOfTerms = int(input("Enter how many tweets to search: "))

# searching for tweets
tweets = tweepy.Cursor(api.search, q=searchTerm, lang="en").items(NoOfTerms)

# creating some variables to store info
positive = 0
negative = 0
neutral = 0
polarity = 0


# iterating through tweets fetched
for tweet in tweets:

    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity  # adding up polarities to find the average later

    if analysis.sentiment.polarity == 0:
        neutral += 1
    elif analysis.sentiment.polarity > 0.00:
        positive += 1
    elif analysis.sentiment.polarity < 0.00:
        negative += 1

positive = percentage(positive, NoOfTerms)
negative = percentage(negative, NoOfTerms)
neutral = percentage(neutral, NoOfTerms)

positive = format(positive, '.2f')
negative = format(negative, '.2f')
neutral = format(neutral, '.2f')

print("How people are reacting on " + searchTerm + " by analyzing " + str(NoOfTerms) + " tweets.")
polarity = polarity/NoOfTerms
if polarity == 0:
    print("Neutral")
elif polarity > 0:
    print("Positive")
elif polarity < 0:
    print("Negative")

labels = ['Positive ['+str(positive)+'%]', 'Neutral ['+str(neutral) + '%]', 'Negative ['+str(negative) + '%]']
sizes = [positive, neutral, negative]
colors = ['yellowgreen', 'gold', 'red']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title('How people are reacting on ' + searchTerm + ' by analyzing ' + str(NoOfTerms) + ' Tweets.')
plt.axis('equal')
plt.tight_layout()
plt.show()