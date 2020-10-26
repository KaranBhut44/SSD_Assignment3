# q1
 - `find_parents(emp-id)` makes list(`l1`) of ancestors(leaders directly or indirectly (parent,grandparent,greategrandparent....etc leaders in the tree)) of that employee from the `org.json` file.
 - if we enter employee-id of organization's leader, it returns "Leader not found".
 - `d` is dictionary which includes emp-id as key and their parent's emp-id as value.
 - `c1` is list of emp-id.
 - `child_parents` contains emp-id mapped with the ancestor dictionary `l1`(created by `find_parents` function).
 - if invalid emp-id is entered as any one of the input then "Leader not found" is displayed.
 - in `else` part, both emp-id's ancestor list is taken as `l1` and `l2` respectively.then both lists are compared. last same emp-id of both lists represents their desired leader's empid.(first same value represents orgranization's leader's emp-id)
 - then leader's emp-id and level difference of leader from both employees are displayed on new lines.

# q2
 - 'fun' function takes 2 dates in all possible format and returns no. of days between those dates. If in given date date,month and year is seperated by . or / or - then it calls `make_list` function otherwise calls `make_list_string` function.
 - `month_number` assigns numbers to all 12 months and `month_days` represents days of all months(considered non-leap year).If year is leap then seperately days are added whenever needed.
 - `make_list` function takes argument as 1 date (date,month and year is seperated by . or / or -) and returns list of date,month,year
 - `make_list_string` function takes argument as 1 date formatted as for ex: "10th October, 2020" or "10th oct, 2020" and returns list of date,month,year
 - `leap` function returns total number of leap years before given month and year.
 - `count` function's argument is list of both dates. It is internally called by fun(a,b) function. and returns no of days between given dates in the list.
 - `fun` is called and given 2 lines from `date_calculator.txt` as arguments. After output is converted to string then it is written in `output.txt` file.

# q3
 - dictionaries of both employees are read from `Employee1.txt` and `Employee2.txt` file as string. 
 - `ast.literal_eval` method converts that string into dictionary object.
 - then name of employees,dates and busy-slot's lists are taken and stored in different variables.
 - if dates of both employee don't match then slot-duration is stored to dummy_variable and "no slot available" is written to `output.txt` file.
 - then date of 12hr format is converted to 24 hours format and minutes are converted to decimal values of hour( AM, PM are removed and changed the format. For ex: value 1:30PM is changed to 13.5).
 - those updated lists are given as arguments to `find_complement` function. which returns list of available slots in same format.
 - `convert_24hr_to_12hr` functions takes that list and converts it to 12hr format(for Ex: value 13.5 is changed to 1:30PM).
 - find_intersaction` function takes 24hr formatted both employees available date slots as arguments and returns list of available slots for both combinely.
 - slot duration input is taken from user and stored it in `slot` variable. and it is passed to `find_required_slot` function along with `available_slots` list.
 - `find_required_slot` function returns list of selected slot matched with requirement(matched with given `slot` argument) if available.if not then it returns string "no slot available".
 - if `find_required_slot` function returns list then  `Available slots for both employees` and `selected slot and slot duration` is written to `output.txt` file, otherwise `no slot available` is written to the file. 




## Link of github repository: https://github.com/KaranBhut44/2020202015.git
