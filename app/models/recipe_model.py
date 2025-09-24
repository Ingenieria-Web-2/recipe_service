"""
Recipe model definition using SQLAlchemy.
"""

import enum

from sqlalchemy import Column, Enum, Integer, String, Text

from db.session import Base


class ExperienceLevel(enum.Enum):
    """
    Enum for recipe difficulty levels.
    """
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"


class Recipe(Base):
    """
    SQLAlchemy model for a recipe.
    """
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(Text, nullable=True)
    difficulty = Column(Enum(ExperienceLevel), nullable=False)
    prep_time_minutes = Column(Integer, nullable=False)
    owner_id = Column(Integer, index=True, nullable=False)
