#
# Program made by Bemnet Dejene
# This program takes 2 files: a tweet file to analyze, and the other keywords with an associated value
# the program goes through first file line by line to determine  the region the tweet was made in
# after doing so, it then analyzes the tweet word by word to see if the tweet has any keywords found described in our second file for the compute_tweet function
# if a key word is found, its associated value is added so that a tweet happiness can be calculated
# the result of this function is average happiness, # of key tweets, and # of total tweets of the regions Eastern, Central, Mountain, and Pacific

# import needed for later to remove unwanted characters
import re

# time_zones function sorts tweets into respective regions based on their latitude and longitude
def time_zones(lat, long):
    if (lat <= 49.189787) and (lat >= 24.660845) and (long > -87.518395) and (long <= -67.444574):
        return "Eastern"

    elif (lat <= 49.189787) and (lat >= 24.660845) and (long > -101.998892) and (long <= -87.518395):
        return "Central"

    elif (lat <= 49.189787) and (lat >= 24.660845) and (long > -115.236428) and (long <= -101.998892):
        return "Mountain"

    elif (lat <= 49.189787) and (lat >= 24.660845) and (long >= -125.242264) and (long <= -115.236428):
        return "Pacific"

# compute_tweets function is the one that generates the data
def compute_tweets(tweets, keywordlist):
    # create empty dictionary to form a dictionary for keyword list
    dictionary = {}

    try:
        tweets = open(tweets, 'r', encoding="UTF-8")
        keywordlist = open(keywordlist, 'r', encoding="UTF-8")

    # error raised when file unable to be found since it does not exist
    except FileExistsError:
        FileExistsError("File does not exist.")

    done = False
    eastern_tweets = 0
    eastern_keytweets = 0
    eastern_tweetscores = []

    central_tweets = 0
    central_keytweets = 0
    central_tweetscores = []

    mountain_tweets = 0
    mountain_keytweets = 0
    mountain_tweetscores = []

    pacific_tweets = 0
    pacific_keytweets = 0
    pacific_tweetscores = []

    # stripping keywordlist to bare bones --> no white spaces
    for myvalues in keywordlist:
        keywordlist = myvalues.rstrip("\n")
        keywordlist = keywordlist.split(",")
        # now turn keyword list into dictionary
        dictionary[keywordlist[0]] = keywordlist[1]

    while not done:
        # analyzing line first by breaking it up into individual words
        for line in tweets:
            line = line.lower()
            elements = line.split()
            regenerated_list = []

            # assigning latitude and longitude values to the tweets index values
            lat = elements[0]
            long = elements[1]

            lat = lat.strip("[,")
            long = long.strip(']')

            lat = float(lat)
            long = float(long)
            # call time zone function to sort into regions
            tweet_timezones = time_zones(lat, long)

            # only want to analyze actual string tweet, not latitude, longitude, time, etc., so it is regenerated
            for number in range(5, len(elements)):
                elements[number] = re.sub(r'\W+', '', elements[number])
                regenerated_list.append(elements[number])

            if tweet_timezones == "Eastern":
                eastern_tweets += 1
                happywords_valuetotal = 0
                num_keywords = 0

                # now analzying word by word in tweet
                for Ekey_words in regenerated_list:
                    # check to see if word in tweet is found in my dictionary
                    if Ekey_words in dictionary.keys():
                        num_keywords += 1
                        happywords_valuetotal += int(dictionary[Ekey_words])

                # if there are any keywords, increase eastern key tweets by 1
                if num_keywords > 0:
                    eastern_keytweets += 1

                if num_keywords != 0:
                    Etweetscore = happywords_valuetotal / num_keywords
                    # add score tweet score to list containing scores for all tweets in this region
                    eastern_tweetscores.append(Etweetscore)

            # do the same thing with Central, Mountain, and Pacific regions
            elif tweet_timezones == "Central":
                central_tweets += 1
                happywords_valuetotal = 0
                num_keywords = 0
                for Ckey_words in regenerated_list:
                    if Ckey_words in dictionary.keys():
                        num_keywords += 1
                        happywords_valuetotal += int(dictionary[Ckey_words])

                if num_keywords > 0:
                    central_keytweets += 1

                if num_keywords != 0:
                    Ctweetscore = (happywords_valuetotal/num_keywords)
                    central_tweetscores.append(Ctweetscore)

            elif tweet_timezones == "Mountain":
                mountain_tweets += 1
                happywords_valuetotal = 0
                num_keywords = 0
                for Mkey_words in regenerated_list:
                    if Mkey_words in dictionary.keys():
                        num_keywords += 1
                        happywords_valuetotal += int(dictionary[Mkey_words])

                if num_keywords > 0:
                    mountain_keytweets += 1

                if num_keywords != 0:
                    Mtweetscore = (happywords_valuetotal / num_keywords)
                    mountain_tweetscores.append(Mtweetscore)

            elif tweet_timezones == "Pacific":
                pacific_tweets += 1
                happywords_valuetotal = 0
                num_keywords = 0
                for Pkey_words in regenerated_list:
                    if Pkey_words in dictionary.keys():
                        num_keywords += 1
                        happywords_valuetotal += int(dictionary[Pkey_words])

                if num_keywords > 0:
                    pacific_keytweets += 1

                if num_keywords != 0:
                    Ptweetscore = happywords_valuetotal / num_keywords
                    pacific_tweetscores.append(Ptweetscore)

        # check to see if you are dividing by 0 by seeing if their are any key tweets in that region
        if eastern_keytweets != 0:
            eastern_avghapp = sum(eastern_tweetscores) / eastern_keytweets

        else:
            eastern_avghapp = 0

        if central_keytweets != 0:
            central_avghapp = sum(central_tweetscores) / central_keytweets

        else:
            central_avghapp = 0

        if mountain_keytweets != 0:
            mountain_avghapp = sum(mountain_tweetscores) / mountain_keytweets

        else:
            mountain_avghapp = 0

        if pacific_keytweets != 0:
            pacific_avghapp = sum(pacific_tweetscores) / pacific_keytweets

        else:
            pacific_avghapp = 0

        # set a variable for each region to tuple variables of interest; average happines, # of key tweets in region, and # of tweets in region
        east_data = (eastern_avghapp, eastern_keytweets, eastern_tweets)
        central_data = (central_avghapp, central_keytweets, central_tweets)
        mountain_data = (mountain_avghapp, mountain_keytweets, mountain_tweets)
        pacific_data = (pacific_avghapp, pacific_keytweets, pacific_tweets)

        return east_data, central_data, mountain_data, pacific_data


