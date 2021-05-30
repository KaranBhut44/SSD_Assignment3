## Question file link: https://github.com/KaranBhut44/SSD_Assignment3/blob/main/PartB/Assignment3_PartB.pdf
# q1.py
 - ##### Removed line-number 16 to 20 and added 16 to 25:
   - make list of employees from input and after removing 1st argument,(number of employees) stored it in `emp_list`.(because this code can handle any number of employees not just 3 to 5)
   - if 1 of the argument(employee-id) is leader of organization then `Leader not found` is printed. 
 - ##### Removed line-number 35 to 43 and added 40 to 55:
   - old code was capable to handle only 2 employees.
   - If invalid employee-id is entered(that employee don't belong to organization) then "Leader not found" is printed.
   - parents_list is made from  `org.json` file(just like partA) and appended it to newly made `child_parents_list`.
   - minimum length of parents_list present in `child_parents_list` is calculated and stored in `min_length` variable. (Note: Here `child_parents_list` is 2-dimensional)
   - for example, parent of 'P' is 'Q' and parent 'Q' is 'R'. then parent_list of 'Q' = `['R']` and parent_list of 'P' =`['R','Q']`.
 - ##### Removed line-number 45,46,47:
   - level of employees are counted and stored in `level` list.
 - ##### Removed line-number 49 to 51 and added line-number 73 to 75:
   - printing leader and level difference of employees to leader.

# q2.py
 - ##### Added line-1:
   - imported `sys` library.
 - ##### Added line-77:
   - seperated "Date1: `date`" string by `:` and removed left spaces from resulting string.
   - Retrieved `date` from that string.
 - ##### Added line-number 80-97:
   - read commandline argument. If no argument present then progressed forward just like partA.
   - If argument is present then took 1st character of string. If it is `m` then it might contain `mm/dd/yyyy` type of format. otherwise progressed further just like partA.
   - Splitted date and month from string. And swapped position of dates and months in string.
   - so, now format is changed from `mm/dd/yyyy` to `dd/mm/yyyy`, `mm-dd-yyyy` to `dd-mm-yyyy` , etc...
 - ##### Removed line-79 and added line-number 99 to 103:
   - if both starting and ending date is same or difference is 1 then, string "....Day" is printed otherwise "....Days" is printed.

# q3.py
 - ##### Added line-number 14 to 38 and removed line-number 109 to 130:
   - made new function `convert_12hr_to_24hr` to change time like `1:30PM` to `13.5`.(In partA, code was written at line-109 to 130)
 - ##### Added line-100 and removed line-75:
   - appended "12-1" to resultant list `l` instead of "(12,1)" for future convenience for finding intersaction between 2 time-slots.
 - ##### Removed line-number 83 to 92 and added 109 to 124:
   - read all files of current directory whose name is like `Employee*.txt` and stored it into `file_list`.
   - read content of files from `file_list` and stored it in `e_list`.
   - converted string form of dictionary to object form from `e_list` and stored it into `E_list`.
 - ##### Removed line-number 94 to 101 and added line-number 126 to 136:
   - make lists for storing emp_names, dates, etc. inplace of individual variables like partA.
   - `emp_name_list` contains name of employees, `date_list` contains dates, `list_list` contains time-slot lists of different employees.
 - ##### Removed line-103 and added line-138,139:
   - check if all dates of date_list is same or not. if not same then "no slot is available" is written to output.txt file.
 - ##### Removed line-number 109 to 130 and added line-number 145 to 150:
   - called `convert_12hr_to_24hr` function for all items present in `list_list` and result is appended to `updated_list`.
   - found complement of each items in `updated_list` and result is stored to `l_list` list.
 - ##### Removed line-number 132 to 163 and added line-number 152 to 171:
   - found available slot for all employees from `find_required_slot` function and stored it in required format.
 - ##### Removed line-167,170 and added line-175,178:
   - stored available slots for all employees and required slot in output.txt file.
