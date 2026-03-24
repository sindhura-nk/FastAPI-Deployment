from pydantic import BaseModel

class user_reports(BaseModel):
    Gender:float
    AGE:float
    Urea:float
    Cr:float
    HbA1c:float
    Chol:float
    TG:float
    HDL:float
    LDL:float
    VLDL:float
    BMI:float