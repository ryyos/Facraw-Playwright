import json
import asyncio

from time import time
from importlib import reload
from icecream import ic
from playwright.async_api import async_playwright, BrowserContext


class Browser:
    def __init__(self) -> None:
        self.base_url = 'https://www.facebook.com'
        self.EMAIL = 'xysryo@gmail.com'
        self.PASS = '1217481210'
        pass

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
        with open("data/cookies/cookies.json", "r") as f:
            cookies = json.loads(f.read())
            
        for cookie in cookies:
            ic(cookie["expires"])

            if int(time()) > cookie["expires"]:
                browser = await self.login(browser=browser)

                with open("data/cookies/cookies.json", "w") as f:
                    f.write(json.dumps(await browser.cookies()))

        return browser


        


    async def main(self):
        self.__playwright = await async_playwright().start()
        browser_before_login = await self.__playwright.chromium.launch(headless=False, args=['--window-position=-8,-2'])
        browser_before_login = await browser_before_login.new_context()

        browser = await self.set_cookies(browser=browser_before_login)

        try:
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





