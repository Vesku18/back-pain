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

print('Solutions file read in')

########################################
# Read users document
########################################
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

print('Users read')

#input("Press Enter to continue...")

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

with open('technical_vocabulary.csv') as csvfile:
	reader = csv.DictReader(csvfile, ['disease','dis_num','disease_sh', 'symptom', 'sym_num', 'symptom_sh', 'therapy', 'the_num','therapy_sh', 'lifestyle', 'lif_num' , 'lifestyle_sh'])
	admin_id=1;
	for row in reader:
		# Read disease column in
		str1 = row['disease']
		if (str1 != ''):
			disease.append([row['disease'], row['disease_sh']])
			dis_set.add(row['disease'])
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

		# Read Symptom column in
		str2=row['symptom']
		if (str2 != ''):
			symptom.append([row['symptom'], row['symptom_sh']])
			sym_set.add(row['symptom'])

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

		# Read therapy column in
		str2=row['therapy']
		if(str2 != ''):#!= ''):
			therapy.append([row['therapy'], row['therapy_sh']])
			the_set.add(row['therapy'])

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

		# Read lifestyle column in
		str2=row['lifestyle']
		if (str2 != ''):
			lifestyle.append([row['lifestyle'], row['lifestyle_sh']])
			lif_set.add(row['lifestyle'])

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

print('Technical vocabulary read in')
#print(technical_vocabulary)
#input("Press Enter to continue...")

######################################################
######################################################
# Histogram - now word, sh - lets add count, category
######################################################
terms_not_in_technical_voc = []

tv_count = []
for t in technical_vocabulary:
	tv_count.append('0')

for a in technical_vocabulary:
	counter=0
	for s in solutions:
		terms = s[3].split()
		for b in terms:
			if len(b)>0:
				if a_in_b(a,b): # Check if even part of word incldues term
					counter=counter+1
	for s in users:
		terms = s[1].split()
		for b in terms:
			if len(b)>0:
				if a_in_b(a,b):
					counter=counter+1
	tv_count[technical_vocabulary.index(a)]=str(counter)

# Sort histogram list
def histogFunc(f):
	return(int(f[1]))
tv_histog = []
for t in technical_vocabulary:
	tv_histog.append([t,tv_count[technical_vocabulary.index(t)]])
tv_histog.sort(reverse=True, key=histogFunc)

# histogram list to file
f=open( "output_histogram_technical_vocabulary.csv","w")
for t in tv_histog[:10]:
	f.write(t[0] + ',' + t[1] + ',' + '\n')
	print(t)

###################################################3
# Histogram for disease
print('Histogram for disease words')
for a in disease:
	counter=0
	if len(a)>0:
		for s in solutions:
			terms = s[3].split()
			for b in terms:
				if len(b)>0:
					if a_in_b(a,b): # Check if even part of word incldues term
						counter=counter+1
		for s in users:
			terms = s[1].split()
			for b in terms:
				if len(b)>0:
					if a_in_b(a,b):
						counter=counter+1
		a.append(str(counter))

# Sort histogram list
def histogCat(f):
	return(int(f[2]))
disease.sort(reverse=True, key=histogCat)

# histogram list to file
f=open( "output_histogram_disease.csv","w")
for t in disease[:10]:
	f.write(t[0] + ',' + t[1] + ',' + t[2] + '\n')
	print(t)

###########################################
# histogram for Symptom
print('Histogram for Symptom words')
for a in symptom:
	counter=0
	if len(a)>0:
		for s in solutions:
			terms = s[3].split()
			for b in terms:
				if len(b)>0:
					if a_in_b(a[0],b): # Check if even part of word incldues term
						counter=counter+1
		for s in users:
			terms = s[1].split()
			for b in terms:
				if len(b)>0:
					if a_in_b(a[0],b):
						counter=counter+1
		symptom[symptom.index(a)].append(str(counter))

# Sort histogram list
def histogCat(f):
	return(int(f[2]))
symptom.sort(reverse=True, key=histogCat)

# histogram list to file
f=open( "output_histogram_symptom.csv","w")
for t in symptom[:10]:
	f.write(t[0] + ',' + t[1] + ',' + t[2] + '\n')
	print(t)

##################################################
# Histogram therapylle
print('histogram for therapy words')
for a in therapy:
	counter=0
	if len(a)>0:
		for s in solutions:
			terms = s[3].split()
			for b in terms:
				if len(b)>0:
					if a_in_b(a[0],b): # Check if even part of word incldues term
						counter=counter+1
		for s in users:
			terms = s[1].split()
			for b in terms:
				if len(b)>0:
					if a_in_b(a[0],b):
						counter=counter+1
		therapy[therapy.index(a)].append(str(counter))

# Sort histogram list
def histogCat(f):
	return(int(f[2]))
therapy.sort(reverse=True, key=histogCat)

# histogram list to file
f=open( "output_histogram_therapy.csv","w")
for t in therapy[:10]:
	f.write(t[0] + ',' + t[1] + ',' + t[2] + '\n')
	print(t)

###############################################
# Histogram for lifestyle
print('Histogram for lifestyle words')
for a in lifestyle:
	counter=0
	if len(a)>0:
		for s in solutions:
			terms = s[3].split()
			for b in terms:
				if len(b)>0:
					if a_in_b(a[0],b): # Check if even part of word incldues term
						counter=counter+1
		for s in users:
			terms = s[1].split()
			for b in terms:
				if len(b)>0:
					if a_in_b(a[0],b):
						counter=counter+1
		lifestyle[lifestyle.index(a)].append(str(counter))

# Sort histogram list
def histogCat(f):
	return(int(f[2]))
lifestyle.sort(reverse=True, key=histogCat)

# histogram list to file
f=open( "output_histogram_lifestyle.csv","w")
for t in lifestyle[:10]:
	f.write(t[0] + ',' + t[1] + ',' + t[2] + '\n')
	print(t)

##########################################
##########################################
# Sentiment vocabulary
##########################################
sentiments_pos=[]
sentiments_neg=[]

with open('sentiment_words.csv') as csvfile:
	reader = csv.DictReader(csvfile, ['word','wor', 'sent'])
	for row in reader:
		if row['wor'] not in stopwords:
			if row['wor'] not in sentiments_pos:
				if row['sent'] == '+':
					sentiments_pos.append(row['wor'])
			if row['wor'] not in sentiments_neg:
				if row['sent'] == '-':
					sentiments_neg.append(row['wor'])
		else:
			removed_words.append(row['wor'])

########################################################
# Sentiment analysis for solutions document
print('Positivness versus negativness in solution docuemnts')
sentiment_solutions=[]
sentiment_users=[]

def toisesta(r):
	return int(r[1])

def kolmannesta(r):
	return int(r[2])

f=open( "output_sentiment_analysis_documents.csv","w")
f.write('Document, positive, negative ' + '\n')

for s in solutions:
	f.write(s[1])
	text_list = s[3].split()
	text_set = set(text_list)
	plus_counter=0
	neg_counter=0
	plus=[]
	neg=[]

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

	sentiment_solutions.append([str(solutions.index(s)), str(plus_counter),str(neg_counter)])

sentiment_solutions.sort(reverse=True, key=toisesta )
print('Dokumnetit joissa eninten positiivisia sanoja ')
print(sentiment_solutions[:5])
sentiment_solutions.sort(reverse=True, key=kolmannesta )
print(' Dokumnetit joissa eniten negatiiivisia sanoja ')
print(sentiment_solutions[:5])

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

f=open( "output_sentiment_analysis_userdoc.csv","w")
f.write('Document, positive, negative ' + '\n')

for s in users:
	f.write(s[0])
	text_list = s[1].split()
	text_set = set(text_list)
	plus_counter=0
	neg_counter=0
	plus=[]
	neg=[]

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

	sentiment_users.append([str(users.index(s)), str(plus_counter),str(neg_counter)])

sentiment_users.sort(reverse=True, key=toisesta)
print( 'Users joissa eniten postitiivisia sanoja ')
print(sentiment_users[:5])
print(' users joissa eniten negatiivisia sanoja ')
sentiment_users.sort(reverse=True, key=kolmannesta)
print(sentiment_users[:5])



#########################################################################
#########################################################################
# Overlapping between user documents and technical vocabulary
#########################################################################

technical_vocabulary_set = set(technical_vocabulary)
print('Common words in reference vs. technical vocabulary in users file')

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


#############################################################
# Overlapping between user documents and technical vocabulary
#############################################################

technical_vocabulary_set = set(technical_vocabulary)
#print(technical_vocabulary_set)
print('Common words reference vs. technical vocabulary in solutions documents')
f=open( "output_intersection_with_reference.csv","w")
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
			f.write(',')
			sss="0"

	f.write(',' + str(len(leikkaus_set)) + ',' + str(len(diff_set)))
	f.write(',' + str(len(dis_set.intersection(leikkaus_set))) + ',' + str(len(sym_set.intersection(leikkaus_set))) + ',' + str(len(the_set.intersection(leikkaus_set))) + ','+ str(len(lif_set.intersection(leikkaus_set))))
	f.write('\n')

################################################################
# Overlapping between user documents with other user document
print('Then calculate intersection with all other user documents')
f=open( "output_document_vs_document_similarity.csv","w")
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
f=open( "output_dictionary.txt","w")
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