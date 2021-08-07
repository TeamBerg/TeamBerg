public class TeamBergKelvin {
    public TeamBergKelvin() {
    }

    public static void main(String[] var0) {
        String var1 = "Kelvin Okoro";
        String var2 = "okorokelvinemoakpo@yahoo.com";
        String var3 = "@Kelvin";
        String var4 = "Genomics";
        String var5 = "@Kel4kelvin";
        System.out.println(var1 + "," + var2 + "," + var3 + "," + var5 + "," + var4 + "," + hammingDistance(var3, var5));
    }

    private static int hammingDistance(String var0, String var1) {
        int var2 = 0;

        int var3;
        for(var3 = 0; var2 < var0.length(); ++var2) {
            if (var0.charAt(var2) != var1.charAt(var2)) {
                ++var3;
            }
        }

        return var3;
    }
}

