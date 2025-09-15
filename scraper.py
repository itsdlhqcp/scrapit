from newsplease import NewsPlease
from urls import urls

def scrape_articles():
    articles_data = []
    articles = NewsPlease.from_urls(urls)

    for url, article in articles.items():
        if article:
            articles_data.append({
                "url": url,
                "title": article.title,
                "authors": article.authors,
                "publish_date": str(article.date_publish) if article.date_publish else None,
                "text": article.maintext[:200] + "..." if article.maintext else None
            })
        else:
            articles_data.append({
                "url": url,
                "error": "Could not extract article"
            })

    return articles_data
