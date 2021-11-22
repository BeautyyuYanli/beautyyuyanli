BASEDIR=$(dirname "$0")
cd $BASEDIR
CWD=$PWD

sh $CWD/components/update.sh
python3 $CWD/generate_readme.py

cd $CWD
git add .
git commit -m "update all"
git push -f origin master