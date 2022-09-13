#!/bin/bash


#All Column Names printed  with 16 spacing each to keep them aligned in a table
#  - sign for left alignment
printf "%-16s" "Employee No." "Department" "Pay Rate" "Exempt" "Hours Worked" "Base Pay" "Overtime" "Total Pay"
echo ""

# cat statement opens and reads data from EMPLOYEE.txt 
#While statement reads line by line from the file and the variables take each word from 
# the line to divide them column wise
cat EMPLOYEE.txt | while read empNum deptName payRate exempt hrsWorked; do

#If conditions to check if hours worked >= 40 and exempt value "N"
    if [ $hrsWorked -ge 40 ]
    then
        if [ "$exempt" == "N" ]; then

        #Used bash calculator(bc) for floating point arithmetic
            base=$(echo "scale=2; $payRate*$hrsWorked"|bc)
        #Overtime calculated as half of payrate for every hour worked over 40 hours
            OT_overtime=$(echo "scale=2; 0.5*$(($hrsWorked-40))*$payRate"|bc)
        #Total pay calculated as base pay plus overtime pay
            totalPay=$(echo "scale=2; $base+$OT_overtime"|bc)
        #Printing all values with defined space to maintain tabular structure
            printf "%-11d\t %-11d\t %-11.2f\t %-11s\t %-11d\t %-11.2f\t %-11.2f\t %-11.2f\t" "$empNum" "$deptName" "$payRate" "$exempt" "$hrsWorked" "$base" "$OT_overtime" "$totalPay"
            echo ""
        else
        #Overtime set to zero, rest same as if statement
            base=$(echo "scale=2; $payRate*$hrsWorked"|bc)
            OT_overtime=0
            totalPay=$(echo "scale=2; $base+$OT_overtime"|bc)
            printf "%-11d\t %-11d\t %-11.2f\t %-11s\t %-11d\t %-11.2f\t %-11.2f\t %-11.2f\t" "$empNum" "$deptName" "$payRate" "$exempt" "$hrsWorked" "$base" "$OT_overtime" "$totalPay"
            echo ""
        fi
    else
        #Overtime set to zero, rest same as if statement
        base=$(echo "scale=2; $payRate*$hrsWorked"|bc)
        OT_overtime=0
        totalPay=$(echo "scale=2; $base+$OT_overtime"|bc)
        printf "%-11d\t %-11d\t %-11.2f\t %-11s\t %-11d\t %-11.2f\t %-11.2f\t %-11.2f\t" "$empNum" "$deptName" "$payRate" "$exempt" "$hrsWorked" "$base" "$OT_overtime" "$totalPay"
        echo ""
    fi
done