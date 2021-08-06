#include <iostream>
#include <string>
#include <stdexcept>

using namespace std;

int hammingDistance(string &, string &);
int main(){
    string name = "Barnabas Oretan";
    string email = "barnabas.oretan@gamil.com";
    string biostack= "genomics";
    string slackUsername= "@omimi";
    string twitterHandle= "@Oshola_omimi";
    try{
        int distance = hammingDistance(slackUsername, twitterHandle);
        cout << "name : "<< name << endl;
        cout << "email : "<< email << endl;
        cout << "slack username :  "<< slackUsername << endl;
        cout << "biostack : "<< biostack << endl;
        cout << "twitter handle : "<< twitterHandle << endl;
        cout << "hamming distance :"<< distance << endl;
    }catch (invalid_argument &invalid_argument){
        cout << invalid_argument.what()<< endl;
    }
    return 0;
    
} // namespace std;
int hammingDistance(string & slackUsername, string & twitterHandle){
    int distanceCounter = 0;
    if (slackUsername.length()!= slackUsername.length()){
        throw invalid_argument("your inputs must be of the same length");
    }
    for (size_t i = 0; i < slackUsername.length(); ++i){
        if (slackUsername[i] != twitterHandle[i]){
            ++distanceCounter;
        }
    }
    return distanceCounter;
}
