import praw

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from collections import Counter

from nltk.sentiment import SentimentIntensityAnalyzer

from wordcloud import WordCloud

# Reddit API credentials

client_id = ""

client_secret = ""

username = ""

password = ""

# Initialize Reddit instance

reddit = praw.Reddit(

    client_id=client_id,

    client_secret=client_secret,

    username=username,

    password=password,

    user_agent="Comment Extraction",

)

# Set the program parameters

limit = 500      # define the limit

upvotes = 5     # define # of upvotes, comment is considered if upvotes exceed this #

picks = 10     # define # of picks here, prints as "Top ## picks are:"

picks_ayz = 5   # define # of picks for sentiment analysis

subreddit_name = "wallstreetbets"

post_flairs = ['Daily Discussion', 'Weekend Discussion', 'Discussion']    # posts flairs to search

# Initialize sentiment analyzer

sia = SentimentIntensityAnalyzer()

# Extract data from subreddit

subreddit = reddit.subreddit(subreddit_name)

posts = []

for submission in subreddit.hot(limit=limit):

    if submission.link_flair_text in post_flairs:

        submission.comments.replace_more(limit=0)

        for comment in submission.comments:

            if comment.score > upvotes:

                for word in comment.body.split():

                    if word.startswith("$") and word[1:].isalpha() and len(word) <= 5:

                        posts.append({

                            "title": submission.title,

                            "body": comment.body,

                            "score": comment.score,

                            "symbol": word[1:].upper(),

                            "sentiment": sia.polarity_scores(comment.body)["compound"],

                        })

# Convert data to pandas DataFrame

df = pd.DataFrame(posts)

# Count symbols and sentiment for each symbol

symbol_counts = Counter(df["symbol"])

sentiment_counts = df.groupby("symbol")["sentiment"].mean().sort_values(ascending=False)

# Print top picks

print(f"Top {picks} mentioned picks:")

for symbol, count in symbol_counts.most_common(picks):

    print(f"{symbol}: {count}")

# Plot symbol counts as word cloud

wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(symbol_counts)

plt.figure(figsize=(16, 8))

plt.imshow(wordcloud, interpolation="bilinear")

plt.axis("off")

plt.title(f"{picks} most mentioned picks")

plt.show()

# Plot sentiment counts as bar chart

plt.figure(figsize=(16, 8))

sns.barplot(x=sentiment_counts.values, y=sentiment_counts.index, color="blue")

plt.title(f"Sentiment analysis of top {picks_ayz} picks")

plt.xlabel("Sentiment score (compound)")

plt.ylabel("Stock symbol")

plt.show()

