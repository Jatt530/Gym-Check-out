
Empty_Dict_To_Hold_Results= {}

# FIXME (1): Get the Student ID from the user
Student_ID = input('SID: ')
while Student_ID != '':
    hold_results = []
# FIXME (2): Display the menu and prompt for what is being checked out
    while True:
        gym_stuff= input('''Enter an item:
l - Lock
t - Towel
q - quit
''')
        if gym_stuff == "l":
            num_lock= input("Enter a lock number:")
            hold_results.append("l" + num_lock)
        if gym_stuff == "t":
            hold_results.append('t')
        if gym_stuff == 'q':
# FIXME (3): Print the dictionary in its raw format.
            Empty_Dict_To_Hold_Results[Student_ID] = hold_results
#Break so the loop does not repeat.
            break
    Student_ID= input('SID: ')
print(Empty_Dict_To_Hold_Results)

# FIXME (4): Print the formatted list of all gear checked out.
print("All Gear Checked Out:")
for i, j in Empty_Dict_To_Hold_Results.items():
    print(i, ':', end='\t')
#Must print twice like this because it is a list
    for item in j:
          print(item, end='\t')
    print()
#Must put print() because the '\t' gets rid of newline
