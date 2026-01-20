from contextlib import asynccontextmanager
from fastapi import FastAPI
from features.products.routes import router as product_router
from features.carts.routes import router as cart_router
from features.auth.controllers import AuthController as auth_router
from common.exceptions import APIException, generic_exception_handler, api_exception_handler

# 1. Import database engine and Base
from core.database import engine, Base
# 2. Import models so Base knows about them 
# (Even if router imports them indirectly, it's safer to be explicit here)
from features.products import models 

# 3. Define the startup logic
@asynccontextmanager
async def lifespan(app: FastAPI):
    # This runs when the app starts
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    yield
    # (Optional) Code here runs when app shuts down

app = FastAPI(
    title="FastAPI Product Management",
    description="A feature-based FastAPI project example",
    version="1.0.0",
    lifespan=lifespan # 4. Attach the logic to the app
)

# Include feature routers
app.include_router(product_router, prefix="/products", tags=["Products"])
app.include_router(cart_router, prefix="/carts", tags=["Carts"])
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])

# Register custom exception handlers
app.add_exception_handler(APIException, api_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI Product Management!"}