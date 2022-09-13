# Programming Assignment 1, CS242
## By- Achintya Gupta, Roll no. 210101005


## Question 1: Awk program
### Files included: 210101005.awk, inventory.txt

### How to run:
- Have 210101005.awk and inventory.txt in same directory 
- Open the terminal in a Linux based OS
- Open the directory in which the files have been stored
- Run the command on terminal: awk -f 210101005.awk inventory.txt

### List of Steps taken:
- Columns were stored in different variables for better readability
- If else statement used to find if an item should be ordered or not.
- Find order amount using the given definition
- Print everything that has been asked in the question

### Variable guide:
- pa_partnum: Part Number	
- pc_price: Price
- qon_Quan_On_Hand: Quantity on Hand
- rp_ReOrder_Pnt: Reorder point
- mo_Min_Order: Minimum Order
- oa_Order_Amt: Order Amount


## Question 2: Bash script
### Files included: 210101005.sh, EMPLOYEE.txt

### How to run: 
- Have 210101005.sh and EMPLOYEE.txt in the same directory  
- Open the terminal in a Linux based OS  
- Open the directory in which the files have been stored  
- Run the following commands on terminal:   
    1. chmod u+x 210101005.sh  
    2. ./210101005.sh  
    First command makes an executable file from bash script and second command runs it to print the output

### List of steps taken:
- All Column Names printed  with 16 spacing each to keep them aligned in a table, - sign is for left alignment
- cat < filename >(concatenate) statement opens and reads data from EMPLOYEE.txt 
- While statement reads line by line from the file and the variables take each word from the line to divide them column wise
- If conditions to check if hours worked >= 40 and exempt value "N" so that we can find if the person is eligible for overtime or not
- Base pay is calculated using the bash calculator (bc) as bash otherwise does not support floating point arithmetic
- Overtime is the extra payment over the base pay made to the employee. Employee is given 1.5 times the pay rate for each hour worked over 40 hours, so the overtime will be 0.5 times the pay rate for each hour as base pay already includes 1 time the pay rate for each hour
- "scale=2" defines the precision of floating point calculation, here upto 2 decimal places.
- Total pay is the sum of overtime and base pay

### Variable guide
- empNum : Employee number
- deptName : Department
- payRate : Pay rate per hour
- exempt : Exempt value (Y/N)
- hrsWorked : Number of hours worked
- base : Base pay = hrsWorked*payRate
- OT_overtime : Overtime paid = 0.5*(hrsWorked-40)*payRate
- totalPay : Total pay of the employee= base+OT_overtime