from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import date, time

from sqlalchemy import null


class BranchBase(BaseModel):
    branch_name: str


class BranchCreate(BranchBase):
    pass


class Branch(BranchBase):
    branch_id: int

    class Config:
        from_attributes = True

class CommentBase(BaseModel):
    employee_id: int
    item_id : int
    comment: str
    type: str


class CommentCreate(CommentBase):
    pass


class Comment(CommentBase):
    comment_id: int
    date: date
    time: time

    class Config:
        from_attributes = True

class Check_In_Out_Base(BaseModel):
    item_id: int
    employee_id: int
    estimated_Check_in_Date: date
    check_out_date: date
    check_out_time: time
    job_assigned: Optional[str]  = Field(default=null())
    company_lended: Optional[str] = Field(default=null())



class Check_in_out_Create(Check_In_Out_Base):
    pass


class Check_in_out(Check_In_Out_Base):
    check_in_date: date
    check_in_time: time
    check_id: int

    class Config:
        from_attributes = True

class BookBase(BaseModel):
    item_id: int
    employee_id: int
    future_check_out_date: date


class BookCreate(BookBase):
    pass


class Book(BookBase):
    book_id: int

    class Config:
        from_attributes = True



class EmployeeBase(BaseModel):
    branch_id: int
    role: str = "user"
    employee_name: str
    employee_phone_number: str
    password: str
    email: str


class EmployeeCreate(EmployeeBase):
    pass


class Employee(EmployeeBase):
    employee_id: int
    comments: List["Comment"] = []
    check_in_outs: List["Check_in_out"] = []
    books: List["Book"] = []
    add_item: List["AddItem"] = []
    add_tool: List["AddTool"] = []

    class Config:
        from_attributes = True


class EmployeeLogin(BaseModel):
    email: str = Field(default=None)
    password: str = Field(default=None)

    class Config:
        from_attributes = True


class ToolBase(BaseModel):
    tool_name: str
    image_link: str
    category_name: str
    details: str
    quantity: int
    data_sheet_pdf_link: str


class ToolCreate(ToolBase):
    pass


class Tool(ToolBase):
    tool_id: int
    items: List["Item"] = []

    class Config:
        from_attributes = True


class ItemBase(BaseModel):
    tool_id: int
    branch_id: int
    status: str
    

class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    item_id: int
    job_assigned: Optional[str] = Field(default=null())
    company_lended: Optional[str] = Field(default=null())
    comments: List["Comment"] = []
    check_in_outs: List["Check_in_out"] = []
    book: Optional["Book"]

    class Config:
        from_attributes = True


class AddItemBase(BaseModel):
    item_id: int
    employee_id: int


class AddItemCreate(AddItemBase):
    pass


class AddItem(AddItemBase):
    add_item_id: int
    check_in_date: date
    check_in_time: time
    items: Item
    employee: Employee

    class Config:
        from_attributes = True


class AddToolBase(BaseModel):
    tool_id: int
    employee_id: int


class AddToolCreate(AddToolBase):
    pass


class AddTool(AddToolBase):
    add_tool_id: int
    check_in_date: date
    check_in_time: time
    tool: Tool
    employee: Employee

    class Config:
        from_attributes = True






