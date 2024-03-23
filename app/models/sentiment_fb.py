from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class SentimentFacebook(SQLModel, table=True):
    __tablename__ = "sentiment_facebook"
    # id: Optional[int] = Field(default=None, primary_key=True)
    # message: str = Field(default=None)
    # language: str = Field(default=None)
    # language_score: str = Field(default=None)
    # total_interactions: str = Field(default=None)
    # country: str = Field(default=None)
    # post_created_date: str = Field(default=None)
    # post_created_time: str = Field(default=None)
    # translated_message: str = Field(default=None)
    # topic_id: int = Field(default=None)
    # sentiment: Optional[str] = Field(default=None)

    id: Optional[int] = Field(default=None, primary_key=True)
    message: Optional[str] = Field(default=None)
    language: Optional[str] = Field(default=None)
    language_score: Optional[str] = Field(default=None)
    total_interactions: Optional[str] = Field(default=None)
    country: Optional[str] = Field(default=None)
    post_created_date: Optional[datetime] = Field(default=None)
    post_created_time: Optional[str] = Field(default=None)
    translated_message: Optional[str] = Field(default=None)
    topic_id: Optional[int] = Field(default=None)
    label: Optional[str] = Field(default=None)

    def __getitem__(self, item):
        return getattr(self, item)


# Update the forward reference
SentimentFacebook.model_rebuild()
