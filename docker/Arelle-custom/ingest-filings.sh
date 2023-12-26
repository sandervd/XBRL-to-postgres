#!/bin/bash
cd filings
for f in ./*.zip; do
       echo "Processing $f file...";
       python ../arelleCmdLine.py -f $f -v --plugins "xbrlDB" --store-to-XBRL-DB 'postgres,5432,postgres,arelle_pwd,arelle_db,10,pgOpenDB'
done
