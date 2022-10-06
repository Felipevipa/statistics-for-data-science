'''
1. In the directory where you put survey.py and the data files, 
create a file named first.py and type or paste in the following 
code:
    import survey
    table = survey.Pregnancies()
    table.ReadRecords()
    print 'Number of pregnancies', len(table.records)
The result should be 13,593 pregnancies.
'''


import survey
table = survey.Pregnancies()
table.ReadRecords()
print('Number of pregnancies ', len(table.records))



'''
2. Write a loop that iterates table and counts the number 
of live births. Find the documentation of outcome and confirm 
that your result is consistent with the summary in the 
documentation.
'''

live_births = 0
for val in table.records:
    # print(val.outcome)
    if val.outcome == 1:
        live_births +=1
    
print('Live births:', live_births)


live_births = [r for r in table.records if r.outcome == 1]
print('Live births:', len(live_births))


'''
3. Modify the loop to partition the live birth records into 
two groups, one for first babies and one for the others. 
Again, read the documentation of birthord to see if your r
esults are consistent.

When you are working with a new dataset, these kinds of 
checks are useful for finding errors and inconsistencies 
in the data, detecting bugs in your program, and checking 
your understanding of the way the fields are encoded.
'''


first_live_birth = 0
other_live_birth = 0
for val in table.records:
    # print(val.outcome)
    if val.outcome == 1:
        if val.birthord == 1:
            first_live_birth += 1
        else:
            other_live_birth += 1
    
print('Live births first:', first_live_birth)
print('Live births other:', other_live_birth)


first_live_birth = [r for r in live_births if r.birthord == 1]
other_live_birth = [r for r in live_births if r.birthord != 1]
print('First births:', len(first_live_birth))
print('Others:', len(other_live_birth))