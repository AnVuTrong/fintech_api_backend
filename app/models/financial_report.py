"""
In this file, we will define the class bctc (financial report)
"""
from sqlmodel import Field, SQLModel, Relationship
from typing import Optional


# Define the bctc model class that inherits from the base class
class FinancialReportBase(SQLModel):
    # We use UUID as the primary key
    id: str

    # The stock quote code
    code: str

    # The quarter of the financial report
    quy: int

    # The year of the financial report
    nam: int

    # The format of the financial report
    format: str

    # Define the __getitem__ method to allow for easy access to the attributes
    def __getitem__(self, item):
        return getattr(self, item)


# Define the bctc model class that inherits from the base class
class BalanceSheet(FinancialReportBase, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    content: str

class IncomeStatement(FinancialReportBase, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    content: str

class CashFlowStatement(FinancialReportBase, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    content: str

# Update the forward reference
BalanceSheet.model_rebuild()
IncomeStatement.model_rebuild()
CashFlowStatement.model_rebuild()
