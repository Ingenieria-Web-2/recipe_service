"""
Entry point for the Recipe microservice.
"""

from fastapi import FastAPI

from api.routers import recipe_router
from db.session import Base, engine

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Recipe Microservice")

app.include_router(recipe_router.router, prefix="/api/recipe", tags=["recipe"])


@app.get("/")
def read_root():
    """
    Root endpoint to verify the service is running.
    """
    return {"message": "Recipe API is up and running!"}
