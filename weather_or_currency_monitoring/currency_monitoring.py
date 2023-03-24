import datetime
import requests


def start(url: str, headers: dict):
    response = requests.get(url=url, headers=headers).json()

    data = filter(lambda x: float(x['priceUsd']) > 10, response["data"])
    data = sorted(data, key=lambda x: float(x['priceUsd']), reverse=True)
    print(f"\n\n\n*********************** {datetime.datetime.now().strftime('%H:%M:%S')} "
          f"*****************************\n\n\n")
    for currency in data:
        print(f"{currency['name']}: {round(float(currency['priceUsd']), 1)} USD")


if __name__ == '__main__':
    pass
