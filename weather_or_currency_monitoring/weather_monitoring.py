import bs4
import requests


def start(url: str, headers: dict):
    data = requests.get(url=url, headers=headers).content

    soup = bs4.BeautifulSoup(data, 'html.parser')
    final = soup.find_all('span', {"class": "unit_temperature_c"})[0].text
    print(f"Погода в {url.split('-')[1].capitalize()} сейчас: {final}")


if __name__ == '__main__':
    pass
