import json
import asyncio
import os

from dotenv import *
from time import time
from importlib import reload
from icecream import ic
from playwright.async_api import async_playwright, BrowserContext

from src.utils.Logs import logger

class Browser:
    def __init__(self) -> None:

        load_dotenv()
        self.FILE_ENV = find_dotenv()
        self.EMAIL = os.getenv('EMAIL')
        self.PASS = os.getenv('PASS')
        self.COOKIES = json.loads(os.getenv('COOKIES'))
        
        self.base_url = 'https://web.facebook.com'
        

    def facebook(self):
        logger.info('reload facebook crawler')
        print()
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
        return browser


    async def set_cookies(self, browser: BrowserContext):
            
        logger.info('check facebook cookies')
        print()
        
        if not self.COOKIES:

            logger.warning('cookies not found')
            logger.warning('Login attempt to retrieve cookies')
            print()

            browser = await self.login(browser=browser)
            os.environ['COOKIES'] = json.dumps(await browser.cookies())
            set_key(self.FILE_ENV, 'COOKIES', os.environ['COOKIES'])
            self.COOKIES = json.loads(os.getenv('COOKIES'))

            logger.info('login successful')
            logger.info('Cookies updated successfully')
            print()

            return browser

        
        logger.info('cookies found')
        logger.info('check expired cookies')
        print()

        for cookie in self.COOKIES:

            logger.info(f'{cookie["name"]}: {int(cookie["expires"])}')
            
            if int(time()) > int(cookie["expires"]) > 0:

                logger.warning(f'{cookie["name"]} expired')
                logger.warning('Login attempt to retrieve cookies')
                print()
                
                browser = await self.login(browser=browser)
                os.environ['COOKIES'] = json.dumps(await browser.cookies())
                set_key(self.FILE_ENV, 'COOKIES', os.environ['COOKIES'])
                self.COOKIES = json.loads(os.getenv('COOKIES'))
                logger.info('login successful')
                logger.info('Cookies updated successfully')
                print()

        logger.info('cookies activated')
        logger.info('add cookies in browser')
        print()

        await browser.add_cookies(self.COOKIES)

        return browser


    async def main(self, search: str):

        logger.info('Facebook Scraper Start..')
        logger.info('Playwright Started..')
        print()

        self.__playwright = await async_playwright().start()
        browser_before_login = await self.__playwright.chromium.launch(headless=False, args=['--window-position=-8,-2'])
        browser_before_login = await browser_before_login.new_context()

        browser = await self.set_cookies(browser=browser_before_login)

        try:
            
            while True:
                facebook = self.facebook()
                try:

                    result = await facebook.main(browser, search=search, cookies=os.getenv('COOKIES'))
                    if result: break

                except Exception as err:
                    ic(err)
                    input('err')

        except KeyboardInterrupt:
            ic('stop')
            await browser_before_login.close()
            await self.__playwright.stop()





