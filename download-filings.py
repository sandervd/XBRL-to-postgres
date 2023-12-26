#!/bin/env python3
import json
import requests
import os

filings_json = 'filings-gb.json'
if not os.path.isfile(filings_json):
    filings_data = requests.get("https://filings.xbrl.org/api/filings?include=entity,language&filter=[{%22name%22%3A%22country%22%2C%22op%22%3A%22eq%22%2C%22val%22%3A%22GB%22}%2C{%22name%22%3A%22input_filing.filing_source.program%22%2C%22op%22%3A%22eq%22%2C%22val%22%3A%22ESEF%22}]&sort=-date_added&page[size]=1000&page[number]=1&_=1703595090227")
    open(filings_json, 'wb').write(filings_data.content)

f = open(filings_json)
data = json.load(f)
for filing in data['data']:
    file_path = 'filings/' + filing['attributes']['fxo_id'] + '.zip'
    if not os.path.isfile(file_path):
        zipfile = requests.get("https://filings.xbrl.org" + filing['attributes']['package_url'])
        open(file_path, 'wb').write(zipfile.content)
f.close()
