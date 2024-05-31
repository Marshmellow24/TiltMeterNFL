import pandas
from methods import cleanser, reddit_api, parseComments

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

# for hot in hot_nfl:
#     if not hot.stickied:
#         print(hot.title)

#         comments = hot.comments
#         for comment in comments[:10]:
#             # print(15*"-")
#             # print(comment.body)
#             buffer_list.append(comment.body)

# output = cleanser(buffer_list)


# df = pandas.DataFrame(output)

# df = df.set_axis(["comment"], axis=1)
# df.to_csv("test_comments.csv", ";")
# df.style.set_properties(**{'text-align': 'left'})
# df.style.set_properties(**{'white-space': 'nowrap'})
# print(df.to_string(justify="left", max_colwidth=100, line_width=50, index=False))

# print(output)

# print(df.iloc[[1]])

# df.style.set_properties(**{'text-align': 'left'})


