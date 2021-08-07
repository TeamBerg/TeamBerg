const details = {
    name: "Foluso Ogunfile", 
    email: "fogunfile@gmail.com",
    slack_username: "@fogunfile",
    biostack: "Software Development",
    twitter_handle: "@f_ogunfile",
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
    const abc = Object.values(details).join(", ");
    console.log(abc);
    return abc;
}
printDetails();

