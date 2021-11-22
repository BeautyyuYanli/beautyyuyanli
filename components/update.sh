BASEDIR=$(dirname "$0")
cd $BASEDIR/music
python3 main.py
python3 generator.py
cd $BASEDIR
git add .
git commit -m "update components"
git push -f origin master