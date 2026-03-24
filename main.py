from fastapi import FastAPI
import pickle
from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

with open('model.pkl','rb') as file:
    model = pickle.load(file)
with open('pre.pkl','rb') as file:
    pre=pickle.load(file)

@app.get("/",response_class=HTMLResponse)
async def home(request:Request):
    return templates.TemplateResponse(request, "DiabetesPrediction.html", {"request": request})

@app.post("/predict")
async def predict(request:Request,
    Gender: int = Form(...),
    AGE: float = Form(...),
    Urea: float = Form(...),
    Cr: float = Form(...),
    HbA1c: float = Form(...),
    Chol: float = Form(...),
    TG: float = Form(...),
    HDL: float = Form(...),
    LDL: float = Form(...),
    VLDL: float = Form(...),
    BMI: float = Form(...)):

    x = [Gender,AGE,Urea,Cr,HbA1c,Chol,TG,HDL,LDL,VLDL,BMI]
    xpre = pre.transform([x])

    res = model.predict(xpre)

    if res[0]==0:
        res_op ='Non-Diabetic'
    elif res[0]==1:
        res_op = 'Diabetic'
    else:
        res_op='Predict_Diabetic'
    
    # Return results
    return templates.TemplateResponse(
        request,
        "DiabetesPrediction.html",
        {
            "request": request,
            "prediction_text": res_op
        },
    )

if __name__ == "__main__":
    # Running uvicorn programmatically in production
    uvicorn.run(
        "main:app",               # The FastAPI app instance
        host="127.0.0.1",           # Bind to all interfaces
        port=8000,                # Port number for the application
        log_level="info",         # Log level
        workers=1,                # Number of workers 
        lifespan="on"
    )