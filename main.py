import requests

# Access StackOverFlow API
response = requests.get('https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow')

# List of skills of mine that I use to find questions on stackoverflow
skills = ['python', 'c++', 'java', 'SQL', 'mySQL', 'rest APIs']

"""
Function returns questions from stackoverflow that are in my skills list
and have only been answered between 0 to 3 times and provides link to the
question
"""


def look_up():
    for query in response.json()['items']:
        if query['score'] in range(0, 3) and \
                any(map(lambda v: v in skills, query['tags'])):
            print(query['title'])
            print(query['link'])
            print(query['tags'])
            print('')


if __name__ == '__main__':
    look_up()
