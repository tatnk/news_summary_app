import requests
from bs4 import BeautifulSoup

class NewsScraper:
    articles = []

    def get_news_articles(self, keyword):
        self.articles.clear()
        url = f"https://news.yahoo.co.jp/search?p={keyword}&ei=utf-8"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        topic = soup.find("div",class_="sc-cb2n4-0 ifqHuB")
        articles_found = topic.select('li')
        print(f"見つかった記事の数: {len(articles_found)}")
        article_id = 1
        for article in articles_found:
            title_elements = article.find_all('a')
            for title_element in title_elements:
                title = title_element.text
                url = title_element['href']
            self.articles.append({'id': article_id, 'title': title, 'url': url})
            article_id += 1
        return self.articles
    
    def get_news_articles_by_id(self, id):
        for article in self.articles:
            if article['id'] == id:
                response = requests.get(article['url'])
                soup = BeautifulSoup(response.text, 'html.parser')
                article_body = soup.find(class_="article_body")
                if article_body:
                    content = article_body.get_text(strip=True)
                else:
                    content = "記事の内容が見つかりませんでした。"
                article['content'] = content
                return article
        return None
