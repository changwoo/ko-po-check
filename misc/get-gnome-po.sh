#!/bin/sh
LISTHTML=list.html
LIST=list.txt
DIR=po-gnome

URL1="http://developer.gnome.org/projects/gtp/status/gnome-2.0-core/po/"
URL2="http://developer.gnome.org/projects/gtp/status/gnome-2.0-fifth-toe/po/"
URL3="http://developer.gnome.org/projects/gtp/status/gnome-2.0-extras/po/"

rm -r $DIR
mkdir $DIR

for URL in $URL1 $URL2 $URL3; do
    wget -O $LISTHTML $URL
    grep "HREF=.*ko.po" $LISTHTML | sed -e "s/^.*\"\(.*ko.po\)\".*$/\1/" >$LIST
    rm -f $LISTHTML

    for F in `cat $LIST`; do
	wget -O $DIR/$F $URL/$F
    done
    rm $LIST
done

