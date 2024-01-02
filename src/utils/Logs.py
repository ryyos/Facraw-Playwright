import logging


logging.basicConfig(datefmt='%m/%d/%Y %I:%M:%S %p', encoding="utf-8", level=logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

console = logging.StreamHandler()
console.setLevel(level=logging.DEBUG) 
console.setFormatter(formatter)

logger = logging.getLogger()
for existing_handler in logger.handlers[:]:
       logger.removeHandler(existing_handler)

logger.addHandler(console)