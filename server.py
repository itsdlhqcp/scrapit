import os
import uvicorn
from fastapi import FastAPI
from scraper import scrape_articles

app = FastAPI()

@app.get("/")
def root():
    return {"message": "News Scraper API is running"}

@app.get("/articles")
def get_articles():
    return {"articles": scrape_articles()}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Render provides PORT env var
    uvicorn.run("server:app", host="0.0.0.0", port=port, reload=True)
