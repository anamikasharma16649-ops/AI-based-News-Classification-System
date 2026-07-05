from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException
from preprocesing import preprocess, preprocess_text
import pickle
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(title = "News Classification System")

app.mount("/static", StaticFiles(directory="frontend"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



with open("model.pkl", "rb") as f:
    model = pickle.load(f)

CATEGORY_MAP = {
    1: {"name": "World", "icon": "🌍"},
    2: {"name": "Sports", "icon": "🏅"},
    3: {"name": "Business", "icon": "💼"},
    4: {"name": "Sci/Tech", "icon": "💻"},
}


class NewsReqst(BaseModel):
    news : str

@app.get("/")
def home():
    return FileResponse("frontend/index.html")


@app.post("/classify")
async def classify_news(news_request: NewsReqst):

    if not news_request.news.strip():
        raise HTTPException(
            status_code=400, detail="News article cannot be empty."
        )

    try:
        prediction = int(model.predict([news_request.news])[0])
        return {
            "success": True,
            "class_id": prediction,
            "category": CATEGORY_MAP[prediction]["name"],
            "icon": CATEGORY_MAP[prediction]["icon"],
        }

    except Exception as e:
        raise HTTPException(
            status_code=500, detail= str(e)
        )
