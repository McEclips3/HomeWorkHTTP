import requests
from pprint import pprint


class Stackoverflow:
    def __init__(self):
        self.url = 'https://api.stackexchange.com/2.3/questions'

    def python(self, start_page, now, past):
        url = self.url
        params = {'site': 'stackoverflow',
                  'fromdate': str(past),
                  'todate': str(now),
                  'tagged': 'python',
                  'sort': 'creation',
                  'page': start_page,
                  'pagesize': 100}
        has_more = True
        questions = []

        while has_more:
            response = requests.get(url, params=params)
            data = response.json()
            for question in data['items']:
                questions.append(question['title'])
            if not data['has_more']:
                has_more = False
            start_page += 1
            params['page'] = start_page
        return questions


if __name__ == '__main__':
    st = Stackoverflow()
    pprint(st.python(1, 1679174564, 1679001763))
