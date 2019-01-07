"""
Lisätty lemmaus.
Lisätty muutama str-muunnos
"""

import sys
import csv
import string
import re
import nltk
import os

stopwords = []
removed_words = []
vocabulary = []
string_count = []
technical_vocabulary = []
solutions = []
users = []
disease = []
dis_set = set()
disease_sh = []
symptom = []
sym_set = set()
symptom_sh = []
therapy = []
the_set = set()
therapy_sh = []
lifestyle = []
lif_set = set()
lifestyle_sh = []


def toisesta(r):
	return int(r[1])


def kolmannesta(r):
	return int(r[2])


def neljannesta(r):
	return int(r[3])  # Documents overall sentiment calculation


def strip_word(s):
	return s.strip(' ,.+-()\/"')

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

def lemmatize_files():
    """"
    Lemmatization. Need file las-fi, no extention in name allowed
    """
    os.system("if not exist users.csv echo SERIOUS ERROR! File users.csv not found!")
    os.system("if not exist solutions.csv echo SERIOUS ERROR! File solutions.csv not found!")
    os.system("if not exist las-fi echo SERIOUS ERROR! File las-fi not found!")
    print("Starting lemmatization. This can take a while, please wait.")
    os.system("if exist users_lemmatized.csv del users_lemmatized.csv")
    r = os.system("java -jar las-fi lemmatize users.csv --locale fi")
    #print(r)
    if r != 0:
        return False
    os.system("ren users.csv.lemmatized users_lemmatized.csv")
    os.system("if exist solutions_lemmatized.csv del solutions_lemmatized.csv")
    r = os.system("java -jar las-fi lemmatize solutions.csv --locale fi")
    #print(r)
    if r != 0:
        return False
    os.system("ren solutions.csv.lemmatized solutions_lemmatized.csv") 
    print("Lemmatization ready.") 
    print("Lemmatized files are users_lemmatized.csv and solutions_lemmatized.csv")
    return True

def create_vocabulary():
	##################################
	# Read Stopwords in
	##################################

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
	tsolutions=[]
	with open('solutions_lemmatized.csv') as csvfile:
		reader = csv.DictReader(csvfile, ['Rivi','User', 'Otsikko', 'Sisus'])
		admin_id=1;
		for row in reader:
			#print(row['Rivi'], row['Sisus'])
			if(row['User'] == 'admin'):
				a=str(admin_id)
				tunnus='admin' + '_' + a
				admin_id=admin_id+1
			else:
				tunnus=row['Rivi']
			tsolutions.append([row['Rivi'], tunnus, row['Otsikko'], row['Sisus']])
			newrow = []
			newOtsikko = ''
			newSisus = ''

			str1=str(row['Otsikko'])

			prt = nltk.word_tokenize(str1)
			for ss in prt:
				s=strip_word(ss).lower()
				newOtsikko += ' ' + s
				if s not in stopwords:
					if s not in vocabulary:
						vocabulary.append(str(s))
						string_count.append(1)
					else:
						ind = vocabulary.index(s)
						string_count[ind]=int(string_count[ind])+1
				else:
					removed_words.append(s)
			str2=str(row['Sisus'])

			prt = nltk.word_tokenize(str2)
			for ss in prt:
				s=strip_word(ss).lower()
				newSisus += ' '+ s
				if s not in stopwords:
					if s not in vocabulary:
						vocabulary.append(str(s))
						string_count.append(1)
					else:
						ind = vocabulary.index(s)
						string_count[ind] = int(string_count[ind]) + 1
				else:
					removed_words.append(s)

			solutions.append([row['Rivi'], tunnus, newOtsikko, newSisus ])

	print('Solutions file read in')

	########################################
	# Read users document
	########################################

	with open('users_lemmatized.csv') as csvfile:
		reader = csv.DictReader(csvfile, ['User_id','Gender', 'Age', 'Region', 'Jobs','Degree','Howactive','Suffer','Sufferi','Sufffernow','Surge','Howtakescare'])
		admin_id=1;
		for row in reader:
			#print(row['Rivi'], row['Sisus'])
			users.append([row['User_id'], row['Howtakescare']])
			str1=row['Howtakescare']
			#prt=str1.split(',')
			prt = nltk.word_tokenize(str1)
			for ss in prt:
				s=strip_word(ss).lower()
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
#						if s not in vocabulary:
#								vocabulary.append(str(s))
#								string_count.append(1)
#						else:
#								ind = vocabulary.index(s)
#								string_count[ind] = int(string_count[ind]) + 1
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
#						if s not in vocabulary:
#								vocabulary.append(str(s))
#								string_count.append(1)
#						else:
#								ind = vocabulary.index(s)
#								string_count[ind] = int(string_count[ind]) + 1
						if s not in technical_vocabulary:
								technical_vocabulary.append(str(s))
					else:
						removed_words.append(s)
			# Read therapy column in
			str2=row['therapy']
			if(str2 != ''):#!= ''):
				therapy.append([row['therapy'], row['therapy_sh']])
				the_set.add(row['therapy'])
				prt=str(str2).split()
				for s in prt:
					if s not in stopwords:
#						if s not in vocabulary:
#								vocabulary.append(str(s))
#								string_count.append(1)
#						else:
#								ind = vocabulary.index(s)
#								string_count[ind] = int(string_count[ind]) + 1
						if s not in technical_vocabulary:
								technical_vocabulary.append(str(s))
					else:
						removed_words.append(s)
			# Read lifestyle column in
			str2=row['lifestyle']
			if (str2 != ''):
				lifestyle.append([row['lifestyle'], row['lifestyle_sh']])
				lif_set.add(row['lifestyle'])
				prt=str(str2).split()
				for s in prt:
					if s not in stopwords:
#						if s not in vocabulary:
#								vocabulary.append(str(s))
#								#string_count.append(1)
#						else:
#								ind = vocabulary.index(s)
#								string_count[ind] = int(string_count[ind]) + 1
						if s not in technical_vocabulary:
								technical_vocabulary.append(str(s))
					else:
						removed_words.append(s)
	print('Technical vocabulary read in')
	#print(technical_vocabulary)
	#input("Press Enter to continue...")

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

	f=open("output_removed_words.txt","w")
	for s in removed_words:
		f.write(s + ',')
	print('Removed words list created')
	f.close()

def create_histograms():
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
			terms = str(s[3]).split()
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
		f.write(str(t[0]) + ',' + str(t[1]) + ',' + '\n')
		print(t)

	###################################################3
	# Histogram for disease

	print('Histogram for disease words')
	for a in disease:
		counter=0
		if len(a)>0:
			for s in solutions:
				terms = str(s[3]).split()
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
		f.write(str(t[0]) + ',' + str(t[1]) + ',' + str(t[2]) + '\n')
		print(t)

	###########################################
	# histogram for Symptom

	print('Histogram for Symptom words')
	for a in symptom:
		counter=0
		if len(a)>0:
			for s in solutions:
				terms = str(s[3]).split()
				for b in terms:
					if len(b)>0:
						if a_in_b(a[0],b): # Check if even part of word incldues term
							counter=counter+1
			for s in users:
				terms = str(s[1]).split()
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
		f.write(str(t[0]) + ',' + str(t[1]) + ',' + str(t[2]) + '\n')
		print(t)

	##################################################
	# Histogram therapylle

	print('histogram for therapy words')
	for a in therapy:
		counter=0
		if len(a)>0:
			for s in solutions:
				terms = str(s[3]).split()
				for b in terms:
					if len(b)>0:
						if a_in_b(a[0],b): # Check if even part of word incldues term
							counter=counter+1
			for s in users:
				terms = str(s[1]).split()
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
		f.write(str(t[0]) + ',' + str(t[1]) + ',' + str(t[2]) + '\n')
		print(t)

	###############################################
	# Histogram for lifestyle

	print('Histogram for lifestyle words')
	for a in lifestyle:
		counter=0
		if len(a)>0:
			for s in solutions:
				terms = str(s[3]).split()
				for b in terms:
					if len(b)>0:
						if a_in_b(a[0],b): # Check if even part of word incldues term
							counter=counter+1
			for s in users:
				terms = str(s[1]).split()
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
		f.write(str(t[0]) + ',' + str(t[1]) + ',' + str(t[2]) + '\n')
		print(t)

def create_sentiment_analysis():
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

	senti_document_pos = 0
	senti_document_neg = 0
	senti_document_neut = 0

	f=open( "output_sentiment_analysis_documents.csv","w")
	f.write('Document, positive, negative ' + '\n')
	for s in solutions:
		f.write(s[1])
		text_list = str(s[3]).split()
		text_set = set(text_list)
		plus_counter=0
		neg_counter=0
		plus=[]
		neg=[]
		senti_counter = 0
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

		senti_counter = plus_counter - neg_counter  # Document is eiter positive or negative or neutral

		f.write(',' + str(neg_counter))
		f.write(',')
		f.write(str(senti_counter))

		f.write(',')
		f.write(str(plus))
		f.write(',')
		f.write(str(neg))
		f.write('\n')

		if solutions.index(s) > 1:  # 1st header line out of calculation
			if senti_counter > 0:  # Added one more positive document
				senti_document_pos = senti_document_pos + 1
			elif senti_counter < 0:  # Added one more negative document
				senti_document_neg = senti_document_neg + 1
			else:  # Added one more neutral document
				senti_document_neut = senti_document_neut + 1

		sentiment_solutions.append([str(solutions.index(s)), str(plus_counter), str(neg_counter), str(senti_counter)])

	sentiment_solutions.sort(reverse=True, key=toisesta )
	print('Dokumnetit joissa eninten positiivisia sanoja ')
	print(sentiment_solutions[:5])
	sentiment_solutions.sort(reverse=True, key=kolmannesta )
	print(' Dokumnetit joissa eniten negatiiivisia sanoja ')
	print(sentiment_solutions[:5])

	print(' Dokumentit 10 kpl jotka eniten positiivisia ')
	sentiment_solutions.sort(reverse=True, key=neljannesta)
	print(sentiment_solutions[:10])
	print(' Dokumentit 10 kpl jotka eniten negatiiivisia ')
	sentiment_solutions.sort(reverse=False, key=neljannesta)
	print(sentiment_solutions[:10])

	print('   Positive sentiment documents: ', senti_document_pos)  # in users.csv
	print('   Negative sentiment documents: ', senti_document_neg)  # in users.csv
	print('   Neutral  sentiment documents: ', senti_document_neut)  # in users.csv
	print()
	f.close()


	file = open("output_sentiment_of_solutions.csv", "w")  # For plotting pies
	file.write('Positive' + ',' + str(senti_document_pos) + '\n')
	file.write('Negative' + ',' + str(senti_document_neg) + '\n')
	file.write('Neutral ' + ',' + str(senti_document_neut) + '\n')

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
	f.close()

	########################################################
	# Sentiment analysis for users document

	print('Positivness versus negativness in user docuemnts')
	f=open( "output_sentiment_analysis_userdoc.csv","w")
	f.write('Document, positive, negative ' + '\n')

	senti_document_u_pos = 0
	senti_document_u_neg = 0
	senti_document_u_neut = 0

	for s in users:
		f.write(s[0])
		text_list = s[1].split()
		text_set = set(text_list)
		plus_counter=0
		neg_counter=0
		plus=[]
		neg=[]
		senti_counter =0
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

		senti_counter = plus_counter - neg_counter  # Document is eiter positive or negative or neutral

		f.write(',' + str(neg_counter))
		f.write(',')
		f.write(str(senti_counter))
		f.write(',')
		f.write(str(plus))
		f.write(',')
		f.write(str(neg))
		f.write('\n')
		if users.index(s) > 1:
			if senti_counter > 0:
				senti_document_u_pos = senti_document_u_pos + 1
			elif senti_counter < 0:
				senti_document_u_neg = senti_document_u_neg + 1
			else:
				senti_document_u_neut = senti_document_u_neut + 1

		sentiment_users.append([str(users.index(s)), str(plus_counter), str(neg_counter), str(senti_counter)])

	sentiment_users.sort(reverse=True, key=toisesta)
	print( 'Users joissa eniten postitiivisia sanoja ')
	print(sentiment_users[:5])
	print(' users joissa eniten negatiivisia sanoja ')
	sentiment_users.sort(reverse=True, key=kolmannesta)
	print(sentiment_users[:5])

	print()
	print(' Users 10 kpl jotka eniten positiivisia ')
	sentiment_users.sort(reverse=True, key=neljannesta )
	print(sentiment_users[:10])

	print(' Users 10 kpl jotka eniten negatiiivisia ')
	sentiment_users.sort(reverse=False, key=neljannesta )
	print(sentiment_users[:10])

	print('   Positive sentiment documents: ', senti_document_u_pos)
	print('   Negative sentiment documents: ', senti_document_u_neg)
	print('   Neutral  sentiment documents: ', senti_document_u_neut)
	print()
	f.close()

	file=open( "output_sentiment_of_users.csv","w")
	file.write('Positive' + ',' + str(senti_document_u_pos) + '\n')
	file.write('Negative' + ',' + str(senti_document_u_neg) + '\n')
	file.write('Neutral ' + ',' + str(senti_document_u_neut) + '\n')
	f.close()

def compare_documents_with_technical_voc():
	#########################################################################
	#########################################################################
	# Overlapping between user documents and technical vocabulary
	#########################################################################

	technical_vocabulary_set = set(technical_vocabulary)
	print('Common words in reference vs. technical vocabulary in users file')
	f=open( "output_intersection_with_reference_for_users_doc.csv","w")
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
		same_words = []
		text_set = set(str(s[3]).split())
		diff_set=set(text_set.difference(technical_vocabulary_set))
		leikkaus_set=set(text_set.intersection(technical_vocabulary_set))
		#print('Doc:' + s[1] + ' Common: ' + str(len(leikkaus_set)) + ', Different: ' + str(len(diff_set)))
		f.write(s[1])
		for sana in technical_vocabulary:
			if( sana in list(leikkaus_set)):
				f.write(',' + '1')
				same_words.append(sana)
			else:
				f.write(',')
				sss="0"

		f.write(',' + str(len(leikkaus_set)) + ',' + str(len(diff_set)))
		same_set = set(same_words)
		f.write(',' + str(len(dis_set.intersection(same_set))) + ',' + str(len(sym_set.intersection(same_set))) + ',' + str(len(the_set.intersection(same_set))) + ','+ str(len(lif_set.intersection(same_set))))
		for p in list(same_set):
			f.write(', ' + str(p) + ' ' )
		f.write('\n')

	f.close()
	################################################################
	# Overlapping between user documents with other user document

	words = []
	common_words =[]

	print('Then calculate intersection with all other user documents')
	f=open( "output_document_vs_document_similarity.csv","w")
	cfile=open( "output_document_commonality.csv","w")
	f.write(' ')
	for s in solutions:
		f.write(','+ s[1] )
	f.write('\n')
	for s in solutions:
		text_set = set(str(s[3]).split())
		common_list = []
		f.write(s[1])
		cfile.write(s[1])
		for d in solutions:
			# verrataan jokaiseen solutionin settiin
			leikkaus_set=set(text_set.intersection(set(str(d[3]).split())))
			# muodostetaan samalla yhteistä listaa kaikista
			f.write(',' + str(len(leikkaus_set)))
			if (s == d):
				cfile.write(',' + str(len(leikkaus_set)))
				words.append(str(len(leikkaus_set)))
			for i in leikkaus_set:
				if(s != d): # Decline diagonal, comparison against itself
					if i not in common_list:
						common_list.append(i)

		f.write(',' + str(len(common_list)) + '\n')

		cfile.write(',' + str(len(common_list)) + '\n')
		common_words.append(str(len(common_list)))

	f.close()

	lista = []
	for s in words:
		lista.append([s, common_words[words.index(s)]])
	lista.sort(reverse = False, key = toisesta )
	words=[]
	common_words = []
	for s in lista:
		words.append(s[0])
		common_words.append(s[1])

	import matplotlib
	import matplotlib.pyplot as plt
	import numpy as np

"""
	# Data for plotting
	for i in common_words:
		common_words[common_words.index(i)] = int(i)
	for i in words:
		words[words.index(i)] = int(i)
	fig=  plt.figure()
	ax = plt.subplot(111)
	line2 = ax.plot( np.array(common_words))
	line1 = ax.plot( np.array(words))

	ax.set(xlabel='Documents', ylabel='Number of words',
		title='Common words in documents, sorted by number of common words')
	ax.grid()

	fig.savefig("test.png")
	plt.show()
"""

def main():
	create_vocabulary()
	create_histograms()
	create_sentiment_analysis()
	compare_documents_with_technical_voc()

