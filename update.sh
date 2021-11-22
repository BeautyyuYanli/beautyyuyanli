BASEDIR=$(dirname "$0")
cd $BASEDIR
CWD=$PWD

sh $CWD/components/update.sh
python3 $CWD/generate_readme.py

cd $CWD
git add .
git commit -m "update: $(date + '%Y/%m/%d %T')"
git push -f origin master
