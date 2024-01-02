import sys
from argparse import ArgumentParser

class ArgumentParserCustom(ArgumentParser):
    def exit(self, status=0, message=None):
            if status:
                print("""
to run the first please insert flags

--email    or -e    YOUR_EMAIL
--password or -p    YOUR_PASSWORD
--search   or -s    WHAT_DO_YOU_WANT_TO_SEARCH

Example: python main.py --email example@gmail.com --password 12345678 --search Freya JKT48
""")
            sys.exit(status)

class ArgumentParserNotFirst(ArgumentParser):
    def exit(self, status=0, message=None):
            if status:
                print("""
please insert flags

--search   or -s    WHAT_DO_YOU_WANT_TO_SEARCH
                      
Example: python main.py --search Freya JKT48
""")
            sys.exit(status)