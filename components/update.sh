BASEDIR=$(dirname "$0")
cd $BASEDIR
CWD=$PWD

cd $CWD/music
proxychains python3 main.py

cd $CWD/dance
proxychains python3 main.py


cd $CWD
git add .
git commit -m "update components"
git push -f origin master