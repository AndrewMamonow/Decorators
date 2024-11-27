import requests
from bs4 import BeautifulSoup
from logger import logger_2


KEYWORDS = ['дизайн', 'фото', 'web', 'python']

def fetch_source(url):
    """Получить HTML-страницу."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f'Ошибка при запросе: {e}')
        return None

def parse_articles(source, keywords):
    """Парсинг статей с учетом ключевых слов."""
    if not source:
        return
    
    soup = BeautifulSoup(source, 'html.parser')
    articles = []
    
    for article in soup.find_all('article'):
        headline = article.h2.a.text.strip()
        post_link = 'https://habr.com' + article.find('a', class_='tm-title__link')['href']
        date_tag = article.find('a', class_='tm-article-datetime-published')
        public_date = date_tag.time['title'] if date_tag else "Не указана"
        
        for search_word in keywords:
            if search_word.lower() in headline.lower():
                articles.append({
                    'Дата': public_date,
                    'Заголовок': headline,
                    'Ссылка': post_link
                })
                break  # Исключить дублирование

    return articles

path = 'web.log'    
@logger_2(path)
def find_articles(articles):
    if not articles:
        return ('Статей по заданным ключевым словам не найдено.')
    
    for article in articles:
        return (f"Дата: {article['Дата']} - Заголовок: {article['Заголовок']} - Ссылка: {article['Ссылка']}")

if __name__ == '__main__':
    SOURCE = fetch_source('https://habr.com/ru/articles')
    ARTICLES = parse_articles(SOURCE, KEYWORDS)
    find_articles(ARTICLES)