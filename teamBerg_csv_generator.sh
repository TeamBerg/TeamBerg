
git clone https://github.com/TeamBerg/TeamBerg.git
cd TeamBerg
echo "gathering information from team "

echo "NAME, EMAIL ADDRESS, SLACK USERNAME, BIOSTACK , TWITTER , HAMMING DISTANCE" > teamBerg.csv
cpp=$(find -iname "*.cpp")
python=$(find . -iname "*[^__].py")
java=$(find -iname "*.java")
R=$(find . -iname "*.R")
js=$(find . -iname "*.js")

repo="$cpp \n $python \n $java \n $R \n $js"
repo=$(echo $repo | tr "\n" "\n")
 
 
for file in $repo
do
    case $file in
 
        *".cpp")
            echo -n "found a c++ extension"
            g++ $file -o compiled_object
            ./compiled_object >> teamBerg.csv
            echo "" >> teamBerg.csv
            echo ""
            echo -n "wrote the c++ content into TeamBerg.csv"
            ;;
            
        *".py")
            echo -n "found a py extension"
            python3 $file >> teamBerg.csv
            echo ""
             echo -n "wrote the python content into TeamBerg.csv"
            ;;
 
        *".java")
            echo -n "found a java extension"
            javac $file
            java TeamBergKelvin >>  teamBerg.csv
            echo ""
            echo -n "wrote the java content into TeamBerg.csv"
            ;;
 
        *".R")
            echo -n "found a R extension"
            Rscript $file >> teamBerg.csv
            echo "" >> teamBerg.csv
            echo ""
            echo -n "wrote the R content into TeamBerg.csv"
            ;;

        *".js")
            echo -n "found a js extension"
            node $file >> teamBerg.csv
            echo ""
            echo -n "wrote the js content into TeamBerg.csv"
            ;;
 
        *)
            echo ""
            ;;
    esac
done
 
echo " "
rm *.class compiled_object
echo ""
 
echo "Successful!!!   Finished  please find the output in teamBerg.csv)"
echo ""


