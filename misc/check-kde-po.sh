#!/bin/sh

DIR=po-kde

for PO in $DIR/*.po; do
    ko-po-check $PO
done
