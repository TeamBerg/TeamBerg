#Rays-Details # stage_zero _assignment
#1. Create strings variable to store the details without Hamming distance
name="Ridwan Shittu"
email="shittuar@gmail.com"
slack_username="@Rays"
biostack= "Data analytics" 
twitter_handle ="@ridwanshittu30"

# 2. Create a function for the Hamming Distance in R
Hamming_distance <- function(a,b){
  A <- strsplit(a, split = "")[[1]]
  B <- strsplit(b, split = "")[[1]]
  C <- sum(A!=B)
  return(C)
}

#3. Print out the details for username:rays with Hamming distance calculated for the slack_username and twitter_handle
details_rays <- list(name=name,email=email, slack_username=slack_username, biostack=biostack, twitter_handle=twitter_handle, Hamming_distance=Hamming_distance(slack_username, twitter_handle))
# print(details_rays)

write.table (details_rays,  sep = ",", row.names=FALSE)
# write.table (details_rays,"details_rays.csv",  sep = ",", row.names=FALSE)

