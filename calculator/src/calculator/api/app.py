from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI(title="Calculator App")

# Get the absolute path to the templates directory
BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "calculator.html",
        {"request": request, "result": None}
    )

@app.post("/calculate")
async def calculate(
    request: Request,
    num1: float = Form(...),
    num2: float = Form(...),
    operation: str = Form(...)
):
    try:
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                raise ValueError("Cannot divide by zero")
            result = num1 / num2
        else:
            raise ValueError("Invalid operation")
        
        return templates.TemplateResponse(
            "calculator.html",
            {
                "request": request,
                "result": f"{result:.2f}",
                "num1": num1,
                "num2": num2,
                "operation": operation
            }
        )
    except ValueError as e:
        return templates.TemplateResponse(
            "calculator.html",
            {
                "request": request,
                "error": str(e),
                "num1": num1,
                "num2": num2,
                "operation": operation
            }
        )
