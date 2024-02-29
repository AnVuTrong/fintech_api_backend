from datetime import datetime
from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship


# Define the model class that inherits from the base class
class StockListBase(SQLModel):
    # We use UUID as the primary key
    id: str

    # The name of the company
    name: str

    # The quote symbol
    code: str = Field(index=True)

    # The exchange where the stock is traded
    exchange: Optional[str] = Field(index=True)

    # Define the __getitem__ method to allow for easy access to the attributes
    def __getitem__(self, item):
        return getattr(self, item)


class StockList(StockListBase, table=True):
    id: str = Field(primary_key=True)

    vn_name: Optional[str] = Field(index=True)

    # The type of doing financial report
    accounting_type : str = Field(index=True)

    # String for company's description
    description : Optional[str]

    # String for company's address
    address : Optional[str]

    # String for company's website
    website : Optional[str]

    # Company's industry level 1
    industry_level_1 : Optional[str]

    # Company's industry level 2
    industry_level_2 : Optional[str]

    # Company's industry level 3
    industry_level_3 : Optional[str]

    # Company's industry level 4
    industry_level_4 : Optional[str]

    # The date of the company's listing
    listing_date : Optional[datetime]

    # The daily trading volume
    daily_trading_volume : Optional[float]

    # The average daily trading volume for the last 15 days
    average_daily_trading_volume : Optional[float]

    # The company's market capitalization
    market_cap : Optional[float]

    # The company's total assets
    total_assets : Optional[float]

    # The total number of outstanding shares
    outstanding_shares : Optional[float]

    # The total number of issued shares
    issued_shares : Optional[float]

    # The total number of treasury shares
    treasury_shares : Optional[float]

# Update the forward reference
StockList.model_rebuild()


