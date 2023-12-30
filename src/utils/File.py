import json

class File:
    def __init__(self) -> None:
        pass

    def write_json(self, path: str, content: any) -> None:
        with open(path, 'w', encoding= "utf-8") as file:
            json.dump(content, file, ensure_ascii=False, indent=2, default=str)

    def write_str(self, path: str, content: any) -> None:
        with open(path, 'w', encoding="utf-8") as file:
            file.writelines(content)

    def write_byte(self, path: str, media: any) -> None:
        with open(path, 'wb') as file:
            file.write(media.content)

    def read_json(self, path: str):
        with open(path, 'r') as file:
            data = json.load(file)
        return data