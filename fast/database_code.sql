CREATE TABLE IF NOT EXISTS `Tool` (
  `tool_id` INT  AUTO_INCREMENT NOT NULL,
  `tool_name` VARCHAR(50) NOT NULL,
  `image_link` VARCHAR(200) NOT NULL,
  `category_name` VARCHAR(50) NOT NULL,
  `details` VARCHAR(200) NOT NULL,
  `quantity` INT NOT NULL,
  `data_sheet_pdf_link` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`tool_id`)
);

CREATE TABLE IF NOT EXISTS `Item` (
  `item_id` INT AUTO_INCREMENT NOT NULL,
  `tool_id` INT NOT NULL,
  `branch_id` INT NOT NULL,
  `status` VARCHAR(100) NOT NULL,
  `job_assigned` VARCHAR(200) ,
  `company_lended` VARCHAR(50) ,
	PRIMARY KEY (`item_ID`),
	CONSTRAINT `fk_Item_Tool`
	FOREIGN KEY (`tool_id`)
	REFERENCES `Tool` (`tool_id`)
);

CREATE TABLE IF NOT EXISTS `Add` (
  `add_id` INT AUTO_INCREMENT NOT NULL,
  `item_id` INT NOT NULL ,
  `employee_id` INT NOT NULL,
  `check_in_date` DATE NOT NULL,
  `check_in_time` TIME NOT NULL,
  PRIMARY KEY (`add_id`),
  CONSTRAINT `fk_Add_Item`
   FOREIGN KEY (`item_id`)
	REFERENCES `Item` (`item_id`)
    
);

CREATE TABLE IF NOT EXISTS `Employee` (
  `employee_id` INT AUTO_INCREMENT NOT NULL,
  `branch_id` INT NOT NULL,
  `employee_name` VARCHAR(50) NOT NULL,
  `employee_phone_number` VARCHAR(50) NOT NULL,
  `role` VARCHAR(50) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`employee_id`)
);

ALTER TABLE `Add`
ADD CONSTRAINT `fk_Add_Employee`
FOREIGN KEY (`employee_id`)
REFERENCES `Employee` (`employee_id`);

CREATE TABLE IF NOT EXISTS `Branch` (
  `branch_id` INT AUTO_INCREMENT NOT NULL,
  `branch_name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`branch_id`)
);

ALTER TABLE `Item`
ADD CONSTRAINT `fk_Item_Branch`
FOREIGN KEY (`branch_id`)
REFERENCES `Branch` (`branch_id`);

ALTER TABLE `Employee`
ADD CONSTRAINT `fk_Employee_Branch`
FOREIGN KEY (`branch_id`)
REFERENCES `Branch` (`branch_id`);

CREATE TABLE IF NOT EXISTS `Check_in_out` (
  `check_id` INT AUTO_INCREMENT NOT NULL,
  `item_id` INT NOT NULL,
  `employee_id` INT NOT NULL,
  `check_in_date` DATE NOT NULL,
  `check_in_time` TIME NOT NULL,
  `check_out_date` DATE NOT NULL,
  `check_out_time` TIME NOT NULL,
  `estimated_Check_in_Date` DATE,
  PRIMARY KEY (`check_id`),
  CONSTRAINT `fk_Check_Item`
	FOREIGN KEY (`item_id`)
	REFERENCES `Item` (`item_id`),
  CONSTRAINT `fk_Check_Employee`
	FOREIGN KEY (`employee_id`)
	REFERENCES `Employee` (`employee_id`)
);


CREATE TABLE IF NOT EXISTS `Book` (
  `book_id` INT AUTO_INCREMENT NOT NULL,
  `item_id` INT NOT NULL,
  `employee_id` INT NOT NULL,
  `future_check_out_date` DATE NOT NULL,
  PRIMARY KEY (`book_id`),
  CONSTRAINT `fk_Book_Item`
	FOREIGN KEY (`item_id`)
	REFERENCES `Item` (`item_id`),
  CONSTRAINT `fk_Book_Employee`
	FOREIGN KEY (`employee_id`)
	REFERENCES `Employee` (`employee_id`)
);


CREATE TABLE IF NOT EXISTS `Comment` (
  `comment_id` INT AUTO_INCREMENT NOT NULL,
  `tool_id` INT NOT NULL,
  `employee_id` INT NOT NULL,
  `comment` VARCHAR(200) NOT NULL,
  `date` DATE NOT NULL,
  `time` TIME NOT NULL,
  `type` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`comment_id`),
  CONSTRAINT `fk_Comment_Tool`
	FOREIGN KEY (`tool_id`)
	REFERENCES `Tool` (`tool_id`),
  CONSTRAINT `fk_Comment_Employee`
	FOREIGN KEY (`employee_id`)
	REFERENCES `Employee` (`employee_id`)
);