from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from datetime import datetime


# Define the news model class that inherits from the base class
class Quoting(SQLModel):
    # The id of the quoting, using UUID
    id: Optional[str]

    # The origin of the data, can be Intraday or History
    api_origin: Optional[str]

    # The stock quote code
    mack: str = Field(index=True)

    # The date of the quoting
    ngay: datetime = Field(index=True)

    # The last time the data is updated
    lastupdate: datetime = Field(index=True)

    # The original open price of the day
    open_root: Optional[float]

    # The original high price of the day
    high_root: Optional[float]

    # The original low price of the day
    low_root: Optional[float]

    # The original close price of the day
    close_root: Optional[float]

    # The original volume of the day
    volume_root: Optional[int]

    # The adjusted open price of the day
    open_adjust: Optional[float]

    # The adjusted high price of the day
    high_adjust: Optional[float]

    # The adjusted low price of the day
    low_adjust: Optional[float]

    # The adjusted close price of the day
    close_adjust: Optional[float]

    # The adjusted volume of the day
    volume_adjust: Optional[int]

    # The ceiling price of the day
    ceilingprice: Optional[float]

    # The floor price of the day
    floorprice: Optional[float]

    # The total trading value of the day
    giatri_giaodich: Optional[float]

    # The selling volume of foreign investors
    kl_nn_ban: Optional[float]

    # The buying volume of foreign investors
    kl_nn_mua: Optional[float]

    # The value of selling from foreign investors
    gt_nn_ban: Optional[float]

    # The value of buying from foreign investors
    gt_nn_mua: Optional[float]

    # Define the __getitem__ method to allow for easy access to the attributes
    def __getitem__(self, item):
        return getattr(self, item)


class IntradayQuoting(Quoting, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)

    ngay: Optional[datetime]

    # The change in price of the day
    changed: Optional[float]

    # The change ratio of the day
    changedratio: Optional[float]


class HistoryQuoting(Quoting, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)

    ngay: Optional[datetime]

    # The average price of the day
    avgprice: Optional[float]

    # The change in price of the day
    changed: Optional[float]

    # The change ratio of the day
    changedratio: Optional[float]

# Update the forward reference
IntradayQuoting.model_rebuild()
HistoryQuoting.model_rebuild()