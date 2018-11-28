import nltk
import csv

table=[]
d=[]
with open('solutions.csv') as csvfile:
	reader = csv.DictReader(csvfile, ['Rivi','Numero', 'Sisus', 'Detaljit'])
	for row in reader:
		#print(row['Rivi'], row['Sisus'])
		table.append([row['Rivi'], row['Sisus'], row['Detaljit']])
		str=row['Sisus']+row['Detaljit']
		prt=str.split()
		for s in prt:
			if s not in d:
				d.append([s])

#print(table)
#print(d)

f=open( "dic_overall.txt","w")
for s in d:
	p=s
	p.append('\n')
	f.write(''.join(p))

f.close()

