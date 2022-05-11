from random import choice

from fastapi import FastAPI, UploadFile, File, HTTPException
import uvicorn


app = FastAPI()


def predict(audio_file):
    predicted_label = choice(['hum', 'whistle']) 
    return predicted_label


@app.get("/")
async def root():
    return {"message": "Welcome to the Hums and Whistles service"}


@app.post("/predict")
async def create_upload_file(uploaded_audio: UploadFile = File(...)):
    print(uploaded_audio.filename+" has just been uploaded")

    if uploaded_audio.content_type != "audio/x-wav":
        raise HTTPException(400, detail="Invalid document type")
        
    predicted_label = predict(uploaded_audio.file.read())

    return{"message": uploaded_audio.filename+" is a "+predicted_label}


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')