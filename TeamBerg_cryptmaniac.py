
def task_output(name, email, slack_username, biostack, twitter_handle, hamming_distance):

    print("name: "+ name + "\n" + "email: " + email + "\n" + "slack_username: " + slack_username + "\n" + "biostack: " + biostack + "\n" + "twitter_handle:  " + twitter_handle + "\n" + "hamming_distance: " + hamming_distance )

def hamming_distance(slack_username, twitter_handle):
    counter = 0
    for w in range(len(slack_username)):
           if slack_username[w] != twitter_handle[w]:
               counter +=1
    return str(counter)

if __name__ == '__main__':
    task_output("Hammed AYANSOLA", "herkolerm@gamil.com", "@Hammed", "genomics", "@Hammedayansola", 
    hamming_distance("@Hammed", "@Hammedayansola"))
    
