import requests
from bs4 import BeautifulSoup


# EROBELLA
def get_erobella_data(url_search_models):
    # # Код запиту для отримання даних моделей:
    # # !!!Не впевнений чи повинен змінюватись user-agent, бо буде проксі!!! Це, здається, непотрібний крок

    # headers = {
    #     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
    #                   "Chrome/112.0.0.0 Safari/537.36 OPR/98.0.0.0"
    # }
    # req = requests.get(url_search_models, headers=headers)
    # src = req.text
    #
    # # + створюємо файл із сторінкою, аби не було багато запитів і обмежень від сайту:
    # with open("ErobellaComModels.html", "w") as page_models:
    #     page_models.write(src)

    # читаємо файл і зберігаємо в змінну:
    with open("ErobellaComModels.html") as page_models:
        source_html = page_models.read()

    # Початок парсингу
    # soup = BeautifulSoup(source_html, "lxml")
    # all_urls_on_page = soup.find_all("div", class_="row profile-block-wrap profile-block-wrap--main")
    # print(all_urls_on_page)

    soup = BeautifulSoup(source_html, "lxml")
    all_urls_on_page = soup.find_all("div", class_="row profile-block-wrap profile-block-wrap--main")
    print(all_urls_on_page)

    counter = 0

    for url in all_urls_on_page:
        url_page = "https://erobella.com" + url.find("div", class_="profile-block").find("a").get("href")
        counter += 1
        print(url_page)
        print(counter)


get_erobella_data("https://erobella.com/sex/#?gender=Weiblich&search_radius=0km")
