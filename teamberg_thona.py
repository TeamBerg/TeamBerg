
def task_result(name, email, slack_username, biostack, twitter_handle, hamming_distance):
    print("name: "+ name +"\n" +"email: "+email + "\n" +"slack_username: " + slack_username + "\n" + "biostack: " + biostack + "\n" + "twitter_handle: " + twitter_handle + "\n" + "hamming_distance: " + hamming_distance )
    



def hamming_distance(slack_username, twitter_username):
    counter = 0
    for y in range(len(slack_username)):
        if slack_username[y] !=twitter_username[y]:
            counter+=1
    return str(counter)








if __name__ == '__main__':
  task_result("wusu deborah thona","thonawusu@gmail.com","@debby","drug development","@thonawusu",
  hamming_distance ("@debby","@thonawusu"))