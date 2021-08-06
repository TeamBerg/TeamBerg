
library('stringdist')
name <- 'Abdulkabir Ojulari'
email <- 'abdulkabirojulari@gmail.com'
slack <- '@abdulojus'
twitter <- '@ojularias'
biostack <- 'Gnomics'
final <- list(Name= name, Email= email,Slack= slack, Twitter= twitter, Biostack= biostack)
hamming_distance <- stringdist(slack, twitter, method="hamming")
cat("Hamming Distance: ", hamming_distance )
write.csv(final)
