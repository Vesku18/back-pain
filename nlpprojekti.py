#import nltk
import csv
import string


def a_in_b(a,b):
	if a is None:
		return False
	if b is None:
		return False
	if len(b) < len(a):
		return False
	for i in range(0,len(a)):
		if a[i] != b[i]:
			return False
	return True

##################################
# Read Stopwords in
##################################
stopwords=[]
removed_words=[]
with open('stopwords.txt') as csvfile:
	reader = csv.DictReader(csvfile, ['Sana'])
	for row in reader:
		#print(row['Sana'])
		stopwords.append(row['Sana'])

#print(stopwords)
print("Stopwords read")

###################################
# Start to create vocabulary
###################################

vocabulary=[] # THIS will contain all the words along the journey
string_count=[] # this will have frequence

solutions=[]
with open('solutions_perusmuoto.csv') as csvfile:
	reader = csv.DictReader(csvfile, ['Rivi','User', 'Otsikko', 'Sisus'])
	admin_id=1;
	for row in reader:
		#print(row['Rivi'], row['Sisus'])
		if(row['User'] == 'admin'):
			a=str(admin_id)
			s='admin' + '_' + a
			admin_id=admin_id+1
		else:
			s=row['Rivi']

		solutions.append([row['Rivi'], s, row['Otsikko'], row['Sisus']])

		str1=row['Otsikko']
		prt=str1.split()
		for s in prt:
			if s not in stopwords:
				if s not in vocabulary:
					vocabulary.append(str(s))
					string_count.append(1)
				else:
					ind = vocabulary.index(s)
					string_count[ind]=int(string_count[ind])+1
			else:
				removed_words.append(s)

		str2=row['Sisus']
		prt=str2.split()
		for s in prt:
			if s not in stopwords:
				if s not in vocabulary:
					vocabulary.append(str(s))
					string_count.append(1)
				else:
					ind = vocabulary.index(s)
					string_count[ind] = int(string_count[ind]) + 1
			else:
				removed_words.append(s)

#print(solutions[1])
print('Solutions file read in')


########################################
# Read users document

users=[]

with open('users.csv') as csvfile:
	reader = csv.DictReader(csvfile, ['User_id','Gender', 'Age', 'Region', 'Jobs','Degree','Howactive','Suffer','Sufferi','Sufffernow','Surge','Howtakescare'])
	admin_id=1;
	for row in reader:
		#print(row['Rivi'], row['Sisus'])
		users.append([row['User_id'], row['Howtakescare']])

		str1=row['Howtakescare']
		prt=str1.split()
		for s in prt:
			if s not in stopwords:
				if s not in vocabulary:
					vocabulary.append(str(s))
					string_count.append(1)
				else:
					ind = vocabulary.index(s)
					string_count[ind]=int(string_count[ind])+1
			else:
				removed_words.append(s)


print(users[1])
print('Users read')



########################################
# Read technical vocabulary
########################################

technical_vocabulary=[]

disease=[]
dis_set=set()
disease_sh=[]
symptom=[]
sym_set=set()
symptom_sh=[]
therapy=[]
the_set=set()
therapy_sh=[]
lifestyle=[]
lif_set=set()
lifestyle_sh=[]

with open('technical_vocabulary_v6.csv') as csvfile:
	reader = csv.DictReader(csvfile, ['disease','disease_sh', 'symptom', 'symptom_sh', 'therapy', 'therapy_sh', 'lifestyle', 'lifestyle_sh', 'nro'])
	admin_id=1;
	for row in reader:
		disease.append([row['disease'], row['disease_sh']])
		dis_set.add(row['disease'])

		str1 = row['disease']
		if(str1 != None):
				prt=str1.split()
				for s in prt:
					if s not in stopwords:
						if s not in vocabulary:
								vocabulary.append(str(s))
								string_count.append(1)
						else:
								ind = vocabulary.index(s)
								string_count[ind] = int(string_count[ind]) + 1

						if s not in technical_vocabulary:
								technical_vocabulary.append(str(s))
					else:
						removed_words.append(s)

		symptom.append([row['symptom'], row['symptom_sh']])
		sym_set.add(row['symptom'])

		str2=row['symptom']

		if (str2 != None):
				prt=str1.split()
				for s in prt:
					if s not in stopwords:
						if s not in vocabulary:
								vocabulary.append(str(s))
								string_count.append(1)
						else:
								ind = vocabulary.index(s)
								string_count[ind] = int(string_count[ind]) + 1

						if s not in technical_vocabulary:
								technical_vocabulary.append(str(s))
					else:
						removed_words.append(s)

		therapy.append([row['therapy'], row['therapy_sh']])
		the_set.add(row['therapy'])

		str2=row['therapy']
		if(str2 != None):#!= ''):
				prt=str2.split()
				for s in prt:
					if s not in stopwords:
						if s not in vocabulary:
								vocabulary.append(str(s))
								string_count.append(1)
						else:
								ind = vocabulary.index(s)
								string_count[ind] = int(string_count[ind]) + 1

						if s not in technical_vocabulary:
								technical_vocabulary.append(str(s))
					else:
						removed_words.append(s)

		lifestyle.append([row['lifestyle'], row['lifestyle_sh']])
		lif_set.add(row['lifestyle'])

		str2=row['lifestyle']
		if (str2 != None):
				prt=str2.split()
				for s in prt:
					if s not in stopwords:
						if s not in vocabulary:
								vocabulary.append(str(s))
								string_count.append(1)
						else:
								ind = vocabulary.index(s)
								string_count[ind] = int(string_count[ind]) + 1

						if s not in technical_vocabulary:
								technical_vocabulary.append(str(s))
					else:
						removed_words.append(s)


#print(sym_set)
#print(the_set)

print('Technical vocabulary read in')
#print(technical_vocabulary)

##########################################
# Sentiment vocabulary
##########################################
sentiments_pos=[]
sentiments_neg=[]

with open('sentiment_words_v5.csv') as csvfile:
	reader = csv.DictReader(csvfile, ['word','wor', 'sent'])
	for row in reader:
		if s not in stopwords:
			if row['wor'] not in sentiments_pos:
				if row['sent'] == '+':
					sentiments_pos.append(row['wor'])
			if row['wor'] not in sentiments_neg:
				if row['sent'] == '-':
					sentiments_neg.append(row['wor'])
		else:
			removed_words.append(s)

########################################################
# Sentiment analysis for solutions document
print('Positivness versus negativness in user docuemnts')

f=open( "sentiment_analysis.csv","w")
f.write('Document, positive, negative ' + '\n')

for s in solutions:
	f.write(s[1])
	text_list = s[3].split()
	text_set = set(text_list)
	plus_counter=0
	neg_counter=0
	plus=[]
	neg=[]
#	print('Dokumentin ' + s[1] + ' vertailu alkaa' + '\n')

	# if all words in positive sentiment definition row are included, then doc gets postiive tic
	for i in sentiments_pos:
		prt=i.split()
		on_sis = 0;
		for p in prt:
			for r in text_list:
				if a_in_b(p,r):
					on_sis=on_sis+1
					plus.append(p + ' löytyi sanasta ' + r)
		if on_sis >= len(prt): # Check if all words of sentiment words in row exist in solutions details
			plus_counter = plus_counter + 1 # stemmed wor may exist in several words in user document but only own count

	f.write(',' + str(plus_counter))

	# Same for negatives
	for i in sentiments_neg:
		prt = i.split()
		on_sis=0
		for p in prt:
			for r in text_list:
				if a_in_b(p,r):
					on_sis=on_sis +1
					neg.append(p + ' löytyi sanasta ' + r)
		if (on_sis >= len(prt)) and (on_sis > 0):
				neg_counter = neg_counter + 1

	f.write(',' + str(neg_counter))

	f.write(',')
	f.write(str(plus))
	f.write(',')
	f.write(str(neg))
	f.write('\n')


'''	print('Näistä pos sanoja etitään' )
	print(text_list)
	print('\n')
	print('Tässä haettavat postiiiviset sanat' + 'n')
	print(sentiments_pos )
	print(plus)

	print('Tässä haettavat negatiiviset  sanat')
	print(sentiments_neg )
	print(neg)

	print('+n' + 'Tulos: Doc ' + s[1] + ' Positive: ' + str(plus_counter) + ', Negative: ' + str(neg_counter) + '\n')
'''

########################################################
# Sentiment analysis for users document
print('Positivness versus negativness in user docuemnts')

f=open( "sentiment_analysis_userdoc.csv","w")
f.write('Document, positive, negative ' + '\n')

for s in users:
	f.write(s[0])
	text_list = s[1].split()
	text_set = set(text_list)
	plus_counter=0
	neg_counter=0
	plus=[]
	neg=[]
#	print('Dokumentin ' + s[1] + ' vertailu alkaa' + '\n')

	# if all words in positive sentiment definition row are included, then doc gets postiive tic
	for i in sentiments_pos:
		prt=i.split()
		on_sis = 0;
		for p in prt:

			for r in text_list:
				if a_in_b(p,r):
					on_sis=on_sis+1
					plus.append(p + ' löytyi sanasta ' + r)
		if (on_sis >= len(prt)) and (on_sis > 0): # Check if all words of sentiment words in row exist in solutions details
			plus_counter = plus_counter + 1 # stemmed wor may exist in several words in user document but only own count

	f.write(',' + str(plus_counter))

	# Same for negatives
	for i in sentiments_neg:
		prt = i.split()
		on_sis=0
		for p in prt:
			for r in text_list:
				if a_in_b(p,r) and r is not None and p is not None:
					on_sis=on_sis +1
					neg.append(p + ' löytyi sanasta ' + r)
		if on_sis >= len(prt) and on_sis != 0:
				neg_counter = neg_counter + 1

	f.write(',' + str(neg_counter))

	f.write(',')
	f.write(str(plus))
	f.write(',')
	f.write(str(neg))
	f.write('\n')




##########################################
# Overlapping between user documents and technical vocabulary
technical_vocabulary_set = set(technical_vocabulary)
#print(technical_vocabulary_set)
print('Common words and difference')

f=open( "intersection_with_reference_for_users_doc.csv","w")
f.write(' ')
for s in technical_vocabulary:
	f.write(','+ s )
f.write(', SAME, DIFFERENT' +','+ 'Disease' +','+ 'Symptom' +','+ 'Therapy'+','+'Lifestyle'+ '\n')

user_counter=0
for s in users:
	user_counter = user_counter +1
	text_set = set(s[1].split())
	diff_set=set(text_set.difference(technical_vocabulary_set))
	leikkaus_set=set(text_set.intersection(technical_vocabulary_set))
	#print('User:' + str(user_counter) + ' Common: ' + str(len(leikkaus_set)) + ', Different: ' + str(len(diff_set)))

	f.write(s[0])
	for sana in technical_vocabulary:
		if( sana in list(leikkaus_set)):
			f.write(',' + '1')
		else:
			f.write(','+ '0')
	f.write(',' + str(len(leikkaus_set)) + ',' + str(len(diff_set)))
	f.write(',' + str(len(dis_set.intersection(leikkaus_set))) + ',' + str(len(sym_set.intersection(leikkaus_set))) + ',' + str(len(the_set.intersection(leikkaus_set))) +','+ str(len(lif_set.intersection(leikkaus_set))) + '\n')

	#print(leikkaus_set)
	#print(str(len(dis_set.intersection(leikkaus_set))) + ',' + str(len(sym_set.intersection(leikkaus_set))) + ',' + str(len(the_set.intersection(leikkaus_set))) + ',''+ str(len(lif_set.intersection(leikkaus_set))))

##########################################
# Overlapping between user documents and technical vocabulary
technical_vocabulary_set = set(technical_vocabulary)
#print(technical_vocabulary_set)
print('Common words and difference')
f=open( "intersection_with_reference.csv","w")
f.write(' ')
for s in technical_vocabulary:
	f.write(','+ s )
f.write(', SAME, DIFFERENT' +','+ 'Disease' +','+ 'Symptom' +','+ 'Therapy'+','+'Lifestyle'+ '\n')

for s in solutions:
	text_set = set(s[3].split())
	diff_set=set(text_set.difference(technical_vocabulary_set))
	leikkaus_set=set(text_set.intersection(technical_vocabulary_set))
	#print('Doc:' + s[1] + ' Common: ' + str(len(leikkaus_set)) + ', Different: ' + str(len(diff_set)))
	f.write(s[1])
	for sana in technical_vocabulary:
		if( sana in list(leikkaus_set)):
			f.write(',' + '1')
		else:
			f.write(','+ '0')

	f.write(',' + str(len(leikkaus_set)) + ',' + str(len(diff_set)))
	f.write(',' + str(len(dis_set.intersection(leikkaus_set))) + ',' + str(len(sym_set.intersection(leikkaus_set))) + ',' + str(len(the_set.intersection(leikkaus_set))) + ','+ str(len(lif_set.intersection(leikkaus_set))) + '\n')


##########################################
# Overlapping between user documents with other user document
print('Then calculate intersection with all other user documents')
f=open( "document_vs_document_similarity.csv","w")
f.write(' ')
for s in solutions:
	f.write(','+ s[1] )
f.write('\n')

for s in solutions:
	text_set = set(s[3].split())
	common_list = []
	f.write(s[1])
	for d in solutions:
		# verrataan jokaiseen solutionin settiin
		leikkaus_set=set(text_set.intersection(set(d[3].split())))
		# muodostetaan samalla yhteistä listaa kaikista
		f.write(',' + str(len(leikkaus_set)))
		for i in leikkaus_set:
			if(s != d): # Decline diagonal, comparison against itself
				if i not in common_list:
					common_list.append(i)
	f.write(',' + str(len(common_list)) + '\n')

	#print('Doc:' + s[1] + ' Common: ' + str(len(set(common_list))) )



##########################################
# Create vocabulary file
##########################################
f=open( "dic.txt","w")
for s in vocabulary:
	#print(s + ' ' + str(string_count[vocabulary.index(s)]))
	f.write(s + ',' + str(string_count[vocabulary.index(s)]) + '\n')

print('Vocabulary file created')

##########################################
# Create removed words list
##########################################

f=open("removed_words.txt","w")
for s in removed_words:
	f.write(s + ',')

print('Removed words list created')

###########################################
# Classify