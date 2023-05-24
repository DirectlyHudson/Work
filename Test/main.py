import requests
from bs4 import BeautifulSoup


# EROBELLA

def get_erobella_data(url_search_models):
    # # Код запиту для отримання даних моделей:
    # # !!!Не впевнений чи повинен змінюватись user-agent, бо буде проксі!!! Це, здається, непотрібний крок

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      "Chrome/112.0.0.0 Safari/537.36 OPR/98.0.0.0"
    }
    req = requests.get(url_search_models, headers=headers)
    src = req.text

    # + створюємо файл із сторінкою, аби не було багато запитів і обмежень від сайту:
    with open("ErobellaComModels.html", "w") as page_allmodels:
        page_allmodels.write(src)

    # читаємо файл і зберігаємо в змінну:
    with open("ErobellaComModels.html") as page_allmodels:
        source_html = page_allmodels.read()

    # Початок парсингу. Знаходимо потрібні блоки з профілями
    soup = BeautifulSoup(source_html, "lxml")
    all_urls_on_page = soup.find_all("div", class_="profile-block")

    # Створюємо список, куди записуємо знайдені посилання на профілі моделей
    urls_page = []
    for url in all_urls_on_page:
        url_page = "https://erobella.com" + url.find("a", class_="profile-block-link")["href"]
        urls_page.append(url_page)
        # print(url_page)
    return print(urls_page)
    # # Зі списку, створенного вище, беремо кожен профіль та вилучаємо потрібні дані
    # for url_page in urls_page:
    #     req = requests.get(url_page, headers)
    #     site_name = url_page.split("/")[-2]
    #
    #     # Запис та читання
    #     with open(f"data/models_profiles/{site_name}.html", "w") as site_name_create:
    #         site_name_create.write(req.text)
    #     with open(f"data/models_profiles/{site_name}.html") as site_name_read:
    #         site_name = site_name_read.read()
    #
    #     # Вилучення даних
    #     soup = BeautifulSoup(site_name, "lxml")
    #     model_data = soup.find("div", class_="user-profile-component-content")
    #     print(model_data)

        # for data in model_data:
        #     nickname = data.find("div", class_="flex-column")
        #     print(nickname)


# get_erobella_data(f"https://erobella.com/sex/#?gender=Weiblich&search_radius=0km")
# Виклик функції збору даних із сайту erobella.com від 0 до 416 сторінки
for page_number in range(0, 417):
    get_erobella_data(f"https://erobella.com/sex/#?gender=Weiblich&search_radius=0km&page={page_number}")
