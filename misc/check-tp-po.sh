#!/bin/sh

DIR=po-tp

for PO in $DIR/*.ko.po; do
    ko-po-check $PO
done
