import requests
from bs4 import BeautifulSoup

'''-----------------------------------------Step One - Getting to the links--------------------------------------------'''
def fetch_professors(course, course_number):
    course = course.upper()
    url = f"https://www.coursicle.com/binghamton/courses/{course}/{course_number}"
    return url

url = fetch_professors(input("Subject: "), input("Course Number: "))      # Change when necessary

def write_info():
    response = requests.get(url)
    with open("info.html", "w", encoding="utf-8") as f:
        f.write(response.text)

# Call write_info for each new website grab: 
write_info()

with open("info.html", "r", encoding="utf-8") as f:
    content = f.read()

soup = BeautifulSoup(content, "html.parser")
div = soup.find_all(attrs={"class": "professorLink"})
professor_links = []
professor_names = []
score_list = []

for links in div:
    professor_links.append(links.get('href'))
    professor_names.append(links.string)

'''----------------------------------Step Two - Getting Each Professor's Rating -----------------------------------------------'''

number = 0
def write_prof(list_index):
    prof_response = requests.get(professor_links[list_index])
    with open("prof_info.html", "w", encoding="utf-8") as f:
        f.write(prof_response.text)

for _ in range(len(professor_links)):
    write_prof(list_index=number)
    with open("prof_info.html", "r", encoding="utf-8") as f:
        content_prof = f.read()

    soup = BeautifulSoup(content_prof, "html.parser")
    div = soup.find_all(attrs={"class": "favoritesRatingNumber"})    
    if len(div) != 0:
        for score in div:
            score_list.append(score.string)
    else: 
        score_list.append("Score not given")
    number += 1

for rows in range(len(professor_names)):
    print(f'{professor_links[rows]} <> {professor_names[rows]} : {score_list[rows]}')
    
### If Doesn't work, due to captcha issue ###