from datetime import datetime

from sqlmodel import SQLModel, Field
from typing import Optional


class Sentiment(SQLModel, table=True):
	id: str = Field(default=None, primary_key=True)
	date: datetime = Field(index=True)
	code: str = Field(index=True)
	sentiment_1d: Optional[float]
	sentiment_3d: Optional[float]
	sentiment_1w: Optional[float]
	sentiment_1m: Optional[float]

	class Config:
		from_attributes = True
