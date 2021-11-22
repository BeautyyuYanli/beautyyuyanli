BASEDIR=$(dirname "$0")
cd $BASEDIR
CWD=$PWD

cd $CWD/music
proxychains python3 main.py

cp $CWD/music/lib -r $CWD/dance
cd $CWD/dance
proxychains python3 main.py