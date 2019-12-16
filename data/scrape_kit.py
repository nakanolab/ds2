import csv
import requests
from bs4 import BeautifulSoup

BASE_URL = 'http://www.kanazawa-it.ac.jp/curriculum_html/undergraduate'

def get_courses(url, prefix):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    courses = []
    for course in soup.find_all('li'):
        name = course.find('div', class_='name')
        if name and name.text.startswith(prefix):
            courses.append((prefix, name.text, course.find('p').text))
    return courses


if __name__ == '__main__':
    courses_ep = get_courses(BASE_URL + '/engineering/computer.html', 'E')
    courses_fm = get_courses(BASE_URL + '/informatics/media.html', 'F')
    with open('courses.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['label', 'name', 'description'])
        for label, name, description in courses_ep + courses_fm:
            writer.writerow([label, name, description])
