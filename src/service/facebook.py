import asyncio

from icecream import ic
from pyquery import PyQuery
from datetime import datetime
from time import time
from playwright.async_api import BrowserContext

from src.utils.Parser import Parser


class Facebook:
    def __init__(self) -> None:
        self.search_url = 'https://www.facebook.com/search/groups/?q='
        self.__parser = Parser()
        pass


    async def fetch_group(self, search: str, browser: BrowserContext):
        page = await browser.new_page()
        await page.set_viewport_size({"width":1919, "height":1050})

        URL = self.search_url+search

        ic(URL)
        await page.goto(url=URL)
        await asyncio.sleep(10)

        for _ in range(5):
            await page.evaluate("window.scrollTo(0, document.querySelector('#facebook div > div.x9f619.x1n2onr6.x1ja2u2z.xdt5ytf.x193iq5w.xeuugli.x1r8uery.x1iyjqo2.xs83m0k.x78zum5.x1t2pt76 > div > div > div > div > div').scrollHeight)")
            ic('scroll')
            await asyncio.sleep(3)
            

        cards = PyQuery(await page.inner_html(selector='#facebook')).find('body div > div.x9f619.x1n2onr6.x1ja2u2z div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.x2lah0s.x1nhvcw1.x1qjc9v5.xozqiw3.x1q0g3np.x78zum5.x1iyjqo2.x1t2pt76.x1n2onr6.x1ja2u2z.x1h6rjhl > div.x9f619.x1n2onr6.x1ja2u2z.xdt5ytf.x193iq5w.xeuugli.x1r8uery.x1iyjqo2.xs83m0k.x78zum5.x1t2pt76  > div  div.x6s0dn4.xkh2ocl.x1q0q8m5.x1qhh985.xu3j5b3.xcfux6l.x26u7qi.xm0m39n.x13fuv20.x972fbf.x9f619.x78zum5.x1q0g3np.x1iyjqo2.xs83m0k.x1qughib.xat24cr.x11i5rnm.x1mh8g0r.xdj266r.x2lwn1j.xeuugli.x18d9i69.x4uap5.xkhd6sd.xexx8yu.x1n2onr6.x1ja2u2z')

        results = [
            {
                'crawling_time': str(datetime.now()),
                'crawling_time_epoch': int(time()),
                'url': self.__parser.ex(html=component, selector='div.xu06os2.x1ok221b:nth-child(1) a').attr('href'),
                'name': self.__parser.ex(html=component, selector='a').text(),
                'status': self.__parser.ex(html=component, selector='div.xu06os2.x1ok221b:nth-child(2)').text().split(' · ')[0],
                'members': self.__parser.ex(html=component, selector='div.xu06os2.x1ok221b:nth-child(2)').text().split(' · ')[1],
                'post': self.__parser.ex(html=component, selector='div.xu06os2.x1ok221b:nth-child(2)').text().split(' · ')[-1],

             }for component in cards
        ]

        ic(results)


        input('Close.?')
        await page.close()

    async def main(self, browser: BrowserContext):
        
        process = asyncio.create_task(self.fetch_group(browser=browser, search='Freya JKT48'))

        await process

        input('confirm.?')



facebook = Facebook()

