#!/bin/sh

DIR=po-gnome

for PO in $DIR/*.ko.po; do
    ko-po-check $PO
done
