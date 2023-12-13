from sqlalchemy.orm import Session

from . import models, schemas

# Branch CRUD Functions
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
    db_branch_update = db.query(models.Branch).filter(models.Branch.branch_id == branch_id).first()
    for key, value in branch.model_dump().items():
        setattr(db_branch_update, key, value)
    db.commit()
    db.refresh(db_branch_update)
    return db_branch_update

def delete_branch(db: Session, branch_id: int):
    db_branch_delete = db.query(models.Branch).filter(models.Branch.branch_id == branch_id).first()
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

def update_employee(db: Session, employee_id: int, employee: schemas.EmployeeCreate):
    db_employee_update = db.query(models.Employee).filter(models.Employee.employee_id == employee_id).first()
    for key, value in employee.model_dump().items():
        setattr(db_employee_update, key, value)
    db.commit()
    db.refresh(db_employee_update)
    return db_employee_update

def delete_employee(db: Session, employee_id: int):
    db_employee_delete = db.query(models.Employee).filter(models.Employee.employee_id == employee_id).first()
    db.delete(db_employee_delete)
    db.commit()
    return db_employee_delete



# Tool CRUD Functions
def get_tool(db: Session, tool_id: int):
    return db.query(models.Tool).filter(models.Tool.tool_id == tool_id).first()

def create_tool(db: Session, tool: schemas.ToolCreate):
    db_tool = models.Tool(**tool.model_dump())
    db.add(db_tool)
    db.commit()
    db.refresh(db_tool)
    return db_tool

def get_all_tools(skip: int, limit: int, db: Session):
    return db.query(models.Tool).offset(skip).limit(limit).all()

def update_tool(db: Session, tool_id: int, tool: schemas.ToolCreate):
    db_tool_update = db.query(models.Tool).filter(models.Tool.tool_id == tool_id).first()
    for key, value in tool.model_dump().items():
        setattr(db_tool_update, key, value)
    db.commit()
    db.refresh(db_tool_update)
    return db_tool_update

def delete_tool(db: Session, tool_id: int):
    db_tool_delete = db.query(models.Tool).filter(models.Tool.tool_id == tool_id).first()
    db.delete(db_tool_delete)
    db.commit()
    return db_tool_delete



#Tool CRUD Functions
def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.item_id == item_id).first()

def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_all_items(skip: int, limit: int, db: Session):
    return db.query(models.Item).offset(skip).limit(limit).all()

def update_item(db: Session, item_id: int, item: schemas.ItemCreate):
    db_item_update = db.query(models.Item).filter(models.Item.item_id == item_id).first()
    for key, value in item.model_dump().items():
        setattr(db_item_update, key, value)
    db.commit()
    db.refresh(db_item_update)
    return db_item_update

def delete_item(db: Session, item_id: int):
    db_item_delete = db.query(models.Item).filter(models.Item.item_id == item_id).first()
    db.delete(db_item_delete)
    db.commit()
    return db_item_delete


# Add CRUD Functions
def get_add(db: Session, add_id: int):
    return db.query(models.Add).filter(models.Add.add_id == add_id).first()

def create_add(db : Session ,add :schemas.AddCreate):
    db_add = models.Add(**add.model_dump())
    db.add(db_add)
    db.commit()
    db.refresh(db_add)
    return db_add

def get_all_adds( skip: int , limit: int , db : Session  ):
    return db.query(models.Add).offset(skip).limit(limit).all()

def update_add(db : Session, add_id):
    db_add_update = (models.Add).filter(models.Add.add_id == add_id).first()
    db.add(db_add_update)
    db.commit()
    db.refresh(db_add_update)
    return db_add_update

def delete_add(db : Session, add_id):
    db_add_delete = db.query(models.Add).filter(models.Add.add_id == add_id).first()
    db.delete(db_add_delete)
    db.commit()
    return db_add_delete

# Book CRUD Functions
def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.book_id == book_id).first()

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_all_books(skip: int, limit: int, db: Session):
    return db.query(models.Book).offset(skip).limit(limit).all()

def update_book(db: Session, book_id: int, book: schemas.BookCreate):
    db_book_update = db.query(models.Book).filter(models.Book.book_id == book_id).first()
    for key, value in book.model_dump().items():
        setattr(db_book_update, key, value)
    db.commit()
    db.refresh(db_book_update)
    return db_book_update

def delete_book(db: Session, book_id: int):
    db_book_delete = db.query(models.Book).filter(models.Book.book_id == book_id).first()
    db.delete(db_book_delete)
    db.commit()
    return db_book_delete


# Check_in_out CRUD Functions
def get_check_in_out(db: Session, check_id: int):
    return db.query(models.Check_in_out).filter(models.Check_in_out.check_id == check_id).first()

def create_check_in_out(db: Session, check_in_out: schemas.Check_in_out):
    db_check_in_out = models.Check_in_out(**check_in_out.model_dump())
    db.add(db_check_in_out)
    db.commit()
    db.refresh(db_check_in_out)
    return db_check_in_out

def get_all_check_in_outs(skip: int, limit: int, db: Session):
    return db.query(models.Check_in_out).offset(skip).limit(limit).all()

def update_check_in_out(db: Session, check_id: int, check_in_out: schemas.Check_in_out):
    db_check_in_out_update = db.query(models.Check_in_out).filter(models.Check_in_out.check_id == check_id).first()
    for key, value in check_in_out.model_dump().items():
        setattr(db_check_in_out_update, key, value)
    db.commit()
    db.refresh(db_check_in_out_update)
    return db_check_in_out_update

def delete_check_in_out(db: Session, check_id: int):
    db_check_in_out_delete = db.query(models.Check_in_out).filter(models.Check_in_out.check_id == check_id).first()
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
    db_comment_update = db.query(models.Comment).filter(models.Comment.comment_id == comment_id).first()
    for key, value in comment.model_dump().items():
        setattr(db_comment_update, key, value)
    db.commit()
    db.refresh(db_comment_update)
    return db_comment_update

def delete_comment(db: Session, comment_id: int):
    db_comment_delete = db.query(models.Comment).filter(models.Comment.comment_id == comment_id).first()
    db.delete(db_comment_delete)
    db.commit()
    return db_comment_delete









