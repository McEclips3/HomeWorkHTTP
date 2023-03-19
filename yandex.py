import requests


class YandexDisk:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_link(self, file_path):
        up_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(up_url, headers=headers, params=params)
        data = response.json()
        href = data.get('href')
        return href

    def upload_file(self, file_path, name):
        href = self._get_link(file_path=file_path)
        response = requests.put(href, data=open(name, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Файл залит')
