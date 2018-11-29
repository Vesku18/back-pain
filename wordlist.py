import nltk
import csv

table=[]
d=[]
with open('solutions.csv') as csvfile:
	reader = csv.DictReader(csvfile, ['Rivi','Numero', 'Sisus', 'Detaljit'])
	for row in reader:
		#print(row['Rivi'], row['Sisus'])
		table.append([row['Rivi'], row['Sisus'], row['Detaljit']])
		str=row['Sisus']+' '+row['Detaljit']
		prt=str.split()
		for s in prt:
			if s not in d:
				d.append([s])

f=open( "dic_overall.txt","w")
for s in d:
	p=s
	p.append('\n')
	f.write(''.join(p))

f.close()

# Code for getting data from 'howtakescare' column of the users.csv file:
input_file = csv.DictReader(open('users.csv'))
table=[]
d=[]
for row in input_file:
        str=row['howtakescare']
        prt=str.split()
        for s in prt:
                if s not in d:
                        d.append([s])
                        
f=open( "dic_users.txt","w")
for s in d:
        p=s
        p.append('\n')
        f.write(''.join(p))

f.close()
