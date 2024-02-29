"""
In this file, we will define the class News which might belong to the whole market or a single company.
"""
from pydantic import ConfigDict
from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from datetime import datetime


# Define the news model class that inherits from the base class
class NewsBase(SQLModel):
    # We use UUID as the primary key
    id: str

    # The title of the news
    title: Optional[str]

    # The url of the news
    url: str

    # The date of the news which is updated on the system
    time: datetime

    # The date source of the news
    datepost: str

    # The source of the news
    sourcenews: Optional[str]

    # The main content of the news
    maincontent: Optional[str]

    # The main content of the news but in English
    maincontent_en: Optional[str]

    # The sentiment of the maincontent_en
    sentiment: Optional[float]

    # Define the __getitem__ method to allow for easy access to the attributes
    def __getitem__(self, item):
        return getattr(self, item)


# Define the news model class that inherits from the base class
class NewsMarket(NewsBase, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)

    model_config = ConfigDict(from_attributes=True)


class NewsStock(NewsBase, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    code: str

# Update the forward reference
NewsStock.model_rebuild()
NewsMarket.model_rebuild()
