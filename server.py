from fastapi import FastAPI
from scraper import scrape_articles

app = FastAPI()

@app.get("/")
def root():
    return {"message": "News Scraper API is running"}

@app.get("/articles")
def get_articles():
    return {"articles": scrape_articles()}
