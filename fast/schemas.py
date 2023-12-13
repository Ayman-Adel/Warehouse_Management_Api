from pydantic import BaseModel
from datetime import date, time

class BranchBase(BaseModel):
    branch_name: str

class BranchCreate(BranchBase):
    pass

class Branch(BranchBase):
    branch_id: int

    class Config:
        from_attributes = True


class EmployeeBase(BaseModel):
    branch_id: int
    employee_name: str
    employee_phone_number: str
    role: str
    password: str
    email:str

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    employee_id: int

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

    class Config:
        from_attributes = True

class ItemBase(BaseModel):
    tool_id: int
    branch_id: int
    status: str
    job_assigned: str
    company_lended: str

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    item_id: int

    class Config:
        from_attributes = True



class AddItemBase(BaseModel):
    item_id: int
    employee_id: int
    check_in_date: date
    check_in_time: time
class AddItemCreate(AddItemBase):
    pass

class AddItem(AddItemBase):
    add_item_id: int

    class Config:
        from_attributes = True



class AddToolBase(BaseModel):
    tool_id: int
    employee_id: int
    check_in_date: date
    check_in_time: time
class AddToolCreate(AddToolBase):
    pass

class AddTool(AddToolBase):
    add_tool_id: int

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



class Check_In_Out_Base(BaseModel):
    item_id: int
    employee_id: int
    check_in_date: date
    check_out_date: date
    check_in_time: time
    check_out_time: time
    estimated_Check_in_Date: date

class Check_in_out_Create(Check_In_Out_Base):
    pass

class Check_in_out(Check_In_Out_Base):
    check_id: int

    class Config:
        from_attributes = True

class CommentBase(BaseModel):
    employee_id: int
    comment: str
    date: date
    time: time
    type: str

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    comment_id : int
    class Config:
        from_attributes = True




