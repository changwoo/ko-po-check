#!/bin/sh
LISTHTML=list.html
LIST=list.txt
DIR=po-gnome

URL1="http://developer.gnome.org/projects/gtp/status/gnome-2.4/PO/"

rm -r $DIR
mkdir $DIR

for URL in $URL1; do
    wget -O $LISTHTML $URL
    grep "HREF=.*ko.po" $LISTHTML | sed -e "s/^.*\"\(.*ko.po\)\".*$/\1/" >$LIST
    rm -f $LISTHTML

    for F in `cat $LIST`; do
	wget -O $DIR/$F $URL/$F
    done
    rm $LIST
done

