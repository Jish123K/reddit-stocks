# reddit-stocks
This is a Python code that uses the Reddit API and several libraries to extract and analyze comments from the WallStreetBets subreddit. The code performs the following tasks:

Initializes the Reddit instance with user credentials

Sets program parameters, such as limit, upvotes, and picks

Initializes a sentiment analyzer

Extracts data from the subreddit by searching for posts with specific flairs and comments with a score greater than the defined upvotes threshold

Filters out comments that do not contain valid stock symbols

Converts the extracted data to a pandas DataFrame

Counts the frequency of each stock symbol and calculates the sentiment score for each symbol

Prints the top mentioned stock symbols and plots them as a word cloud

Plots the sentiment scores of the top picks as a horizontal bar chart.

The code uses the following libraries:

praw: Python Reddit API Wrapper, used to extract data from Reddit

pandas: data manipulation library, used to convert extracted data to a DataFrame

matplotlib: data visualization library, used to create the word cloud and bar chart

seaborn: data visualization library, used to create the horizontal bar chart

collections: Python built-in library, used to count the frequency of stock symbols

nltk: Natural Language Toolkit, used to perform sentiment analysis on comments

wordcloud: data visualization library, used to create the word cloud.
