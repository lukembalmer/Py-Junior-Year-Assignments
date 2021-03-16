#record the frequency of words in a song's lyrics

def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

def string_to_list(songstr):
    songstr = songstr.lower()
    lyrics = songstr.split()
    return lyrics

lyrics = string_to_list("Happy Birthday to You Happy Birthday to You Happy Birthday Dear Luke Happy Birthday to You")

print(lyrics_to_frequencies(lyrics))