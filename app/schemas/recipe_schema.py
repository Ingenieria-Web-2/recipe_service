"""
Recipe schemas for request and response models (pydantic).
"""

from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict

from models.recipe_model import ExperienceLevel


# Shared properties
class RecipeBase(BaseModel):
    """
    Base schema for a recipe.
    """
    name: str
    description: Optional[str] = None
    difficulty: ExperienceLevel
    prep_time_minutes: int

# Properties to receive on item creation


class RecipeCreate(RecipeBase):
    """
    Schema for creating a new recipe.
    """

# Properties to return to client


class Recipe(RecipeBase):
    """
    Schema for returning a recipe to the client.
    """
    id: int
    owner_id: int

    model_config = ConfigDict(from_attributes=True)
