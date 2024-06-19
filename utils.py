import praw
import string, contractions
import yaml, csv
import pandas as pd

# constant for default config file 
CONFIG = "config.yml"

# read config file and return yaml obj
def get_config(filename):
    with open(filename, "r") as file:
        api_credentials = yaml.safe_load(file)
    return api_credentials

# read csv file and transform into df
def loadCSV2DF(filename):
    with open(filename, "r", encoding="utf-8") as file:
        output = pd.read_csv(file, sep = ";", usecols=[1], skip_blank_lines=True, header=0)
    return output

# read csv file
def loadCSV(filename):
    output = []
    with open(filename, "r", encoding="utf-8") as file:
        f = csv.reader(file, delimiter=";", skipinitialspace=True)
        for row in f:
            output.append(row)
    return output[1:]

# get model info from csv
def getModel(index, file):
    df = pd.read_csv(file,  sep=";")
    task = df.loc[index,:]["task"]
    model = df.loc[index,:]["model"]
    file_name = df.loc[index,:]["file_name"]
    
    return task, model, file_name

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

# parse through cleanec non-deleted/removed comments until count is reached
def parseComments(comments, count):
    buffer = []
    deleted = ["[deleted]", "[removed]", "[gelöscht]", "[entfernt]"]
    
    for comment in comments:
        if comment.body not in deleted:
            buffer.append(comment.body)
        if len(buffer) == count:
            break  
    
    return buffer 

def convertDF(input):
    pdf = pd.DataFrame(input)
    return pdf

if __name__ == "__main__":
    pass