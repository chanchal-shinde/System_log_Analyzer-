def print_data() :
    with open("system.log","r") as f:
        data=f.read()
        print(data) #printing the data
    

# function for printing number of lines and error in it

report=""

def count() :
    global report
    count_total_line=0
    count_error=0
    count_info=0
    count_warning=0
    msg={}

    with open("system.log","r") as f:

        while True:
            line=f.readline().strip()  # reading data line by line

            if not line :
                break

# counting the if the words like error , warning appeared in lines 

            if("ERROR" in line):
                count_error+=1

            if("WARNING" in line):
                count_warning += 1

            if("INFO" in line) :
                count_info += 1
            
# counting if error or a messages appeared more than once in the file

            if line not in msg :
                msg[line]=1
            else :
               msg[line] += 1 
               
            count_total_line+=1
            
# printing total line and apperance of errors and warnings

        print(f'\n\n------ SYSTEM LOG REPORT -----\n')
        print("Total log entries:- ",count_total_line)
        print("\nERROR Message :- ",count_error)
        print("WARNING Message :- ",count_warning)
        print("INFO Message :- ",count_info)

        report += f'\n\n----------------\n SYSTEM LOG REPORT \n ---------------\n\nTotal log entries:- {count_total_line}\n'
        report += f'\n->ERROR Message :- {count_error} \n->WARNING Message :- {count_warning} \n->INFO Message :- {count_info} \n'

        
# printing if a error occured moree than once
        
        print(f'\n\nRepeated Messages : ')
        for line in msg :
            if msg[line] >1 :
                print(f'\n {line} ---> {msg[line]} times')
                report += f'\nRepeated mesaage : \n{line} ocuured {msg[line]} times'

# function for writing in repoet file

def write() :
    global report
    with open("report.txt","w") as f :
        f.write(report)

# callinf functions        
print_data()
count()
write()