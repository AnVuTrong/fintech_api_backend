from datetime import datetime

from pydantic import ConfigDict
from sqlmodel import Field, SQLModel
from typing import Optional


# Define the news model class that inherits from the base class
class Indexes(SQLModel):
    # The type of the time series data: 1: Ngày, 2: Tháng, 3: Quý, 4: Năm
    kieu_thoi_gian: Optional[int]

    # The date, this is the primary key
    ngay: datetime

    # Define the __getitem__ method to allow for easy access to the attributes
    def __getitem__(self, item):
        return getattr(self, item)


class VietnamIndex(Indexes, table=True):
    # The date, this is the primary key
    ngay: Optional[datetime] = Field(default=None, primary_key=True)

    # The stock index of vnindex
    vnindex: Optional[float] = Field(default=None)

    # The stock index of hnxindex
    hnxindex: Optional[float] = Field(default=None)

    # The stock index of upcom index
    upindex: Optional[float] = Field(default=None)

    # The stock index of vn30 index
    vn30: Optional[float] = Field(default=None)

    # The stock index of hnx30 index
    hnx30: Optional[float] = Field(default=None)

    model_config = ConfigDict(from_attributes=True)


class WorldIndex(Indexes, table=True):
    # The date, this is the primary key
    ngay: Optional[datetime] = Field(default=None, primary_key=True)

    # The stock index of BSE Sensex - India
    bsesn: Optional[float] = Field(default=None)

    # The stock index of Dow Jones - US
    dji: Optional[float] = Field(default=None)

    # The stock index of CAC 40 - France
    fchi: Optional[float] = Field(default=None)

    # The stock index of FTSE 100 - UK
    ftse: Optional[float] = Field(default=None)

    # The stock index of FTSE - Singapore
    ftwisgpl: Optional[float] = Field(default=None)

    # The stock index of DAX - Germany
    gdaxi: Optional[float] = Field(default=None)

    # The stock index of HANG SENG - Hong Kong
    hsi: Optional[float] = Field(default=None)

    # The stock index of Nasdaq - US
    ixic: Optional[float] = Field(default=None)

    # The stock index of FTSE - Malaysia
    klse: Optional[float] = Field(default=None)

    # The stock index of KOSPI - South Korea
    ks11: Optional[float] = Field(default=None)

    # The stock index of NIKKEI 225 - Japan
    n225: Optional[float] = Field(default=None)

    # The stock index of PSEi - Philippines
    psi: Optional[float] = Field(default=None)

    # The stock index of SET - Thailand
    seti: Optional[float] = Field(default=None)

    # The stock index of S&P 500 - US
    spx: Optional[float] = Field(default=None)

    # The stock index of SHANGHAI - China
    ssec: Optional[float] = Field(default=None)

    # The stock index of Euro Stoxx 50 - Europe
    stoxx50: Optional[float] = Field(default=None)

    # The stock index of CBOE Volatility - US
    vix: Optional[float] = Field(default=None)

    model_config = ConfigDict(from_attributes=True)


# Update the forward reference
VietnamIndex.model_rebuild()
WorldIndex.model_rebuild()
