from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models.note import Note
from schemas.note import noteEntity,notesEntity
import connect_withMongo

note=APIRouter()

templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def home(request: Request):
    docs=connect_withMongo.client.notes.notes.find({})
    newDocs=[]
    for doc in docs:
        newDocs.append({
            "id":doc["_id"],
            "title":doc["title"],
            "desc":doc["desc"],
            "imp":doc["imp"]
        })
        print(doc)
    return templates.TemplateResponse(
        request=request, name="index.html", context={"newDocs" : newDocs}
    )

@note.post("/")
async def insert_note(request: Request):
    form = await request.form()
    formDict=dict(form)
    print(formDict)
    formDict["imp"] = True if "imp" in formDict else False
    inserted_note=connect_withMongo.client.notes.notes.insert_one(formDict)
    return {"Success":True}

