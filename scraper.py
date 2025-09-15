import requests
from newsplease import NewsPlease
from urls import urls

# Browser-like headers
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

def scrape_articles():
    articles_data = []

    for url in urls:
        try:
            response = requests.get(url, headers=HEADERS, timeout=10)

            if response.status_code != 200:
                articles_data.append({
                    "url": url,
                    "error": f"not a 200 response: {response.status_code}"
                })
                continue

            article = NewsPlease.from_html(response.text, url)

            if article and article.maintext:
                articles_data.append({
                    "url": url,
                    "title": article.title,
                    "authors": article.authors,
                    "publish_date": str(article.date_publish) if article.date_publish else None,
                    "text": article.maintext[:200] + "..."
                })
            else:
                articles_data.append({
                    "url": url,
                    "error": "Could not extract article content"
                })

        except Exception as e:
            articles_data.append({
                "url": url,
                "error": str(e)
            })

    return articles_data
