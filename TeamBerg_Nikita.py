  
name = "Nikita Shukla"
email = "nikitashukla004@gmail.com"
slack_username = "@Nikita2Chimera"
biostack =  "genomics"
twitter_handle = "@NikitaShukla11"


def hamming_distance(slack_username, twitter_handle):
    c = 0
    j = 0
    while j < len(slack_username):
        if(slack_username[j] != twitter_handle[j]):
            c=c+1
        j=j+1
    return c         
slack_username = "@Nikita2Chimera"
twitter_handle = "@NikitaShukla11"

print(name, email, slack_username, biostack, twitter_handle, hamming_distance(slack_username, twitter_handle))
