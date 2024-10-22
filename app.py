import os

import numpy as np
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from mlProject.pipeline.prediction import PredictionPipeline

app = FastAPI()  # initializing a FastAPI app
app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


# Route to display the home page
@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Route to train the pipeline
@app.get("/train")
async def training():
    os.system("python main.py")
    return {"message": "Training Successful!"}


# Route to handle predictions in a web UI
@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    fixed_acidity: float = Form(...),
    volatile_acidity: float = Form(...),
    citric_acid: float = Form(...),
    residual_sugar: float = Form(...),
    chlorides: float = Form(...),
    free_sulfur_dioxide: float = Form(...),
    total_sulfur_dioxide: float = Form(...),
    density: float = Form(...),
    pH: float = Form(...),
    sulphates: float = Form(...),
    alcohol: float = Form(...),
):
    try:
        # Prepare the input data as a numpy array
        data = [
            fixed_acidity,
            volatile_acidity,
            citric_acid,
            residual_sugar,
            chlorides,
            free_sulfur_dioxide,
            total_sulfur_dioxide,
            density,
            pH,
            sulphates,
            alcohol,
        ]
        data = np.array(data).reshape(1, 11)

        # Instantiate prediction pipeline and make predictions
        obj = PredictionPipeline()
        predict = obj.predict(data)

        return templates.TemplateResponse(
            "results.html", {"request": request, "prediction": str(predict)}
        )

    except Exception as e:
        print(f"The Exception message is: {e}")
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "message": "Something went wrong"},
        )


# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check route that returns a simple status message"""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
