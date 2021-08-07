const details = {
    name: "Foluso Ogunfile", 
    email: "fogunfile@gmail.com",
    slack_username: "@fogunfile",
    twitter_handle: "@f_ogunfile",
    biostack: "Software Development",
}

const hammingDistance = (str1, str2) => {
    let count = 0;
    if(str1.length === str2.length){
        let i = 0;
        while(i < str1.length){
            if(str[i] != str2[i]){
                count++;
            }
            i++;
        }
    } else {
        count = -1;
    }
    return count;
};

const printDetails = () => {
    ({slack_username, twitter_handle} = details);
    details.hamming_distance = hammingDistance(slack_username, twitter_handle);
    return Object.values(details).join(", ");
}
printDetails();

