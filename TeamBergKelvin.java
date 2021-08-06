public class TeamBergKelvin {
    public static void main(String[] args) {
        String name = "Kelvin Okoro";
        String email= "okorokelvinemoakpo@yahoo.com";
        String slackUsername = "@Kelvin";
        String biostack = "Genomics";
        String twitterHandle= "@Kel4kelvin";

        System.out.println(name+" "+email+ " "+slackUsername+" "+twitterHandle+" " +biostack+" " + hammingDistance(slackUsername,twitterHandle));

    }

    private static int hammingDistance(String slackUsername, String twitterHandle)
    {
        int i = 0, count = 0;
        while (i < slackUsername.length())
        {
            if (slackUsername.charAt(i) != twitterHandle.charAt(i))
                count++;
            i++;
        }
        return count;
    }

}
