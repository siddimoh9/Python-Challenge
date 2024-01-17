import os
import csv
csvpath = "PyPoll\Resources/election_data.csv"
#csvpath=os.path.join("Resources", "budget_data.csv")
with open(csvpath) as csvfile:
    csvreadr=csv.reader(csvfile, delimiter=',')
    header=next(csvreadr)
#lists
    names=[]
    win=[]
    percent=[]
#counter
    total=0
#begin
    for row in csvreadr:
        total += 1
        if row[2] not in names:
            names.append(row[2])
            index=names.index(row[2])
            win.append(1)
        else:
            index=names.index(row[2])
            win[index]+=1
#%
    for vote in win:
        percentage=(vote/total)*100
        percentage=round(percentage)
        percentage = "%.3f%%" % percentage
        percent.append(percentage)
#winner
    elected=max(win)
    index=win.index(elected)
    elected_name=names[index]
#print
print("Election Results")
print(f"Total Votes: {str(win)}")
for i in range(len(names)):
    print(f"{names[i]}: {str(percent[i])} ({str(win[i])})")
print(f"Winner: {elected_name}")
#txt file
#convert
with open("PyPollAnalysis.txt","w") as txt_file:
    txt_file.write("ELection Results\n")
    txt_file.write(f"Total Votes: {str(win)}\n")
    for i in range(len(names)):  
        txt_file.write(f"{names[i]}: {str(percent[i])} ({str(win[i])})\n")
    txt_file.write(f"Winner: {elected_name}\n")
    



