import os
import asyncio

from dotenv import *
from src import Browser
from src import file
from src import ArgumentParserCustom
from src import ArgumentParserNotFirst
from src import logger

if __name__ == '__main__':

    
    if not os.path.exists(path='.env'):
        arg = ArgumentParserCustom(description='To run the program for the first time, please enter the flag according to the provisions')
        arg.add_argument('--email', '-e', type=str, help='Please insert your email', required=True)
        arg.add_argument('--password', '-p', type=str, help='Please insert your password', required=True)
        arg.add_argument('--search', '-s', type=str, help='Please insert key for search', required=True)
        args = arg.parse_args()

        file.write('.env', content='')

        load_dotenv()
        file_env = find_dotenv()
        set_key(file_env, 'EMAIL', args.email)
        set_key(file_env, 'PASS', args.password)
        set_key(file_env, 'COOKIES', '[]')

        logger.info('Flag Founded')
        logger.info('Set Environment..')
        logger.info('Environment Cretated')
        logger.info(f'Search With KeyWord: {args.search}')
        print()

    else:
        arg = ArgumentParserNotFirst(description='please enter the flag according to the provisions')
        arg.add_argument('--search', '-s', type=str, help='Please insert key for search', required=True)
        args = arg.parse_args()
    

    browser = Browser()
    asyncio.run(browser.main(search=args.search))