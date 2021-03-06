'''
Courses Alert version 2.0
This script look for and alert you about free courses on Techcracked.com and freeonlinecourses.xyz
with your keywords
By N0vachr0n0 & Comsavvy
'''

from bs4 import BeautifulSoup
import requests
import easygui
import time
import webbrowser

titre_cours = [[],[]]
button = ["CHECK","OK"]

# This is example of keywords
keywords = ["Android", "IoT", "Ethical", "Machine", "Mobile", "AI", "Python", "Flutter", "Ios", "AWS", "Kali",
            "Complete", "OWASP"]
print("Courses Alert is running ...")


def cooking(url_, name_class, id):
    global titre_cours
    new = 0
    courses = []
    resp = requests.get(url_).text
    soup = BeautifulSoup(resp, "lxml")

# Checking new courses
    for art in soup.find_all(class_=name_class, limit=3):
        if art.get_text() not in titre_cours:
            titre_cours[id].append(art.get_text())
            new = 1
            if len(titre_cours) > 4:
                del (titre_cours[id][3])

    # Verifying whether keywords match with a new course
    if new == 1:
        for j in range(len(titre_cours[id])):
            for i in range(len(keywords)):
                if keywords[i] in titre_cours[id][j]:
                    if titre_cours[id][j] not in courses:
                        courses.append(titre_cours[id][j])
        new = 0
    for i in range(len(courses)):
        choice = easygui.buttonbox(f"{courses[i]}\n\nSource: {url_}", "NEW COURSES !", button)
        if choice == button[0]:
            webbrowser.open_new(f"{url_}")

if __name__ == '__main__':
    while True:
        cooking("https://www.techcracked.com/", "post-title", 0)
        cooking("https://www.freshercooker.in/", "entry-title td-module-title", 1)  # Checking only in Hacking session
        time.sleep(14400)  # Waiting 4 hours to check again
