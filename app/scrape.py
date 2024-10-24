import aiohttp
from bs4 import BeautifulSoup
from app.config import list
import fake_useragent

# Инициализация user-agent
user = fake_useragent.UserAgent().random
header = {'user-agent': user}


# Функция для выполнения асинхронного HTTP-запроса
async def fetch(session, url, headers):
    async with session.get(url, headers=headers) as response:
        return await response.text()

async def scrape():
    check_page = 1
    async with aiohttp.ClientSession() as session:
        for storage in range(1):
            link = f"https://habr.com/ru/articles/page{check_page}"
            response = await fetch(session, link, headers={'user-agent': fake_useragent.UserAgent().random})
            soup = BeautifulSoup(response, "lxml")
            block = soup.find("div", class_="tm-articles-list")

            for article in block.find_all("article", class_="tm-articles-list__item"):
                check_names = article.find("a", class_="tm-title__link")
                result_name = check_names.find("span").text.strip()

                tweet_link = article.find("a", class_="tm-title__link").get("href")
                pars_link = 'https://habr.com' + tweet_link
                list.append(result_name)

            check_page += 1
