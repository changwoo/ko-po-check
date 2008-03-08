#!/bin/sh
LISTHTML=list.html
LIST=list.txt
DIR=po-gnome

URLLIST="http://l10n.gnome.org/languages/ko/gnome-2-22"
URLBASE="http://l10n.gnome.org/"

rm -r $DIR
mkdir $DIR

for URL in $URLLIST; do
    wget -O $LISTHTML $URL
    grep "href=\".*ko.po\"" $LISTHTML | sed -e "s/^.*\"\(.*ko.po\)\".*$/\1/" >$LIST
    #rm -f $LISTHTML

    for F in `cat $LIST`; do
	(cd $DIR && wget $URLBASE/$F)
    done
    #rm $LIST
done

