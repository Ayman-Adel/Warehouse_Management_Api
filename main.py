from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List
from fast import models, schemas, crud
from fast.endpoints import *
from fast.database import SessionLocal, engine
from auth.jwt_handler import signjwt
import uvicorn

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {'Hello': 'World'}

# Branch Api functions


@app.post(f"/{branches}/""",) #response_model=schemas.Branch)
def create_branch(branch: schemas.BranchCreate, db: Session = Depends(get_db)):
    db_branch = crud.create_branch(db, branch=branch)
    if db_branch is None:
        raise HTTPException(
            status_code=400, detail="Branch_id is already exists")
    return "Branch has been created"


@app.get(f"/{branches}/""{branch_id}",) #response_model=schemas.Branch)
def read_branch(branch_id: int, db: Session = Depends(get_db)):
    db_branch = crud.get_branch(db, branch_id=branch_id)
    if db_branch is None:
        raise HTTPException(status_code=404, detail="Branch not found")
    return db_branch


@app.get(f"/{branches}/""",) #response_model=List[schemas.Branch])
def read_all_branches(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    branches = crud.get_all_branches(skip, limit, db)
    return branches


@app.delete(f"/{branches}/""{branch_id}",) #response_model=schemas.Branch)
def delete_branch(branch_id: int, db: Session = Depends(get_db)):
    db_delete = crud.delete_branch(db, branch_id=branch_id)
    if db_delete is None:
        raise HTTPException(status_code=404, detail="Branch not found")
    return "Branch has been deleted"


@app.put(f"/{branches}/""{branch_id}",) #response_model=schemas.Branch)
def update_branch(branch_id: int, branch: schemas.BranchCreate, db: Session = Depends(get_db)):
    db_update = crud.update_branch(db, branch_id=branch_id, branch=branch)
    if db_update is None:
        raise HTTPException(status_code=404, detail="Branch not found")
    return "Branch has been updated"


# Employee Api Functions
    # will be deleted and replaced by signup
@app.post(f"/{employees}/""",) #response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = crud.create_employee(db, employee=employee)
    if db_employee is None:
        raise HTTPException(
            status_code=400, detail="Employee_id is already exists")
    return db_employee


@app.get(f"/{employees}/""{employee_id}",) #response_model=schemas.Employee)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee


@app.get(f"/{employees}/""",) #response_model=List[schemas.Employee])
def read_all_employees(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    employees = crud.get_all_employees(skip, limit, db)
    return employees


# response_model=schemas.Employee)
@app.delete(f"/{employees}/""{employee_id}", )
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    db_delete = crud.delete_employee(db, employee_id=employee_id)
    if db_delete is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return "Employee has been deleted"


@app.put(f"/{employees}/""{employee_id}",) #response_model=schemas.Employee)
def update_employee(employee_id: int, employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    db_update = crud.update_employee(
        db, employee_id=employee_id, employee=employee)
    if db_update is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return "Employee has been updated"


# sinup
@app.post(f"/employee/sinup", tags=["singup"])
def employee_signup(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = crud.create_employee(db, employee=employee)
    if db_employee is None:
        raise HTTPException(
            status_code=400, detail="Employee_id is already exists")
    return signjwt(employee.email)


def check_employee(employee: schemas.EmployeeLogin, skip: int, db: Session):
    employees = crud.get_all_employees_emails(db=db, skip=skip)
    for email in employees:
        if email == employee.email:
            return True
    return False


# login
@app.post(f"/employee/sinin", tags=["sign in"])
def employee_login(employee: schemas.EmployeeLogin, db: Session = Depends(get_db)):
    if (check_employee(employee=employee, db=db, skip=0)):
        return signjwt(employee.email)
    return {"error": "invalid email address"}


# Tool Api Functions
@app.post(f"/{tools}/""",) #response_model=schemas.Tool)
def create_tool(tool: schemas.ToolCreate, db: Session = Depends(get_db)):
    db_tool = crud.create_tool(db, tool=tool)
    if db_tool is None:
        raise HTTPException(
            status_code=400, detail="Tool_id is already exists")
    return "Tool has been created"


@app.get(f"/{tools}/""{tool_id}",) #response_model=schemas.Tool)
def read_tool(tool_id: int, db: Session = Depends(get_db)):
    db_tool = crud.get_tool(db, tool_id=tool_id)
    if db_tool is None:
        raise HTTPException(status_code=404, detail="Tool not found")
    return db_tool


@app.get(f"/{tools}/""",) #response_model=List[schemas.Tool])
def read_all_tools(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tools = crud.get_all_tools(skip, limit, db)
    return tools


@app.delete(f"/{tools}/""{tool_id}}",) #response_model=schemas.Tool)
def delete_tool(tool_id: int, db: Session = Depends(get_db)):
    db_delete = crud.delete_tool(db, tool_id=tool_id)
    if db_delete is None:
        raise HTTPException(status_code=404, detail="Tool not found")
    return "Tool has been deleted"


@app.put(f"/{tools}/""{tool_id}}",) #response_model=schemas.Tool)
def update_tool(tool_id: int, tool: schemas.ToolCreate, db: Session = Depends(get_db)):
    db_update = crud.update_tool(db, tool_id=tool_id, tool=tool)
    if db_update is None:
        raise HTTPException(status_code=404, detail="Tool not found")
    return "Tool has been updated"

# Item Api Function
@app.post(f"/{items}/""",) #response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = crud.create_item(db, item=item)
    if db_item is None:
        raise HTTPException(
            status_code=400, detail="Item_id is already exists")
    return "Item has been created"


@app.get(f"/{items}/""{item_id}",) #response_model=schemas.Item)
def read_item(item_id: int ,db: Session = Depends(get_db)):
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@app.get(f"/{items}/""",) #response_model=List[schemas.Item])
def read_all_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = crud.get_all_items(skip, limit, db)
    return items


@app.delete(f"/{items}/""{item_id}}",) #response_model=schemas.Item)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_delete = crud.delete_item(db, item_id=item_id)
    if db_delete is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return "Item has been deleted"


@app.put(f"/{items}/""{item_id}",) #response_model=schemas.Item)
def update_item(item_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_update = crud.update_item(db, item_id=item_id, item=item)
    if db_update is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return "Item has been updated"


# Additem Api functions
@app.post(f"/{additems}""/", response_model=schemas.AddItem)
def create_additem(additem: schemas.AddItemCreate, db: Session = Depends(get_db)):
     db_add = crud.create_additem(db, additem=additem)
     if db_add is None:
        raise HTTPException(status_code=400, detail="Add_id is already exists")
     return "Additem has been created"


@app.get(f"/{additems}""/{add_item_id}",) #  response_model=schemas.AddItem)
def read_additem(add_item_id: int, db: Session = Depends(get_db)):
     db_additem = crud.get_additem(db, add_item_id=add_item_id)
     if db_additem is None:
         raise HTTPException(status_code=404, detail="Add not found")
     return db_additem


@app.get(f"/{additems}""/",) # response_model=List[schemas.AddItem])
def read_all_additems(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
     additems = crud.get_all_additems(skip, limit, db)
     return additems


@app.delete(f"/{additems}""/{add_item_id}",) #response_model=schemas.AddItem)
def delete_additem(add_item_id: int, db: Session = Depends(get_db)):
     db_delete = crud.delete_additem(db, add_item_id=add_item_id)
     if db_delete is None:
         raise HTTPException(status_code=404, detail="Add not found")
     return "Additem has been deleted"


@app.put(f"/{additems}""/{add_item_id}", response_model=schemas.AddItem)
def update_additem(add_item_id: int, db: Session = Depends(get_db)):
     db_update = crud.update_additem(db, add_item_id=add_item_id)
     if db_update is None:
        raise HTTPException(status_code=404, detail="Add not found")
     return "Additem has been updated"

# Addtool Api functions
@app.post(f"/{addtools}""/", response_model=schemas.AddTool)
def create_addtool(addtool: schemas.AddToolCreate, db: Session = Depends(get_db)):
     db_add = crud.create_addtool(db, addtool=addtool)
     if db_add is None:
        raise HTTPException(status_code=400, detail="Add_id is already exists")
     return "Addtool has been created"


@app.get(f"/{addtools}""/{add_tool_id}",) #  response_model=schemas.AddTool)
def read_addtool(add_tool_id: int, db: Session = Depends(get_db)):
     db_addtool = crud.get_addtool(db, add_tool_id=add_tool_id)
     if db_addtool is None:
         raise HTTPException(status_code=404, detail="Add not found")
     return db_addtool


@app.get(f"/{addtools}""/",) # response_model=List[schemas.AddTool])
def read_all_addtools(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
     addtools = crud.get_all_addtools(skip, limit, db)
     return addtools


@app.delete(f"/{addtools}""/{add_tool_id}",) #response_model=schemas.AddTool)
def delete_addtool(add_tool_id: int, db: Session = Depends(get_db)):
     db_delete = crud.delete_addtool(db, add_tool_id=add_tool_id)
     if db_delete is None:
         raise HTTPException(status_code=404, detail="Add not found")
     return "Addtool has been deleted"


@app.put(f"/{addtools}""/{add_tool_id}", response_model=schemas.AddTool)
def update_addtool(add_tool_id: int, db: Session = Depends(get_db)):
     db_update = crud.update_addtool(db, add_tool_id=add_tool_id)
     if db_update is None:
        raise HTTPException(status_code=404, detail="Add not found")
     return "Addtool has been updated"


# Book Api Functions
@app.post(f"/{books}/""",) #response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = crud.create_book(db, book=book)
    if db_book is None:
        raise HTTPException(
            status_code=400, detail="Book_id is already exists")
    return "Book has been created"
# Read Book


@app.get(f"/{books}/""{book_id}",) #response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

# Read All Books


@app.get(f"/{books}/""",) #response_model=List[schemas.Book])
def read_all_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    books = crud.get_all_books(skip, limit, db)
    return books


@app.delete(f"/{books}/""{book_id}",) #response_model=schemas.Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_delete = crud.delete_book(db, book_id=book_id)
    if db_delete is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return "Book has been deleted"


@app.put(f"/{books}/""{book_id}",) #response_model=schemas.Book)
def update_book(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_update = crud.update_book(db, book_id=book_id, book=book)
    if db_update is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return "Book has been updated"


# Check_in Api functions
@app.post(f"/{check_ins}/""",) #response_model=schemas.Check_in_out)
def create_check_in(check_in_out: schemas.Check_in_out_Create, db: Session = Depends(get_db)):
    db_check_in = crud.create_check_in(db, check_in_out=check_in_out)
    if db_check_in is None:
        raise HTTPException(
            status_code=400, detail="Check_in_id is already exists")
    return "Check_in has been created"


# response_model=schemas.Check_in_out)
@app.get(f"/{check_ins}/""{check_id}", )
def read_check_in(check_id: int, db: Session = Depends(get_db)):
    db_check_in = crud.get_check_in(db, check_id=check_id)
    if db_check_in is None:
        raise HTTPException(status_code=404, detail="Check_innot found")
    return db_check_in


@app.get(f"/{check_ins}/""",) #response_model=List[schemas.Check_in_out])
def read_all_check_ins(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    check_ins = crud.get_all_check_ins(skip, limit, db)
    return check_ins



@app.delete(f"/{check_ins}/""{check_id}",) # response_model=schemas.Check_in_out))
def delete_check_in(check_id: int, db: Session = Depends(get_db)):
    db_delete = crud.delete_check_in(db, check_id=check_id)
    if db_delete is None:
        raise HTTPException(status_code=404, detail="Check_in not found")
    return "Check_in has been deleted"



@app.put(f"/{check_ins}/""{check_id}",) # response_model=schemas.Check_in_out))
def update_check_in(check_id: int, check_in_out: schemas.Check_in_out, db: Session = Depends(get_db)):
    db_update = crud.update_check_in(
        db, check_id=check_id, check_in_out=check_in_out)
    if db_update is None:
        raise HTTPException(status_code=404, detail="Check_in not found")
    return "Check_in has been updated"

# Check_out Api functions
@app.post(f"/{check_outs}/""",) #response_model=schemas.Check_in_out)
def create_check_out(check_in_out: schemas.Check_in_out_Create, db: Session = Depends(get_db)):
    db_check_out = crud.create_check_out(db, check_in_out=check_in_out)
    if db_check_out is None:
        raise HTTPException(
            status_code=400, detail="Check_out_id is already exists")
    return "Check_out has been created"


# response_model=schemas.Check_in_out)
@app.get(f"/{check_outs}/""{check_id}", )
def read_check_out(check_id: int, db: Session = Depends(get_db)):
    db_check_out = crud.get_check_out(db, check_id=check_id)
    if db_check_out is None:
        raise HTTPException(status_code=404, detail="Check_out not found")
    return db_check_out


@app.get(f"/{check_outs}/""",) #response_model=List[schemas.Check_in_out])
def read_all_check_outs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    check_outs = crud.get_all_check_outs(skip, limit, db)
    return check_outs



@app.delete(f"/{check_outs}/""{check_id}",) # response_model=schemas.Check_in_out))
def delete_check_out(check_id: int, db: Session = Depends(get_db)):
    db_delete = crud.delete_check_out(db, check_id=check_id)
    if db_delete is None:
        raise HTTPException(status_code=404, detail="Check_out not found")
    return "Check_out has been deleted"



@app.put(f"/{check_outs}/""{check_id}",) # response_model=schemas.Check_in_out))
def update_check_out(check_id: int, check_in_out: schemas.Check_in_out, db: Session = Depends(get_db)):
    db_update = crud.update_check_out(
        db, check_id=check_id, check_in_out=check_in_out)
    if db_update is None:
        raise HTTPException(status_code=404, detail="Check_out not found")
    return "Check_out has been updated"


# Comment Api Functions
@app.post(f"/{comments}/""",) #response_model=schemas.Comment)
def create_comment(comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    db_comment = crud.create_comment(db, comment=comment)
    if db_comment is None:
        raise HTTPException(
            status_code=400, detail="Comment_id is already exists")
    return "Comment has been created"


@app.get(f"/{comments}/""{comment_id}",) #response_model=schemas.Comment)
def read_comment(comment_id: int, db: Session = Depends(get_db)):
    db_comment = crud.get_comment(db, comment_id=comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment


@app.get(f"/{comments}/""",) #response_model=List[schemas.Comment])
def read_all_comments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    comments = crud.get_all_comments(skip, limit, db)
    return comments


@app.delete(f"/{comments}/""{comment_id}",) #response_model=schemas.Comment)
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    db_delete = crud.delete_comment(db, comment_id=comment_id)
    if db_delete is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return "Comment has been deleted"


@app.put(f"/{comments}/""{comment_id}",) #response_model=schemas.Comment)
def update_comment(comment_id: int, comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    db_update = crud.update_comment(db, comment_id=comment_id, comment=comment)
    if db_update is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return "Comment has been updated"




# auth
# register
# login
# logout
# admin prev

# emp -> admin
# add insert tools
# delete direct access on add tables

# brook check  into 2 stages
# stage in stage out

# redesign messages
