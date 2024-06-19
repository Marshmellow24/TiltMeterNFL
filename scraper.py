import pandas
from utils import cleanser, reddit_api, parseComments

# initialize API w/ credentials
reddit = reddit_api()

print(reddit.user.me())

# get subreddit game thread 
submission = reddit.submission("16l9gh6")

# get 100 comments of submission
parsed_output = parseComments(submission.comments, 100)

# clean data
cleaned_output = cleanser(parsed_output)

# convert to df
comments_clean = pandas.DataFrame(cleaned_output)

# save as csv to subfolder 'Jets'
comments_clean.to_csv("Jets/week2.csv", sep=";", header=False)

print("done")

