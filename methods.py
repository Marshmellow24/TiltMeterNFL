import praw
import string, contractions
import yaml, csv

# constant for default config file 
CONFIG = "config.yml"

# read config file and return yaml obj
def get_config(filename):
    with open(filename, "r") as file:
        api_credentials = yaml.safe_load(file)
    return api_credentials

# read file for inference
def loadCSV(filename):
    with open(filename, "r") as file:
        prepared_comments = csv.reader(file, delimiter=";")
    return prepared_comments

# hook up to Reddit API
def reddit_api(config = CONFIG):
    parsed_config = get_config(config)

    client_id = parsed_config["reddit_api"]["client_id"]
    client_sec = parsed_config["reddit_api"]["client_secret"] 
    pw = parsed_config["reddit_api"]["password"] 
    user_agt = parsed_config["reddit_api"]["user_agent"] 
    usern = parsed_config["reddit_api"]["username"]

    reddit = praw.Reddit(client_id = client_id,
                     client_secret = client_sec, password = pw,
                     user_agent = user_agt, username = usern)
    return reddit

# clean output, removes uppercases, contractions, whitespaces, punctuation
def cleanser(input):
    output_list = []
    for comment in input:
        comment = comment.lower()
        comment = contractions.fix(comment)
        comment = comment.translate(str.maketrans("","", string.punctuation))
        comment = " ".join(comment.split())
        output_list.append(comment)
    return output_list

# parse through non-deleted/removed comments until count is reached
def parseComments(comments, count):
    buffer = []
    deleted = ["[deleted]", "[removed]", "[gelöscht]", "[entfernt]"]
    
    for comment in comments:
        if comment.body not in deleted:
            buffer.append(comment.body)
        if len(buffer) == count:
            break  
    
    return buffer 

if __name__ == "main":
    pass