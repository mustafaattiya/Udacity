# Check profanity in a text file

import urllib
import urllib.request
import urllib.parse

# Python 3.6.4

# Read a text file
def read_text():
    path = "/Users/mustafa/Documents/Office Corner/CV's/Forex Job Description.txt"
    file = open(path, "r", encoding="utf-8") 
    file_contents = file.read()
    #print(file_contents)
    file.close()
    check_profanity(file_contents) # Added after creating the "check_profanity" function

        
def check_profanity(text):
        
    site_url = "http://www.wdylike.appspot.com/?"

    file_contents_in_url = urllib.parse.urlencode({'q' : text})

    check = site_url + file_contents_in_url
    #print(check)

    url = urllib.request.urlopen(check)
    url_bytes = url.read()
    #print(url_bytes)

    site_url_contents = url_bytes.decode("utf8")
    #print("\n""Profanity result: ""\n" + site_url_contents)

    if "true" in site_url_contents:
        print("PROFANITY ALERT!!!")
    elif "false" in site_url_contents:
        print("Crystal Clear")


read_text()

