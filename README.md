<h1 align="center" >Hello 👋, I'm Ryo</h1>
<h3 align="center" >An independent backend developer</h3>

<h1 align="center" >Welcome To Facraw-Playwright🎗️</h1>

> This program is an exercise for scraping using playwright

## Feature

- Use of playwright for scrapingminute, hour and day
- use of cookies and check expiration so you don't need to always log in
- can produce up to thousands of data and images in one run

## Tech

- [Playwright](https://playwright.dev/) is a versatile Python library crafted for seamless browser automation and comprehensive end-to-end testing. With Playwright, you can script interactions with web pages, navigate through websites, and execute a variety of actions, replicating real user interactions within the browser environment.

- [python-dotenv](https://pypi.org/project/python-dotenv/) is a convenient Python library that simplifies the management of environment variables in your projects. It allows you to load variables from a .env file into your environment, making it easy to configure and control settings for your applications.

- [asyncio](https://docs.python.org/3/library/asyncio.html) is a Python library that provides a framework for writing asynchronous programs. It enables you to write concurrent code using the async/await syntax, allowing for efficient and scalable I/O operations. asyncio is particularly useful for building responsive and high-performance applications, especially in scenarios where you need to handle many I/O-bound operations concurrently.

- [icecream](https://github.com/gruns/icecream) is a Python library that provides a simple and informative way to log code, helping with monitoring program execution flows.

## Requirement

- [Python](https://www.python.org/) v3.11.6+
- [icecream](https://github.com/gruns/icecream) v2.1.3+
- [python-dotenv](https://pypi.org/project/python-dotenv/) v1.0.0+
- [Playwright](https://playwright.dev/) v1.40.0+

## Installation

> To run this program you need to install some libraries with the command

```sh
pip install -r requirements.txt
```

## Example Usage

```bash
# Clone this repositories
git clone https://github.com/ryosoraa/Facraw-Playwright.git

# go into the directory
cd Facraw-Playwright

```

### First start

To run the program the first time you have to include several flags

```bash
python main.py --email example@gmail.com --password 12345678 --search Freya_JKT48
```

### Start next

and to run the second and subsequent programs you can run it like this

```bash
python main.py --search Freya_JKT48
```

## Flags

|    Flag    | Alias |         Descriptions          |          Example          |
| :--------: | :---: | :---------------------------: | :-----------------------: |
|  --email   |  -e   |  Insert your facebook email   | --email example@gmail.com |
| --password |  -p   | Insert your facebook password |    --password 12345678    |
|  --search  |  -s   |  thing you want to look for   |   --search Freya_JKT48    |

## 🚀Structure

```
│   .gitignore
│   LICENSE
│   main.py
│   README.md
│   requirements.txt
│
├───data
│   ├───image
│   └───json
├───src
│   │   __init__.py
│   │
│   ├───service
│   │       browser.py
│   │       facebook.py
│   │       UrlParser.py
│   │
│   └───utils
│           Arguments.py
│           File.py
│           Logs.py
│           Parser.py
│
└───target
    ├───groups
    │       groups.json
    │
    └───image
```

## Author

👤 **Rio Dwi Saputra**

- Twitter: [@ryosora12](https://twitter.com/ryosora12)
- Github: [@ryosoraa](https://github.com/ryosoraa)
- LinkedIn: [@rio-dwi-saputra-23560b287](https://www.linkedin.com/in/rio-dwi-saputra-23560b287/)
- Instagram: [@ryosoraa](https://www.instagram.com/ryosoraaa/)

<a href="https://www.linkedin.com/in/ryosora/">
  <img align="left" alt="Ryo's LinkedIn" width="24px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />
</a>
<a href="https://www.instagram.com/ryosoraaa/">
  <img align="left" alt="Ryo's Instagram" width="24px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/instagram.svg" /> 
</a>
