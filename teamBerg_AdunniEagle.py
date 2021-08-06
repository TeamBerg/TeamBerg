# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def hamming_distance(slack_username, twitter_username) -> int:
    distance_counter = 0
    for n in range(len(slack_username)):
        if slack_username[n] != twitter_username[n]:
            distance_counter += 1
    return distance_counter


def task_one(name, email, slack_handle, bio_stack, twitter_handle, hamming_distance):
    print("name: " + name + "\n"
                            "email: " + email + "\n"
                                                "slack_handle: " + slack_handle + "\n"
                                                                                  "biostack: " + bio_stack + "\n"
                                                                                                             "twitter_handle: " + twitter_handle + "\n"
                                                                                                                                                   "hamming_distance: " + hamming_distance + "\n")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hamming_distance = str(hamming_distance("@AdunniEagle", "@Wealthysdot"))
    task_one("Sobambo Adedotun", "sobamboadedotun@gmail.com", "AdunniEagle", "Genomics", "wealthysdot", hamming_distance)
