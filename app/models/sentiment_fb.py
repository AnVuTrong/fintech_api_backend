from sqlmodel import SQLModel, Field
from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel


class SentimentFacebook(SQLModel, table=True):
    __tablename__ = "sentiment_facebook"
    id: Optional[str] = Field(default=None, primary_key=True)
    message: Optional[str] = Field(default=None)
    language: Optional[str] = Field(default=None)
    language_score: Optional[str] = Field(default=None)
    total_interactions: Optional[str] = Field(default=None)
    country: Optional[str] = Field(default=None)
    created_at: Optional[datetime] = Field(default=None)
    post_created_at: Optional[datetime] = Field(default=None)
    translated_message: Optional[str] = Field(default=None)
    topic_id: Optional[str] = Field(default=None)
    label: Optional[str] = Field(default=None)
    sentiment: Optional[int] = Field(default=None)

    def __getitem__(self, item):
        return getattr(self, item)


class SentimentUEHFB(SQLModel, table=True):
    __tablename__ = "sentiment_ueh_fb"
    id: Optional[str] = Field(default=None, primary_key=True)
    message: Optional[str] = Field(default=None)
    language: Optional[str] = Field(default=None)
    language_score: Optional[str] = Field(default=None)
    total_interactions: Optional[str] = Field(default=None)
    country: Optional[str] = Field(default=None)
    created_at: Optional[datetime] = Field(default=None)
    post_created_at: Optional[datetime] = Field(default=None)
    translated_message: Optional[str] = Field(default=None)
    topic_id: Optional[str] = Field(default=None)
    label: Optional[str] = Field(default=None)
    sentiment: Optional[int] = Field(default=None)

    def __getitem__(self, item):
        return getattr(self, item)


class SentimentUEHGG(SQLModel, table=True):
    __tablename__ = "sentiment_ueh_gg"
    id: Optional[str] = Field(default=None, primary_key=True)
    url: Optional[str] = Field(default=None)
    content: Optional[str] = Field(default=None)
    language: Optional[str] = Field(default=None)
    language_score: Optional[str] = Field(default=None)
    total_interactions: Optional[str] = Field(default=None)
    translated_content: Optional[str] = Field(default=None)
    summarized_content: Optional[str] = Field(default=None)
    created_at: Optional[datetime] = Field(default=None)
    post_create_at: Optional[datetime] = Field(default=None)
    topic_id: Optional[str] = Field(default=None)
    label: Optional[str] = Field(default=None)
    sentiment: Optional[int] = Field(default=None)

    def __getitem__(self, item):
        return getattr(self, item)


class SentimentFBResponse(BaseModel):
    sentiment_facebook_list: List[SentimentFacebook]
    average_sentiment: Optional[float]
    average_weighted_sentiment: Optional[float]


class SentimentUEHFBResponse(BaseModel):
    sentiment_ueh_fb_list: List[SentimentUEHFB]
    average_sentiment: Optional[float]
    average_weighted_sentiment: Optional[float]


class SentimentUEHGGResponse(BaseModel):
    sentiment_ueh_list: List[SentimentUEHGG]
    average_sentiment: Optional[float]
    average_weighted_sentiment: Optional[float]


# Update the forward reference
SentimentFacebook.model_rebuild()
SentimentUEHFB.model_rebuild()
SentimentUEHGG.model_rebuild()
