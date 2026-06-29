from fastapi import FastAPI, UploadFile, File, HTTPException
from pathlib import Path
import shutil
app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Document Assistant"}


#Upload PDF file endpoint

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code = 400, detail= "Invalid file type. Only PDF files are allowed.")
    file_path = UPLOAD_DIR / file.filename

    #write uploaded file to a folder
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file,buffer)

    return {"filename" : file.filename, "status" : "uploaded successfully"}
