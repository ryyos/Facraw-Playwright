import requests
from http.cookies import SimpleCookie
from icecream import ic

def convert_cookies(cookies):
    cookie = SimpleCookie()
    
    for key, value in cookies.items():
        cookie[key] = value

    return cookie.output(header='', sep=';')


def start():
    cookies = {
        "sb":"vTSQZVQWp3vXCNsKP7q0VGtT",
        "wd":"1919x1050",
        "datr": "vTSQZW_5gW9EyEtZ2qoQem6v",
        "c_user": "61554883686578",
        "xs": "20%3AiDhoSckM3bD33A%3A2%3A1703949509%3A-1%3A-1",
        "fr": "0lQBlatVtvdoEp4bd.AWWL2mn7VL79YtVFORzAOXAKW4w.BlkDS9.Vg.AAA.0.0.BlkDTH.AWVOijQTT8s",
        "presence":"C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1703949516208%2C%22v%22%3A1%7D",
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Cookie": convert_cookies(cookies)
    }

    ic(headers)


start()