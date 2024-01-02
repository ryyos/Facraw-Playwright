import requests
import json
import re

from uuid import uuid4
from urllib import request
from time import sleep
from icecream import ic


class UrlParser:
    def __init__(self) -> None:
        self.__image_id = None
        self.__url_pattern = re.compile(r'"uri":"(https:\\\/\\\/[^\"]+)"')


    def __curl(self, path: str,url_image: str):
        request.urlretrieve(url_image, f'{path}/{uuid4()}.jpg')


    def ex(self, path: str, image_id: int, media_token, cookies: str, url_card: str) -> str:
        self.__image_id = image_id

        payload = {
            'av': 61554883686578,
            '__user': 61554883686578,
            '__a': 1,
            '__req': '1y',
            '__hs': '19723.HYP:comet_pkg.2.1..2.1',
            'dpr': 1,
            '__ccg': 'EXCELLENT',
            '__rev': 1010618297,
            '__s': 'p0avn1:1tdhw3:zzl31w',
            '__hsi': 7319054393648017670,
            '__dyn': '7AzHK4HwkEng5K8G6EjBAo2nDwAxu13wFwhUKbgS3q2ibwNw9G2Saw8i2S1DwUx60GE3Qwb-q7oc81xoswIK1Rwwwqo465o-cwfG12wOx62G5Usw9m1YwBgK7o884y0Mo4G1hx-3m1mzXw8W58jwGzEaE5e7oqBwJK2W5olwUwgojUlDw-wUwxwjFovUaU3VBwFKq2-azqwqo4i223908O3216xi4UdUcojxK2B0oobo8oC1hxB0qo4e16wWwjHDzUiw',
            '__csr': 'g9sh9b6PrdfkiyTT4n4RbdeAx5TthsRIBsIy94FtaTRjlPt4h5QCymWlkGOnGLFkV97FGGWtWuaGQiGVAi8yvZ2WKFaGUHCK9maLQqhpriOzHKF9qFeim8F2Ey9gBxi6qzoGcwwUvV9aCUy8z8C4ETG6EG4EggrGfxe48lgG9AG7UjWHx67FGz4i2S2e2yqm9x-bxSi1izEgxucwzU4q5Eyi58boGq1yUhw8u1ixq0yo7ii1vxm5E5au2K1hxOU5W0ke0m62e1nw2FOeu0si02AK00jTy5o12kcwPw1fC2u0smEHxZ05XOwiE1qE0KDw0SAo0sWw5vw0xKw0YVw9G02Vu08Yo8o0Tq',
            '__comet_req': 15,
            'fb_dtsg': 'NAcNDQSHrTQoVaLDYjqQn7YB1nzvYzHiyCCW11XgKcdMq_Hljzu4r9w:17:1704046353',
            'jazoest': 25627,
            'lsd': 'lvZfhg3L7NWQ_djzi-NVYu',
            '__aaid': 0,
            '__spin_r': 1010618297,
            '__spin_b': 'trunk',
            '__spin_t': 1704100145,
            'qpl_active_flow_ids': 431626709,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'CometPhotoRootContentQuery',
            'variables': json.dumps({
                "UFI2CommentsProvider_commentsKey":"CometPhotoRootQuery",
                "displayCommentsContextEnableComment":None,
                "displayCommentsContextIsAdPreview":None,
                "displayCommentsContextIsAggregatedShare":None,
                "displayCommentsContextIsStorySet":None,
                "displayCommentsFeedbackContext":None,
                "feedbackSource":65,
                "feedLocation":"COMET_MEDIA_VIEWER",
                "focusCommentID":None,
                "isMediaset":True,
                "mediasetToken": str(media_token),
                "nodeID": str(image_id),
                "privacySelectorRenderLocation":"COMET_MEDIA_VIEWER",
                "renderLocation":"permalink",
                "scale":1,
                "useDefaultActor":False,
                "useHScroll":False,
                "__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":False,
                "__relay_internal__pv__CometUFIIsRTAEnabledrelayprovider":False
                }),
            'server_timestamps': True,
            'doc_id': 7089273397778090
        }


        header = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'Content-Length': '2069',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'sb=ueeLZaTMfeTXW68RY813oOzl; datr=ueeLZe-wA6Jtq5O_Z9GAYJ-X; locale=en_GB; c_user=61554883686578; xs=17%3APL3qDfdMIA2sSA%3A2%3A1704046353%3A-1%3A-1%3A%3AAcWL3QjjkgocoyjkGUkMnzNnE65_HKQBpChBIDg6fA; fr=1hXzmdfE0hAJAtabB.AWXnCO5DlvU3fT6nMjyCnwZC9wU.BlkoEp.FU.AAA.0.0.BlkoEx.AWWknMoFO90; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1704100150986%2C%22v%22%3A1%7D; wd=939x945',
            'Dpr': '1',
            'Origin': 'https://web.facebook.com',
            'Referer': str(url_card),
            'Sec-Ch-Prefers-Color-Scheme': 'dark',
            'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'Sec-Ch-Ua-Full-Version-List': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.130", "Google Chrome";v="120.0.6099.130"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Model': '""',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Ch-Ua-Platform-Version': '"15.0.0"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Viewport-Width': '939',
            'X-Asbd-Id': '129477',
            'X-Fb-Friendly-Name': 'CometPhotoRootContentQuery',
            'X-Fb-Lsd': 'lvZfhg3L7NWQ_djzi-NVYu'
        }



        response = requests.post(url='https://web.facebook.com/api/graphql/', data=payload, headers=header)

        URL = self.__url_pattern.findall(response.text.split('\r\n')[0])[0].replace('\\', '')
        self.__curl(path=path, url_image=URL)

        return URL


