from sqlalchemy import Time, Date, Boolean, Column, ForeignKey, Integer, String, true
from sqlalchemy.orm import relationship
from fast.database import Base


class Branch(Base):
    __tablename__ = "branch"

    branch_id = Column(Integer, primary_key=True,
                       index=True, autoincrement=True)
    branch_name = Column(String, index=True)

    item = relationship("Item", back_populates="branch")


class Employee(Base):
    __tablename__ = "employee"

    employee_id = Column(Integer, primary_key=True,
                         index=True, autoincrement=True)
    branch_id = Column(Integer, ForeignKey(Branch.branch_id), index=True)
    employee_name = Column(String, index=True)
    employee_phone_number = Column(String, index=True)
    role = Column(String, index=True)
    password = Column(String, index=True)
    email = Column(String, index=True, unique=True)
    add = relationship("Add", back_populates="employee")
    book = relationship("Book", back_populates="employee")
    check_in_out = relationship("Check_in_out", back_populates="employee")
    comment = relationship("Comment", back_populates="employee")


class Tool(Base):
    __tablename__ = "tool"

    tool_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tool_name = Column(String, index=True)
    image_link = Column(String, index=True)
    category_name = Column(String)
    details = Column(String)
    quantity = Column(Integer)
    data_sheet_pdf_link = Column(String)


class Item(Base):
    __tablename__ = "item"

    item_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tool_id = Column(Integer, ForeignKey(Tool.tool_id), index=True)
    branch_id = Column(Integer, ForeignKey(Branch.branch_id), index=True)
    status = Column(String)
    job_assigned = Column(String)
    company_lended = Column(String)

    branch = relationship("Branch", back_populates="item")
    add = relationship("Add", back_populates="item")
    book = relationship("Book", back_populates="item")
    check_in_out = relationship("Check_in_out", back_populates="item")


class AddItem(Base):
    __tablename__ = "add_item"

    add_item_id = Column(Integer, primary_key=True, index=True,
                    default=1, autoincrement=True)
    item_id = Column(Integer, ForeignKey(Item.item_id), index=True)
    employee_id = Column(Integer, ForeignKey(Employee.employee_id), index=True)
    check_in_date = Column(Date, index=True)
    check_in_time = Column(Time, index=True)

    item = relationship("Item", back_populates="add_item")
    employee = relationship("Employee", back_populates="add_item")


class AddTool(Base):
    __tablename__ = "add_tool"

    add_tool_id = Column(Integer, primary_key=True, index=True,
                    default=1, autoincrement=True)
    tool_id = Column(Integer, ForeignKey(Item.item_id), index=True)
    employee_id = Column(Integer, ForeignKey(Employee.employee_id), index=True)
    check_in_date = Column(Date, index=True)
    check_in_time = Column(Time, index=True)

    item = relationship("Item", back_populates="add_tool")
    employee = relationship("Employee", back_populates="add_tool")

class Book(Base):
    __tablename__ = "book"

    book_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    item_id = Column(Integer, ForeignKey(Item.item_id), index=True)
    employee_id = Column(Integer, ForeignKey(Employee.employee_id), index=True)
    future_check_out_date = Column(Date)

    item = relationship("Item", back_populates="book")
    employee = relationship("Employee", back_populates="book")


class Check_in_out(Base):
    __tablename__ = "check_in_out"

    check_id = Column(Integer, primary_key=True,
                      index=True, autoincrement=True)
    item_id = Column(Integer, ForeignKey(Item.item_id), index=True)
    employee_id = Column(Integer, ForeignKey(Employee.employee_id), index=True)
    check_in_date = Column(Date, index=True)
    check_out_date = Column(Date, index=True)
    check_in_time = Column(Time, index=True)
    check_out_time = Column(Time, index=True)
    estimated_Check_in_Date = Column(Date, index=True)

    item = relationship("Item", back_populates="check_in_out")
    employee = relationship("Employee", back_populates="check_in_out")


class Comment(Base):
    __tablename__ = "comment"

    comment_id = Column(Integer, primary_key=True,
                        index=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey(Employee.employee_id), index=True)
    comment = Column(String, index=True)
    date = Column(Date, index=True)
    time = Column(Time, index=True)
    type = Column(String, index=True)

    employee = relationship("Employee", back_populates="comment")
