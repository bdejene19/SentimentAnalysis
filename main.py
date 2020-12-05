#
#
#
from sentiment_analysis import compute_tweets

# ask for user input to determine analysis
fileName = input("Enter the name of your file: ")
keyword_fileName = input("Enter the name of your keywords list file: ")

file_analysis = compute_tweets(fileName, keyword_fileName)

# printing readable version of data to 3 decimals for each region
print("\nEastern Data")
print("Average happiness: %.3f" % file_analysis[0][0])
print("Number of key tweets: ", file_analysis[0][1])
print("Number of Eastern tweets: ", file_analysis[0][2])
print()

print("Central Data")
print("Average happiness: %.3f " % file_analysis[1][0])
print("Number of key tweets: ", file_analysis[1][1])
print("Number of Eastern tweets: ", file_analysis[1][2])
print()

print("Mountain Data")
print("Average happiness: %.3f" % file_analysis[2][0])
print("Number of key tweets: ", file_analysis[2][1])
print("Number of Eastern tweets: ", file_analysis[2][2])
print()

print("Pacific Data")
print("Average happiness: %.3f " % file_analysis[3][0])
print("Number of key tweets: ", file_analysis[3][1])
print("Number of Eastern tweets: ", file_analysis[3][2])
