import nltk
import csv

table=[]
d=[]
with open('solutions.csv') as csvfile:
	reader = csv.DictReader(csvfile, ['Rivi','Numero', 'Sisus'])
	for row in reader:
		print(row['Rivi'], row['Sisus'])
		table.append([row['Rivi'], row['Sisus']])
		str=row['Sisus']
		prt=str.split()
		for s in prt:
			if s not in d:
				d.append([s])

#print(table)
print(d)

f=open( "dic.txt","w")
for s in d:
	p=s
	p.append('\n')
	f.write(''.join(p))


# Stopwords
# stopwords = set(line.strip() for line in open('stopwords.txt'))
#stopwords = stopwords.union(set(['on','ja']) )

#wordcount = {}

