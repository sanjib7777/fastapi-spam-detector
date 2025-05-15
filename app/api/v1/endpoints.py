from fastapi import APIRouter
from pydantic import BaseModel
from app.model.predictor import predict_spam

router = APIRouter()

class EmailInput(BaseModel):
    text: str

@router.post("/predict")
def classify_email(input: EmailInput):
    result = predict_spam(input.text)
    return {"result": result}
