name = "Nirvana Munir"
email = "nirvana.monir66@gmail.com"
slack_username = "@Nirvana"
biostack =  "Drug Development"
twitter_handle = "@Nervana"


def hamming_distance(slack_username, twitter_handle):
    count = 0
    i = 0
    while i < len(slack_username):
        if(slack_username[i] != twitter_handle[i]):
            count += 1
        i += 1
    return count         
slack_username = "@Nirvana"
twitter_handle = "@Nervana"

print(name, email, slack_username, biostack, twitter_handle, hamming_distance(slack_username, twitter_handle)) 
