#import git
#git.Repo.clone_from('https://github.com/JOJO-men/Horizon.git', 'main1')
import requests

response = requests.get("https://api.github.com/repos/JOJO-men/Horizon/releases/latest")
print(response.json()["published_at"])









import zipfile
import requests
import os
from urllib.parse import urlencode
try:
    print("Processing...")

    base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'
    public_key = 'https://disk.yandex.ru/d/CdAL0a1JNWhWRw'  # Сюда вписываете вашу ссылку

    # Получаем загрузочную ссылку
    final_url = base_url + urlencode(dict(public_key=public_key))
    response = requests.get(final_url)
    download_url = response.json()['href']

    # Загружаем файл и сохраняем его
    download_response = requests.get(download_url)
    with open('Nightmare.zip', 'wb') as f:  # Здесь укажите нужный путь к файлу
        f.write(download_response.content)

    fantasy_zip = zipfile.ZipFile(os.getcwd() + '\\Nightmare.zip')
    fantasy_zip.extractall(os.getcwd())
    fantasy_zip.close()
    print("done")
except Exception as exc:
    print(exc)
    print("FATAL ERROR")
