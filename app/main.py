from fastapi import FastAPI, Query
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
ITEM_CATEGORY_MAP = {
    "banana": "fruit",
    "apple": "fruit",
    "carrot": "vegetable",
    "chicken": "meat"
}

class ItemCategoryUpdate(BaseModel):
    item: str
    category: str

@app.get("/autosuggest")
def autosuggest(query: str = Query(..., min_length=1)):
    item = query.lower().strip()
    category = ITEM_CATEGORY_MAP.get(item)
    if category:
        return {"message": f"{item.capitalize()} is a {category}"}
    return {"message": f"No category found for '{query}'"}

@app.post("/add-item")
def add_item(data: ItemCategoryUpdate):
    item = data.item.lower().strip()
    category = data.category.lower().strip()
    ITEM_CATEGORY_MAP[item] = category
    return {"message": f"Added/updated {item} as {category}"}
