#!/bin/sh

LISTHTML=list.html
LIST=list.txt
DIR=po-tp
DIRURL="http://www.iro.umontreal.ca/contrib/po/teams/PO/ko/"
URL="http://www.iro.umontreal.ca/contrib/po/teams/PO/ko/?M=D"

rm -rf $DIR
mkdir $DIR

wget -O $LISTHTML $URL
grep "HREF=.*ko.po" $LISTHTML | sed -e "s/^.*\"\(.*ko.po\)\".*$/\1/" > $LIST
rm -f $LISTHTML

for F in `cat $LIST`; do
    DOMAIN=`echo $F|sed -e "s/^\(.*\)-.*$/\1/"`
    if eval "test x\$HAS_$DOMAIN != x1"; then
	echo "*** Getting $F..."
	wget -O $DIR/$F $DIRURL/$F
    else
	echo "*** Skipping old $F..."
    fi
    eval "HAS_$DOMAIN=1"
done

rm $LIST

