import json
import os
import nltk
import string
from text_preprocessing import *
from tqdm import tqdm

#returns a list of the 25 tweeter users
def get_users():
    path = "/Users/emilyyu/Desktop/Exercises/final_project_json"
    tweeters = []
    for file in os.listdir(f"{path}"):
        if file.endswith(".json"):
            tweeters.append(os.path.splitext(file)[0])
    return tweeters

#returns a list of strings of clean words of the tweet
def clean_tweet(tweet):
    tweet = remove_URL(tweet)
    tweet = replace_contractions(tweet)
    words = nltk.word_tokenize(tweet)
    words = normalize(words)
    return words

#returns a list of the users tweets
def get_user_tweets(user):
    user_tweets = []
    path = "/Users/emilyyu/Desktop/Exercises/final_project_json"
    with open(f"/Users/emilyyu/Desktop/Exercises/final_project_json/{user}.json") as f:
        dictionary = json.load(f)
        for i in range(len(dictionary)):
            if 'data' in dictionary[i]:
                for j in range(len(dictionary[i]['data'])):
                    tweet = dictionary[i]['data'][j]['text']
                    tweet = clean_tweet(tweet)
                    if len(tweet) != 0:
                        user_tweets.append(tweet)
    return user_tweets

#returns a dictionary of keys: tweeter users, value: list of the users tweets
def get_tweets(user_dictionary):
    tweeters = get_users()
    for user in tqdm(tweeters):
        tweet_list = get_user_tweets(user)
        user_dictionary[user] = tweet_list
    return user_dictionary


def all_words():
    all_words = set()
    with open(f"/Users/emilyyu/Desktop/Exercises/guessthetweeter/tweeter_dictionary.json") as f:
        dictionary = json.load(f)
        #iterating through each user
        for user in dictionary:
            #iterating through each tweet of the user
            for tweets in dictionary[user]:
                #iterating through every word of the tweet
                for word in tweets:
                    all_words.add(word)
    return all_words 

def get_tuples():
    list_tuples = []
    with open(f"/Users/emilyyu/Desktop/Exercises/guessthetweeter/tweeter_dictionary.json") as f:
        dictionary = json.load(f)
        for user in dictionary:
            for tweet in dictionary[user]:
                #making the tweet a string
                string_tweet = ""
                for word in tweet:
                    string_tweet += word + " "
                user_tuple = (user, string_tweet)
                list_tuples.append(user_tuple)
    return list_tuples
    

def create_dataframe(all_words, list_tuples):
    data = pd.DataFrame(dictionary.values(), columns = all_words, index = list_tuples)
    #DATA MAKE DICTIONARY 
    #INDEX = LIST OF THE TUPLES
    #print(data)
    #data.to_csv("/Users/emilyyu/Desktop/Exercises/guessthetweeter/tweeter_matrix.csv")


def main():
    #print(all_words())
    print(get_tuples()[500])
    #all_words = {}
    #all_words = all_words(all_words, user_dictionary)
    #print(all_words)

    #print(get_user_tweets('@barackobama')) 
    #user_dictionary = {}
    #user_dictionary = get_tweets(user_dictionary)

    #Saved to a JSON FILE TO WORK ON EASIER
    #with open("/Users/emilyyu/Desktop/Exercises/guessthetweeter/tweeter_dictionary.json", "w") as write_file:
        #json.dump(user_dictionary, write_file, indent=4)
    
if __name__ == "__main__":
    main()

#Understanding the JSON
#keys: data (contain all the tweets), meta (tells other information)
#dictionary[0] 1/30 tweets
#dictionary[0]['data'][0] 0-99 100 tweets in a dictionary
#dictionary[0]['data'] data from every dictionary
#(dictionary[0]['data'][0]['text']) Tweet from every dictionary print(dictionary[0]['data'][0]['text'])