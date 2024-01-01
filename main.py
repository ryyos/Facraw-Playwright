import os
import asyncio

from src import Browser

br = Browser()
asyncio.run(br.main())

# from dotenv import *

# env_file = find_dotenv()
# load_dotenv()
# print(os.getenv('EMAIL'))

# os.environ['EMAIL'] = 'hehe'
# print()

# set_key(env_file, 'EMAIL', os.getenv('EMAIL'))

