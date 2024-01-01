import json
import asyncio
import os

from dotenv import *
from time import time
from importlib import reload
from icecream import ic
from playwright.async_api import async_playwright, BrowserContext


class Browser:
    def __init__(self) -> None:
        load_dotenv()
        self.FILE_ENV = find_dotenv()
        self.EMAIL = os.getenv('EMAIL')
        self.PASS = os.getenv('PASS')
        self.COOKIES = json.loads(os.getenv('COOKIES'))
        
        self.base_url = 'https://www.facebook.com'
        

    def facebook(self):
        from src.service import facebook
        facebook = reload(facebook)
        from src.service.facebook import Facebook
        facebook = Facebook()
        return facebook
    



    async def login(self, browser: BrowserContext):

        login_page = await browser.new_page()

        await login_page.set_viewport_size({"width":1919, "height":1050})
        await login_page.goto(f'{self.base_url}/login')
        await login_page.get_by_label('Email address or phone number').fill(self.EMAIL)
        await login_page.get_by_label('Password').fill(self.PASS)
        await login_page.locator('#loginbutton').click()
        
        await asyncio.sleep(20)
        ic('finish')
        return browser


    async def set_cookies(self, browser: BrowserContext):
            
        if not self.COOKIES:
            ic('null cookies')
            browser = await self.login(browser=browser)
            os.environ['COOKIES'] = json.dumps(await browser.cookies())
            set_key(self.FILE_ENV, 'COOKIES', os.environ['COOKIES'])

        for cookie in self.COOKIES:
            ic(cookie["expires"])
            
            ic(int(time()) > int(cookie["expires"]) > 0)
            if int(time()) > int(cookie["expires"]) > 0:
                ic("masuk ex")
                browser = await self.login(browser=browser)
                os.environ['COOKIES'] = json.dumps(await browser.cookies())
                set_key(self.FILE_ENV, 'COOKIES', os.environ['COOKIES'])

        return browser


    async def main(self):
        self.__playwright = await async_playwright().start()
        browser_before_login = await self.__playwright.chromium.launch(headless=False, args=['--window-position=-8,-2'])
        browser_before_login = await browser_before_login.new_context()

        browser = await self.set_cookies(browser=browser_before_login)

        try:
            ic('final')
            page = await browser.new_page()
            await page.goto('https://www.facebook.com/home.php')
            while True:
                facebook = self.facebook()
                try:

                    await facebook.main(browser)

                    ic('new sessions')

                except Exception as err:
                    ic(err)
                    input('err')

        except KeyboardInterrupt:
            ic('stop')
            await browser_before_login.close()
            await self.__playwright.stop()





