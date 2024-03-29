from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship


# Define the entity model class that inherits from the base class
class EntityBase(SQLModel):
    # We use UUID as the primary key
    id: str

    # The name of the entity
    name: str

    # The quote symbol of the entity
    code: str

    # The exchange the entity is listed on
    exchange: str

    # Define the __getitem__ method to allow for easy access to the attributes
    def __getitem__(self, item):
        return getattr(self, item)


# Define the entity model class that inherits from the base class
class Entity(EntityBase, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)

    # Define the relationship between the entity and the news
    stock_news: List["NewsStock"] = Relationship(back_populates="entity")
    market_news: List["NewsMarket"] = Relationship(back_populates="entity")

    # Define the relationship between the entity and the stock quote
    intraday_quoting: List["IntradayQuoting"] = Relationship(back_populates="entity")
    history_quoting: List["HistoryQuoting"] = Relationship(back_populates="entity")

    # Define the relationship between the entity and the stock list
    stock_list: List["StockList"] = Relationship(back_populates="entity")


# Importing this class to avoid circular dependencies
from app.models.news import NewsStock, NewsMarket
from app.models.stock_quoting import IntradayQuoting, HistoryQuoting
from app.models.stock_list import StockList

# Update the forward reference
Entity.model_rebuild()
