# Security
# ssrf.php
Simple file that allows user to test ssrf vulnerability in file uploaders on websites.<br />
To use it try to upload this file to server. If you are able to retrieve it from server then try to use c parameter like this:<br />
*www.example.com/content/ssrf.php?c=whoami* <br />
If in response you will receive something like *www-data* then you are able to perform commands on server side. <br />

# urlEncode.py
Simple script to encode urls. You can run it like this: <br />
*python ./urlEncode.py "url to encode"*

# dependenciesRecon.js
Simple script that automates basic dependecies recon on websites in browser. It is designed to be used in chrome/opera console.
To use it just copy paste it to the browser's console on website you want to check.
