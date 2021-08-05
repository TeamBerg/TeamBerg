
def task_output(name, email, slack_username, biostack, twitter_handle, hamming_distance):
  print("name: "+ name + "\n" +"email: "+ email + "\n" +"slack_username: "+ slack_username+ "\n"+"biosatck: "+ biostack + "\n" + "twitter_handle: "+ twitter_handle + "\n" + "hamming_distance: "+ hamming_distance )


def hamming_distance(slack_username, twitter_username):
    counter = 0
    for x in range(len(slack_username)):
        if slack_username[x] != twitter_username[x]:
            counter+=1
    return str(counter)




if __name__ == '__main__':
    task_output("barnabas oretan","barnabas.oretan@gmail.com","@omimi","genomics","@Oshola_omimi",
    hamming_distance("@omimi", "@Oshola_omimi"))