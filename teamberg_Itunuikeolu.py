from scipy.spatial.distance import hamming
name = 'Itunu Bisayo ABODERIN'
email_address = 'itunubisayo@gmail.com'
slack_username = '@Itunuikeolu'
biostack = 'Public health and Genomic Epidemiology'
twitter_handle = '@ItunuBisayo'
print(name)
print(email_address)
print(slack_username)
print(biostack)
print(twitter_handle)
# Calculate hamming distance
# define arrays
str1 = ['@', 'I', 't', 'u', 'n', 'u', 'i', 'k', 'e', 'o', 'l', 'u']
str2 = ['@', 'I', 't', 'u', 'n', 'u', 'B', 'i', 's', 'a', 'y', 'o']
# calculate Hamming distance between the two arrays
hamming_distance = hamming(str1, str2) * len(str1)
print(hamming_distance)
