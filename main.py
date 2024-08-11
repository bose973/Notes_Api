# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
# import connect_withMongo

# app = FastAPI()

# #q at line in app.get("/items/{item_id}") to be read as , it can be string type of None type and default value is None
# app.mount("/static", StaticFiles(directory="static"), name="static")
# templates = Jinja2Templates(directory="templates")

# # @app.get("/")
# # async def root():
# #     return {"message": "Hello World"}


# @app.get("/", response_class=HTMLResponse)
# async def home(request: Request):
#     docs=connect_withMongo.client.notes.notes.find({})
#     newDocs=[]
#     for doc in docs:
#         if "notes" in doc:
#             newDocs.append({
#                 "id":doc["_id"],
#                 "notes":doc["notes"]
#             })
#         print(doc)
#     return templates.TemplateResponse(
#         request=request, name="index.html", context={"newDocs" : newDocs}
#     )

# @app.get("/items/{item_id}")
# async def read_item(item_id : int, q : str | None = None ):
#     return {"itemID":item_id,"q":q}

