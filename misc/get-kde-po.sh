#!/bin/sh

URL_HEAD=ftp://ftp.kde.or.kr/KDE/distributions/kde-i18n-ko.tar.bz2
URL_3_0=ftp://ftp.kde.or.kr/KDE/distributions/kde-i18n-ko-3.0-branch.tar.bz2
URL_2_2=ftp://ftp.kde.or.kr/KDE/distributions/kde-i18n-ko-2.2-branch.tar.bz2
OUTFILE=temp.tar.bz2

DIR=po-kde
URL=$URL_3_0

if [ $# -gt 1 ]; then
    if [ $1 = 'HEAD' ]; then
	DIR=po-kde
	URL=$URL_HEAD
    elif [ $1 = '3.0' ]; then
	DIR=po-kde-3.0
	URL=$URL_3_0
    elif [ $1 = '2.0' ]; then
	DIR=po-kde-2.2
	URL=$URL_2_2
    fi
fi

rm -rf $DIR
mkdir $DIR
wget -O $DIR/$OUTFILE $URL

(cd $DIR; tar jxvf $OUTFILE)
rm -f $DIR/$OUTFILE

find $DIR -name "*.po" -exec mv "{}" $DIR \;
rm -r $DIR/kde-i18n-ko-*/