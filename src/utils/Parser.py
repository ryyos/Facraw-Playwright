from pyquery import PyQuery

class Parser:
    def __init__(self) -> None:
        pass

    def ex(self, html: PyQuery, selector: str) -> PyQuery:
        result = None
        try:
            html: str = PyQuery(html)
            result = html.find(selector)
        except Exception as err:
            print(err)

        finally:
            return result