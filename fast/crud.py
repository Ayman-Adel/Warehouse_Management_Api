from mysqlx import ColumnType
from sqlalchemy import column, null
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from . import models, schemas

# Branch CRUD Functions
#   C    R     U       D
# create read update delete


def get_branch(db: Session, branch_id: int):
    return db.query(models.Branch).filter(models.Branch.branch_id == branch_id).first()


def create_branch(db: Session, branch: schemas.BranchCreate):
    db_branch = models.Branch(**branch.model_dump())
    db.add(db_branch)
    db.commit()
    db.refresh(db_branch)
    return db_branch


def get_all_branches(skip: int, limit: int, db: Session):
    return db.query(models.Branch).offset(skip).limit(limit).all()


def update_branch(db: Session, branch_id: int, branch: schemas.BranchCreate):
    db_branch_update = db.query(models.Branch).filter(
        models.Branch.branch_id == branch_id).first()
    for key, value in branch.model_dump().items():
        setattr(db_branch_update, key, value)
    db.commit()
    db.refresh(db_branch_update)
    return db_branch_update


def delete_branch(db: Session, branch_id: int):
    db_branch_delete = db.query(models.Branch).filter(
        models.Branch.branch_id == branch_id).first()
    db.delete(db_branch_delete)
    db.commit()
    return db_branch_delete


# Employee CRUD Functions
def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.employee_id == employee_id).first()


def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(**employee.model_dump())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def get_all_employees(skip: int, limit: int, db: Session):
    return db.query(models.Employee).offset(skip).limit(limit).all()


def get_all_employees_emails(skip: int, db: Session):
    employees = db.query(models.Employee).offset(skip).all()
    return [str(employee.email) for employee in employees]


def update_employee(db: Session, employee_id: int, employee: schemas.EmployeeCreate):
    db_employee_update = db.query(models.Employee).filter(
        models.Employee.employee_id == employee_id).first()
    for key, value in employee.model_dump().items():
        setattr(db_employee_update, key, value)
    db.commit()
    db.refresh(db_employee_update)
    return db_employee_update


def delete_employee(db: Session, employee_id: int):
    db_employee_delete = db.query(models.Employee).filter(
        models.Employee.employee_id == employee_id).first()
    db.delete(db_employee_delete)
    db.commit()
    return db_employee_delete


# Tool CRUD Functions
def get_tool(db: Session, tool_id: int):
    return db.query(models.Tool).filter(models.Tool.tool_id == tool_id).options(joinedload(models.Tool.items)).first()


def create_tool(db: Session, tool: schemas.ToolCreate):
    db_tool = models.Tool(**tool.model_dump())
    db.add(db_tool)
    db.commit()
    db.refresh(db_tool)
    return db_tool


def get_all_tools(skip: int, limit: int, db: Session):
    return db.query(models.Tool).offset(skip).limit(limit).all()


def update_tool(db: Session, tool_id: int, tool: schemas.ToolCreate):
    db_tool_update = db.query(models.Tool).filter(
        models.Tool.tool_id == tool_id).first()
    for key, value in tool.model_dump().items():
        setattr(db_tool_update, key, value)
    db.commit()
    db.refresh(db_tool_update)
    return db_tool_update


def delete_tool(db: Session, tool_id: int):
    db_tool_delete = db.query(models.Tool).filter(
        models.Tool.tool_id == tool_id).first()
    db.delete(db_tool_delete)
    db.commit()
    return db_tool_delete


# Tool CRUD Functions
def get_item(db: Session, item_id: int):
    item = db.query(models.Item).filter(models.Item.item_id == item_id).options(joinedload(models.Item.tool)).first()
    return item


def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_all_items(skip: int, limit: int, db: Session):
    return db.query(models.Item).offset(skip).limit(limit).all()


def update_item(db: Session, item_id: int, item: schemas.ItemCreate):
    db_item_update = db.query(models.Item).filter(
        models.Item.item_id == item_id).first()
    for key, value in item.model_dump().items():
        setattr(db_item_update, key, value)
    db.commit()
    db.refresh(db_item_update)
    return db_item_update


def delete_item(db: Session, item_id: int):
    db_item_delete = db.query(models.Item).filter(
        models.Item.item_id == item_id).first()
    db.delete(db_item_delete)
    db.commit()
    return db_item_delete


# Add_item CRUD Functions
def get_additem(db: Session, add_item_id : int):
    return db.query(models.AddItem).filter(models.AddItem.add_item_id  == add_item_id ).first()


def create_additem(db: Session, additem: schemas.AddItemCreate):
    db_additem = models.AddItem(**additem.model_dump())
    db.add(db_additem )
    db.commit()
    db.refresh(db_additem )
    return db_additem 


def get_all_additems(skip: int, limit: int, db: Session):
    return db.query(models.AddItem).offset(skip).limit(limit).all()


def update_additem(db: Session, add_item_id):
    db_additem_update = (models.AddItem).filter(
        models.AddItem.add_item_id == add_item_id).first()
    db.add(db_additem_update)
    db.commit()
    db.refresh(db_additem_update)
    return db_additem_update


def delete_additem(db: Session, add_item_id):
    db_additem_delete = db.query(models.AddItem).filter(
        models.AddItem.add_item_id == add_item_id).first()
    db.delete(db_additem_delete)
    db.commit()
    return db_additem_delete

# Add_tool CRUD Functions
def get_addtool(db: Session, add_tool_id  : int):
    return db.query(models.AddTool).filter(models.AddTool.add_tool_id  == add_tool_id  ).first()


def create_addtool(db: Session, addtool: schemas.AddToolCreate):
    db_addtool = models.AddItem(**addtool.model_dump())
    db.add(db_addtool)
    db.commit()
    db.refresh(db_addtool)
    return db_addtool


def get_all_addtools(skip: int, limit: int, db: Session):
    return db.query(models.AddTool).offset(skip).limit(limit).all()


def update_addtool(db: Session, add_tool_id ):
    db_addtool_update = (models.AddTool).filter(
        models.AddTool.add_tool_id  == add_tool_id ).first()
    db.add(db_addtool_update)
    db.commit()
    db.refresh(db_addtool_update)
    return db_addtool_update


def delete_addtool(db: Session, add_tool_id ):
    db_addtool_delete = db.query(models.AddTool).filter(
        models.AddTool.add_tool_id  == add_tool_id ).first()
    db.delete(db_addtool_delete)
    db.commit()
    return db_addtool_delete

# Book CRUD Functions


def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.book_id == book_id).first()


def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    db_item = db.query(models.Item).filter(models.Item.item_id == db_book.item_id).first()
    if db_item :
      
        #if db_book.item_id is not None:
            #db_item.status = "Booked"
            
     return db_book


def get_all_books(skip: int, limit: int, db: Session):
    return db.query(models.Book).offset(skip).limit(limit).all()


def update_book(db: Session, book_id: int, book: schemas.BookCreate):
    db_book_update = db.query(models.Book).filter(
        models.Book.book_id == book_id).first()
    for key, value in book.model_dump().items():
        setattr(db_book_update, key, value)
    db.commit()
    db.refresh(db_book_update)
    return db_book_update


def delete_book(db: Session, book_id: int):
    db_book_delete = db.query(models.Book).filter(
        models.Book.book_id == book_id).first()
    db.delete(db_book_delete)
    db.commit()
    return db_book_delete

# Check_in CRUD Functions
def get_check_in(db: Session, check_id: int):
    return db.query(models.Check_in_out).filter(models.Check_in_out.check_id == check_id).first()


def create_check_in(db: Session, check_in_out: schemas.Check_in_out_Create):
    db_check_in_out = models.Check_in_out(**check_in_out.model_dump())
    db.add(db_check_in_out)
    db.commit()
    db.refresh(db_check_in_out)
    return db_check_in_out


def get_all_check_ins(skip: int, limit: int, db: Session):
    return db.query(models.Check_in_out).offset(skip).limit(limit).all()


def update_check_in(db: Session, check_id: int, check_in_out: schemas.Check_in_out):
    db_check_in_out_update = db.query(models.Check_in_out).filter(
        models.Check_in_out.check_id == check_id).first()
    for key, value in check_in_out.model_dump().items():
        setattr(db_check_in_out_update, key, value)
    db.commit()
    db.refresh(db_check_in_out_update)
    return db_check_in_out_update


def delete_check_in(db: Session, check_id: int):
    db_check_in_out_delete = db.query(models.Check_in_out).filter(
        models.Check_in_out.check_id == check_id).first()
    db.delete(db_check_in_out_delete)
    db.commit()
    return db_check_in_out_delete

# Check_out CRUD Functions
def get_check_out(db: Session, check_id: int):
    return db.query(models.Check_in_out).filter(models.Check_in_out.check_id == check_id).first()


def create_check_out(db: Session, check_in_out: schemas.Check_in_out_Create):
    db_check_in_out = models.Check_in_out(**check_in_out.model_dump())
    db.add(db_check_in_out)
    db.commit()
    db.refresh(db_check_in_out)
    db_item = db.query(models.Item).filter(models.Item.item_id == db_check_in_out.item_id).first()
    if db_item :

        if db_check_in_out.job_assigned is not None:
            db_item.status = db_check_in_out.job_assigned
            db_item.job_assigned = db_check_in_out.job_assigned
        elif db_check_in_out.company_lended is not None:
            db_item.status = db_check_in_out.company_lended
            db_item.company_lended = db_check_in_out.company_lended
    db.commit()
    db.refresh(db_item)
    return db_check_in_out


def get_all_check_outs(skip: int, limit: int, db: Session):
    return db.query(models.Check_in_out).offset(skip).limit(limit).all()


def update_check_out(db: Session, check_id: int, check_in_out: schemas.Check_in_out):
    db_check_in_out_update = db.query(models.Check_in_out).filter(
        models.Check_in_out.check_id == check_id).first()
    for key, value in check_in_out.model_dump().items():
        setattr(db_check_in_out_update, key, value)
    db.commit()
    db.refresh(db_check_in_out_update)
    return db_check_in_out_update


def delete_check_out(db: Session, check_id: int):
    db_check_in_out_delete = db.query(models.Check_in_out).filter(
        models.Check_in_out.check_id == check_id).first()
    db.delete(db_check_in_out_delete)
    db.commit()
    return db_check_in_out_delete


# Comment CRUD Functions
def get_comment(db: Session, comment_id: int):
    return db.query(models.Comment).filter(models.Comment.comment_id == comment_id).first()


def create_comment(db: Session, comment: schemas.CommentCreate):
    db_comment = models.Comment(**comment.model_dump())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def get_all_comments(skip: int, limit: int, db: Session):
    return db.query(models.Comment).offset(skip).limit(limit).all()


def update_comment(db: Session, comment_id: int, comment: schemas.CommentCreate):
    db_comment_update = db.query(models.Comment).filter(
        models.Comment.comment_id == comment_id).first()
    for key, value in comment.model_dump().items():
        setattr(db_comment_update, key, value)
    db.commit()
    db.refresh(db_comment_update)
    return db_comment_update


def delete_comment(db: Session, comment_id: int):
    db_comment_delete = db.query(models.Comment).filter(
        models.Comment.comment_id == comment_id).first()
    db.delete(db_comment_delete)
    db.commit()
    return db_comment_delete
