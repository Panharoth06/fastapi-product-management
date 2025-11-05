from fastapi import FastAPI
from features.products.routes import router as product_router
from common.exceptions import APIException, generic_exception_handler, api_exception_handler

app = FastAPI(
    title="FastAPI Product Management",
    description="A feature-based FastAPI project example",
    version="1.0.0"
)

# Optional: run initialization logic on startup
# @app.on_event("startup")
# def on_startup():
#     init_db()  # e.g., create tables, insert seed data

# Include feature routers
app.include_router(product_router, prefix="/products", tags=["Products"])

# Register custom exception handlers
app.add_exception_handler(APIException, api_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

# Simple health check endpoint
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI Product Management!"}
