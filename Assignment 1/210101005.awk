BEGIN{ 
print "____________________________________________________________________________\n";
print "\nProgramming Assignment 1, Q1 by Achintya Gupta, Roll No. 210101005\n"; 
print "____________________________________________________________________________\n";
print "\t\t\t\tINVENTORY REPORT\n";
print"----------------------------------------------------------------------------"; 
print "Part_no  Price  Quantity_On_Hand  Reorder_Point  Minimum_Order  Order_Amt";
print"----------------------------------------------------------------------------"} #Introduction and column names printed on the screen


#Variable names added to code for better readability without opening data file
{pa_partnum= $1}		
{pc_price= $2}
{qon_Quan_On_Hand= $3}
{rp_ReOrder_Pnt= $4}
{mo_Min_Order= $5}
{oa_Order_Amt=0}

#Defining Order Amount using given definition
{if (qon_Quan_On_Hand>=rp_ReOrder_Pnt) oa_Order_Amt= 0;
else oa_Order_Amt= rp_ReOrder_Pnt + mo_Min_Order - qon_Quan_On_Hand;
}


#Printing the entire table of data, the Inventory report
{print pa_partnum, "\t", pc_price, "\t\t", qon_Quan_On_Hand, "\t\t", rp_ReOrder_Pnt, "\t\t", mo_Min_Order, "\t   ", oa_Order_Amt}


#End of report
END{ print"----------------------------------------------------------------------------";
print "\n\t\t\t\tEND OF REPORT\n";
print "____________________________________________________________________________"}
