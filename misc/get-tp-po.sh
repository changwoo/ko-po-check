#!/bin/sh
LISTHTML=list.html
LIST=list.txt
DIR=po-tp
URL="http://www.iro.umontreal.ca/contrib/po/teams/PO/ko/"

rm -rf $DIR
mkdir $DIR

wget -O $LISTHTML $URL
grep "HREF=.*ko.po" $LISTHTML | sed -e "s/^.*\"\(.*ko.po\)\".*$/\1/" >$LIST
rm -f $LISTHTML

for F in `cat $LIST`; do
    wget -O $DIR/$F $URL/$F
done
rm $LIST

