import os
import csv
csvpath = "PyBank\Resources/budget_data.csv"
#csvpath=os.path.join("Resources", "budget_data.csv")
with open(csvpath) as csvfile:
    csvreadr=csv.reader(csvfile, delimiter=',')
#skips header
    next(csvreadr)
#    
    budget_data=[next(csvreadr)]
#start of variables
    net=int(budget_data[0][1])
    difference=[]
# refrence point for calculation
    last_value=net
#starting loop
    for line in csvreadr:
        budget_data.append(line)
        net=net+int(line[1])
        difference.append(int(line[1])-last_value)
        last_value=int(line[1])
#max change
greatest_inc=difference.index(max(difference))
#min change
greatest_dec=difference.index(min(difference))
#printing resultant
print("Financial Analysis")                                                  
print("Total Months: " + str(len(budget_data)) + " months")
print("Total: $" + str(net))
print("Average Change: $"+ str(round(sum(difference))/(len(difference))))
print("Greatest Increase: "+(budget_data[greatest_inc+1][0]) + " $"+ str(max(difference)))
print("Greatest Decrease: "+(budget_data[greatest_dec+1][0]) + " $"+ str(min(difference)))
#txt file
with open("PyBankAnalysis.txt","w") as txt_file:
    txt_file.write(f"Financial Analysis\n")
    txt_file.write(f"Total Months:   {str(len(budget_data))} +  months\n")
    txt_file.write(f"Total: $  {str(net)}\n")
    txt_file.write(f"Average Change: $ {str(round(sum(difference))/(len(difference)))}\n")
    txt_file.write(f"Greatest Increase: {(budget_data[greatest_inc+1][0])  +  str(max(difference))}\n")
    txt_file.write(f"Greatest Decrease: {(budget_data[greatest_dec+1][0])  +  str(min(difference))}\n")