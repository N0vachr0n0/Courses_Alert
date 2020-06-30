'''
Courses Alert version 1.0

This script look for and alert you about free courses on Techcracked.com and freeonlinecourses.xyz
with your keywords

By N0vachr0n0

'''

from bs4 import BeautifulSoup
import requests
import easygui
import time

titre_cours = []
new = 0
# This is example of keywords
keywords = ["Android", "IoT", "Ethical", "Machine", "Mobile", "AI", "Python", "Flutter", "Ios", "AWS", "Kali",
            "Complete", "OWASP"]

print("Courses Alert is running ...")


def cooking(url_, name_class):
    resp = requests.get(url_)
    soup = BeautifulSoup(resp.text, "lxml")

    # Checking new courses
    for art in soup.find_all("h2", class_=name_class, limit=3):
        if art.get_text not in titre_cours:
            titre_cours.append(art.get_text())
            new = 1
            if titre_cours.__len__() > 4:
                del (titre_cours[3])

    # Verifying whether keywords match with a new course
    if new == 1:
      for i in range(keywords.__len__()):
          for y in range(titre_cours.__len__()):
              if keywords[i - 1] in titre_cours[y - 1]:
                  easygui.msgbox("{}\nSource:- {}".format(titre_cours[y - 1], url_), title="NEW COURSES !")
                  new = 0


if __name__ == '__main__':
    while 1:
        cooking("https://www.techcracked.com/", "post-title")
        cooking("https://freeonlinecourses.xyz/category/hacking/", "entry-title")  # Checking only in Hacking session
        time.sleep(14400)  # Waiting 4 hours to check again
