#Rays-Details # stage_zero _assignment
#1. Create strings variable to store the details without Hamming distance
name="Ridwan Shittu"
email="shittuar@gmail.com"
stack_username="@Rays"
biostack= "Data analytics" 
twitter_handle ="@ridwanshittu30"

#bring all together
details_rays <- c(name, email, stack_username, biostack, twitter_handle)
print(details_rays)

# 2. Create a function for the Hamming Distance in R
Hamming_distance <- function(a,b){
  A <- strsplit(a, split = "")[[1]]
  B <- strsplit(b, split = "")[[1]]
  C <- sum(A!=B)
  return(C)
}

#3. Print out the details for username:rays with Hamming distance calculated for the slack_username and twitter_handle
details_rays <- c(name,email, stack_username, biostack, twitter_handle, Hamming_distance(stack_username, twitter_handle))

print(details_rays)

# # 'Method 2'
# # Without Hamming_distance
# details_rays <- c(name="Ridwan Shittu", email="shittuar@gmail.com", stack_username="@Rays", biostack= "Metagenomics", 
#                   twitter_handle ="@ridwanshittu30")
# 
# # with Hamming_distance
# details_rays <- c(name="Ridwan Shittu", email="shittuar@gmail.com", stack_username="@Rays", biostack= "Metagenomics", 
#                   twitter_handle ="@ridwanshittu30", hamming_distance=Hamming_distance("@Rays", "@ridwanshittu30"))
# print(details_rays)
