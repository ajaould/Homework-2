import os
import csv


csvpath = os.path.join("03-Python_Homework_PyBank_Resources_budget_data.csv")


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)
    #The total number of months included in the dataset

    counter = 0

    counter_2 = 0

    largest = 0

    smallest = 0

    average = []

    newav = []

    months = []

    for row in csvreader:
        counter = counter + 1

        counter_2 = counter_2+float(row[1])

        
        average.append(int(row[1]))

        months.append(row[0])

    cur=0
    nxt=0
    l = 0
    s=0
    for i in range(len(average)-1):
        cur=average[i]
        nxt=average[i+1]
      #  print(cur-nxt)
        newav.append(nxt-cur)
        
        if largest < float(nxt-cur):
            largest = float(nxt-cur)
            l=i+1

        if smallest > float(nxt-cur):
            smallest = float(nxt-cur)
            s=i+1

    finav=sum(newav)/len(newav)


    #The net total amount of "Profit/Losses" over the entire period

  
    print("Financial Analysis")
    print("-------------------------------------------")
    print("Total Months: " + str(counter))

    print("Total: $" + str(counter_2))

    #average = counter_2/counter
    #print(str(average))
    print("Average Change: $" + str(finav))

   # print(str(largest)) 
    print("Greatest Increase in Profits: " + months[l] + " ($" + str(largest) + ")" )
    print("Greatest Decrease in Profits: " + months[s] + " ($" + str(smallest) + ")")

    



# Open the file using "write" mode. Specify the variable to hold the contents
with open("bank.txt", 'x') as txtfile:
    txtfile.write("Financial Analysis \n")
    txtfile.write("-------------------------------------------\n") 
    txtfile.write("Total Months: " + str(counter) + "\n")
    txtfile.write("Total: $" + str(counter_2)+ "\n")
    txtfile.write("Average Change: $" + str(finav)+ "\n")
    txtfile.write("Greatest Increase in Profits: " + months[l] + " ($" + str(largest) + ") \n" )
    txtfile.write("Greatest Decrease in Profits: " + months[s] + " ($" + str(smallest) + ") \n")









# Election Data

csvpath = os.path.join("03-Python_Homework_PyPoll_Resources_election_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    ecounter = 0
    kcount = 0
    ccount = 0
    lcount = 0
    ocount = 0


    for row in csvreader:

        #count number of votes
        ecounter = ecounter + 1

        #count number of Khan votes
        if row[2] == "Khan":
            kcount += 1

        if row[2] == "Correy":
            ccount += 1
        
        if row[2] == "Li":
            lcount += 1

        if row[2] == "O'Tooley":
            ocount += 1

    kpercent = kcount/ecounter
    formatk = format(kpercent, '.3%')

    cpercent = ccount/ecounter
    formatc = format(cpercent, '.3%')

    lpercent = lcount/ecounter
    formatl = format(lpercent, '.3%')

    opercent = ocount/ecounter
    formato = format(opercent, '.3%')



    print("Election Results")
    print("-------------------------------------------")
    print("Total votes: " + str(ecounter))
    print("-------------------------------------------")
    print("Khan: " + str(formatk) + " (" + str(kcount) + ")")
    print("Correy: " + str(formatc) + " (" + str(ccount) + ")")
    print("Li: " + str(formatl) + " (" + str(lcount) + ")")
    print("O'Tooley: " + str(formato) + " (" + str(ocount) + ")")
    print("-------------------------------------------")
    if (ocount > ccount and ocount > lcount and ocount > ccount):
        print("winner: O'Correy")
    

    elif (ccount > kcount and ccount > lcount and ccount>ocount):
        print("Winner: Correy")
    
    elif (lcount > ccount and lcount > ccount and lcount> ocount):
        print("Winner: Li")

    elif (kcount > ccount and kcount > lcount and kcount > ocount):
        print("Winner: Khan")



    print("-------------------------------------------")

# Open the file using "write" mode. Specify the variable to hold the contents
with open("election.txt", 'x') as txtfile:
    txtfile.write("Election Results \n")
    txtfile.write("-------------------------------------------\n") 
    txtfile.write("Total votes: " + str(ecounter) + "\n")
    txtfile.write("-------------------------------------------\n")
    txtfile.write("Khan: " + str(formatk) + " (" + str(kcount) + ") \n")
    txtfile.write("Correy: " + str(formatc) + " (" + str(ccount) + ") \n")
    txtfile.write("Li: " + str(formatl) + " (" + str(lcount) + ") \n" )
    txtfile.write("O'Tooley: " + str(formato) + " (" + str(ocount) + ") \n")
    txtfile.write("-------------------------------------------\n")
    if (ocount > ccount and ocount > lcount and ocount > ccount):
        txtfile.write("winner: O'Correy")
    

    elif (ccount > kcount and ccount > lcount and ccount>ocount):
        txtfile.write("Winner: Correy")
    
    elif (lcount > ccount and lcount > ccount and lcount> ocount):
        txtfile.write("Winner: Li")

    elif (kcount > ccount and kcount > lcount and kcount > ocount):
        txtfile.write("Winner: Khan")


