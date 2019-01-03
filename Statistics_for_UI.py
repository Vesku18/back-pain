import numpy as np
import csv
import matplotlib.pyplot as plt
import matplotlib.colors
#matplotlib.style.use('ggplot')
import pandas as pd
from tkinter import *
from pandastable import Table, TableModel


################################
###### Subplot ages + ages if high pain:

def ages_and_ages_with_pain(reader, csvfile):
        d=[]
        csvfile.seek(0) # going back to...
        next(reader)    # ...the second line of csv file
        for row in reader:
                age=row['age']
                age=float(age)
                if abs(age) < 130:
                    if abs(age) > 5:
                        d.append(abs(age))        
        fig32, axs = plt.subplots(1, 2, sharey=True, figsize=(10,6))
        plt.rcParams["patch.force_edgecolor"] = True

        weights = np.ones_like(d)/float(len(d)) # sum of bar heights => 1
        N, bins, patches = axs[0].hist(x=sorted(d), bins=[20,25,30,35,40,45,50,55,60,65,70,75,80], facecolor='green',
                            alpha=0.8, rwidth=1.0, weights=weights)
        my_xticks = [20,25,30,35,40,45,50,55,60,65,70,75,80] #x-axis numbering
        plt.setp(axs, xticks = my_xticks)#, yticks = [0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45])
        axs[0].grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        axs[0].set_title('Users\' age distribution',fontsize=14)
        axs[0].set_ylabel('Sum of bar heights = 1')
        axs[0].set_xlabel('Age (years)')

        csvfile.seek(0)
        next(reader)
        d2=[]
        for row in reader:
                p = float(row['suffersnowpain'])
                age = float(row['age'])
                if (abs(age) < 130 and abs(age) > 5):
                    if p > 7:
                        d2.append(abs(age))

        weights = np.ones_like(d2)/float(len(d2)) # sum of bar heights => 1
        N, bins, patches = axs[1].hist(x=sorted(d2), bins=[20,25,30,35,40,45,50,55,60,65,70,75,80], facecolor='orange',
                            alpha=0.8, rwidth=1.0, weights=weights)
        axs[1].grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        axs[1].set_title('Users\' age distribution if pain now > 7',fontsize=14)
        axs[1].set_ylabel('Sum of bar heights = 1')
        axs[1].set_xlabel('Age (years)')
        #plt.savefig("subplot_ages.png") 
#################################



#################################
###### Subplot Pain:
def pain(reader, csvfile):
        d=[]
        d2=[]
        csvfile.seek(0)
        next(reader)
        for row in reader:
                pain=row['suffersnowpain']
                p = float(pain)
                if not p == -1:
                        d.append(p)
        plt.rcParams["patch.force_edgecolor"] = True
        weights = np.ones_like(d)/float(len(d)) # sum of bar heights => 1
        fig31, axs = plt.subplots(1, 2, sharey=True, figsize=(10,6))
        N, bins, patches = axs[0].hist(x=sorted(d), bins=[-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13], facecolor='red',
                            alpha=1.0, rwidth=0.6, align='left', weights=weights)
        my_xticks = [0,1,2,3,4,5,6,7,8,9,10,11,12] #x-axis numbering
        plt.setp(axs[0], xticks = my_xticks, yticks = [0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.50,0.55,0.60])
        axs[0].grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        axs[0].set_title('Users\' pain level at the moment',fontsize=14)
        axs[0].text(2.15, 0.22, '0 = no pain \n12 = maximal pain', fontsize=12)
        axs[0].set_ylabel('Sum of bar heights = 1')

        csvfile.seek(0)
        next(reader)
        for row in reader:
                pain1=row['sufferedpastpain']  
                pain2=row['sufferedpastsciaticapain']
                p1 = float(pain1)
                p2 = float(pain2)
                if not p1 == -1:
                        d2.append(p1)
                if not p2 == -1:
                        d2.append(p2)        
        weights = np.ones_like(d2)/float(len(d2)) # sum of bar heights => 1
        N, bins, patches = axs[1].hist(x=sorted(d2), bins=[-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13], facecolor='orange',
                            alpha=1.0, rwidth=0.6, align='left', weights=weights)               
        my_xticks = [0,1,2,3] #x-axis numbering
        plt.setp(axs[1], xticks = my_xticks, yticks = [0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.50,0.55,0.60])
        axs[1].grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        axs[1].set_title('Users\' pain experience in the past',fontsize=14)
        axs[1].text(4.25, 0.2, '0 = no \n1 = yes \n2 = not relapsed \n3 = relapsed', fontsize=12)         
        axs[1].set_ylabel('Sum of bar heights = 1')
        #plt.savefig("subplot_pain.png")


####################################

    

####################################
######### Correlations:
def corr_matrix(reader, csvfile):
        csvfile.seek(0)
        next(reader)
        d1=[]
        d2=[]
        d3=[]
        d4=[]
        d5=[]
        d6=[]
        d7=[]
        d8=[]
        d9=[]
        for row in reader:
                age=row['age']
                job=row['jobsituation']
                gend=row['gender']
                pain1=row['sufferedpastpain']  
                pain2=row['sufferedpastsciaticapain']
                painnow=row['suffersnowpain']
                howactive=row['howactive']
                surgery=row['surgerydone']
                edudeg=row['degree']
                age=float(age)
                if (abs(age) < 130 and abs(age) > 5):
                        if not (job == '-1' or gend == '-1'):
                                if not (pain1 == '-1' or pain2 == '-1'):
                                        if not (painnow == '-1' or howactive == '-1'):
                                                        if not (surgery == '-1' or edudeg == '-1'):
                                                                d1.append(abs(age))
                                                                d2.append(float(job))
                                                                d3.append(float(gend))
                                                                d4.append(float(pain1))                                                 
                                                                d5.append(float(pain2))
                                                                d6.append(float(painnow))
                                                                d7.append(float(howactive))
                                                                d8.append(float(surgery))
                                                                d9.append(float(edudeg))
        
        df = pd.DataFrame({'age': d1})
        df['jobsit.'] = d2
        df['gender'] = d3
        df['pastpain']= d4
        df['pastsciatica'] = d5
        df['nowpain'] = d6                                          
        df['howactive'] = d7
        df['surgery'] = d8
        df['education'] = d9

        # Correlation matrix:
        dfcor = df.corr(method='pearson')
        dfcor_final = dfcor.round(3) # Taking 3 decimals to results
        
        #dfcor_final.to_csv('corr_matrix.csv', sep=',', encoding='utf-8')

        #with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        #       print(dfcor_final)
                      
        
        # Table to UI:
        class CorTable(Frame):
                def __init__(self, parent=None):
                        self.parent = parent
                        Frame.__init__(self)
                        self.main = self.master
                        #self.main.geometry('600x400+200+100')
                        #self.main.title('Table app')
                        f = Frame(self.main)
                        f.pack(fill=BOTH,expand=1)
                        dfcor_final['index'] = ['age', 'jobsit.', 'gender', 'pastpain', 'pastsciatica', 'nowpain', 'howactive', 'surgery', 'education']
                        self.table = pt = Table(f, dataframe=dfcor_final,
                        showtoolbar=True, showstatusbar=True)
                        
                        pt.show()

        CorTable()
        #app = TestApp()
        #launch the app
        #app.mainloop()

        # Correlation "heatmap":   
        fig20 = plt.figure(20)
        fig20.set_size_inches(7.5, 7)
        plt.imshow(df.corr(method='pearson'), cmap=plt.cm.Reds, interpolation='none')
        plt.colorbar()
        tick_marks = [i for i in range(len(df.columns))]
        plt.xticks(tick_marks, df.columns, rotation='vertical')
        plt.yticks(tick_marks, df.columns)
        plt.title('Correlations between variables',fontsize=18)
        plt.show()
        #plt.savefig('Corr_heatmap.png')
        
############################################        


############################################
####### Gender subplot:
def gender_subplot(reader, csvfile):
        d=[]
        d2=[]
        csvfile.seek(0)
        next(reader)
        for row in reader:
                g=row['gender']
                gend=float(g)
                if not gend == -1:
                        d.append(gend)
        plt.rcParams["patch.force_edgecolor"] = True
        weights = np.ones_like(d)/float(len(d)) # sum of bar heights => 1
        fig33, axs = plt.subplots(1, 2, sharey=True, figsize=(10,6))
        N, bins, patches = axs[0].hist(x=d, bins=[1,2,3], facecolor='blue',
                            alpha=1.0, rwidth=0.4, align='left', weights=weights)
        my_xticks = [1,2] #x-axis numbering
        plt.setp(axs[0], xticks = my_xticks, yticks = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8])
        axs[0].grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        axs[0].set_title('Gender distribution of the users',fontsize=14)
        axs[0].text(1, 0.41, '1 = male \n2 = female', fontsize=12)
        axs[0].set_ylabel('Sum of bar heights = 1')

        csvfile.seek(0)
        next(reader)
        for row in reader:
                pain1=row['sufferedpastpain']  
                pain2=row['sufferedpastsciaticapain']
                gend=row['gender']
                g=float(gend)
                p1 = float(pain1)
                p2 = float(pain2)
                if not (p1 == -1 and p2 == -1):
                        if p1 == 3 or p2 == 3:
                                if g==1 and not (g==-1 or g==3):
                                        d2.append(g);
                                else:
                                        d2.append(g);
        weights = np.ones_like(d2)/float(len(d2)) # sum of bar heights => 1
        N, bins, patches = axs[1].hist(x=sorted(d2), bins=[1,2,3], facecolor='red',
                            alpha=1.0, rwidth=0.4, align='left', weights=weights)               
        my_xticks = [1,2] #x-axis numbering
        plt.setp(axs[1], xticks = my_xticks, yticks = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8])
        axs[1].grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        axs[1].set_title('Users with relapsed pain',fontsize=14)
        axs[1].text(1.2, 0.3, '1 = male \n2 = female', fontsize=12)         
        axs[1].set_ylabel('Sum of bar heights = 1')
        plt.savefig("subplot_gender.png")

############################################


def gender_vs_nowpain(reader, csvfile):
        csvfile.seek(0)
        next(reader)
        mpain=[]
        fpain=[]
        for row in reader:
                pain=row['suffersnowpain']
                g=row['gender']
                p = float(pain)
                if not p == -1:
                        if g=='1' and not g=='-1':
                                mpain.append(p)
                        else:
                                fpain.append(p)

        plt.rcParams["patch.force_edgecolor"] = True
        fig9, axs = plt.subplots(1, 2, sharey=True, figsize=(9,6))
        weights = np.ones_like(mpain)/float(len(mpain)) # sum of bar heights => 1
        N, bins, patches = axs[0].hist(x=sorted(mpain), bins=[-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13], facecolor='blue',
                            alpha=1.0, rwidth=0.5, align='left', weights=weights)
        my_xticks = [0,1,2,3,4,5,6,7,8,9,10,11,12] #x-axis numbering
        plt.setp(axs, xticks = my_xticks, yticks = [0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45])
        axs[0].grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        axs[0].set_title('Males\' pain level at the moment',fontsize=14)
        axs[0].text(2.15, 0.22, '0 = no pain \n12 = maximal pain', fontsize=12)
        axs[0].set_ylabel('Sum of bar heights = 1')

        weights = np.ones_like(fpain)/float(len(fpain)) # sum of bar heights => 1
        N, bins, patches = axs[1].hist(x=sorted(fpain), bins=[-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13], facecolor='red',
                            alpha=1.0, rwidth=0.4, align='left', weights=weights)
        axs[1].grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        axs[1].set_title('Females\' pain level at the moment',fontsize=14)
        axs[1].text(2.15, 0.22, '0 = no pain \n12 = maximal pain', fontsize=12)      
        axs[1].set_ylabel('Sum of bar heights = 1')
        #plt.savefig("Gender_pain_distribution.png")

def gender_vs_age_if_highpain(reader, csvfile):
        csvfile.seek(0)
        next(reader)
        mage=[]
        fage=[]
        for row in reader:
                a=row['age']
                g=row['gender']
                age = float(a)
                p=row['suffersnowpain']
                pain = float(p)
                if abs(age) < 130:
                    if abs(age) > 5:
                            if pain > 7: 
                                if g=='1' and not g=='-1':
                                        mage.append(abs(age))
                                else:
                                        fage.append(abs(age))
                
        plt.rcParams["patch.force_edgecolor"] = True
        fig18, axs = plt.subplots(1, 2, sharey=True, figsize=(8,6))
        weights = np.ones_like(mage)/float(len(mage)) # sum of bar heights => 1
        N, bins, patches = axs[0].hist(x=sorted(mage), bins=[20,25,30,35,40,45,50,55,60,65,70,75,80], facecolor='blue',
                            alpha=1.0, rwidth=1.0, weights=weights)
        my_xticks = [20,25,30,35,40,45,50,55,60,65,70,75,80] #x-axis numbering
        plt.setp(axs, xticks = my_xticks)#, yticks = [0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45])
        axs[0].grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        axs[0].set_title('Males\' ages if pain now > 7',fontsize=14)
        axs[0].set_ylabel('Sum of bar heights = 1')
        axs[0].set_xlabel('Age (years)')


        weights = np.ones_like(fage)/float(len(fage)) # sum of bar heights => 1
        N, bins, patches = axs[1].hist(x=sorted(fage), bins=[20,25,30,35,40,45,50,55,60,65,70,75,80], facecolor='red',
                            alpha=1.0, rwidth=1.0, weights=weights)
        axs[1].grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        axs[1].set_title('Females\' ages if pain now > 7',fontsize=14)
        axs[1].set_ylabel('Sum of bar heights = 1')
        axs[1].set_xlabel('Age (years)')      
        #plt.savefig("Gender_age_if_high_pain_distribution.png")

                




##################################
###### Job subplot:
def job_subplot(reader, csvfile):
        csvfile.seek(0)
        next(reader)
        d=[]
        job=[]
        job2=[]
        for row in reader:
                j=row['jobsituation']
                j2=float(j)
                if not j2 == -1:
                        d.append(j2)  
        plt.figure(40, figsize = (11,11))
        plt.rcParams["patch.force_edgecolor"] = True
        
        plt.subplot(221)
        weights = np.ones_like(d)/float(len(d)) # sum of bar heights => 1
        n, bins, patches = plt.hist(x=d, bins=[1,2,3,4], facecolor='blue',
                            alpha=0.6, rwidth=0.5, align='left', weights=weights)
        my_xticks = [1,2,3] #x-axis numbering
        plt.xticks(my_xticks)
        plt.grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        plt.xlabel('')
        plt.ylabel('Sum of bar heights = 1',fontsize=10)
        plt.title('Job situation of the users',fontsize=14)
        plt.text(1.6, 0.32, '1 = full time job \n2 = part time job\n3 = retired or unemployed',
                 fontsize=10, alpha=1.0)
        maxfreq = n.max()

        csvfile.seek(0)
        next(reader)
        for row in reader:
                pain = row['suffersnowpain']
                jobsit = row['jobsituation']
                p = float(pain)
                j = float(jobsit)
                if (p > 7 and j > 0):
                        job.append(j)
        plt.subplot(222)               
        weights = np.ones_like(job)/float(len(job)) # sum of bar heights => 1
        n, bins, patches = plt.hist(x=job, bins=[1,2,3,4], facecolor='blue',
                            alpha=0.6, rwidth=0.5, align='left', weights=weights)
        my_xticks = [1,2,3] #x-axis numbering
        plt.xticks(my_xticks)
        plt.grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        plt.xlabel('')
        plt.ylabel('Sum of bar heights = 1',fontsize=10)
        plt.title('Job situation if pain now > 7',fontsize=14)
        plt.text(1.3, 0.3, '1 = full time job \n2 = part time job\n3 = retired or unemployed',
                 fontsize=10)
        maxfreq = n.max()

        
        csvfile.seek(0)
        next(reader)
        for row in reader:
                pain1=row['sufferedpastpain']  
                pain2=row['sufferedpastsciaticapain']
                jobsit = row['jobsituation']
                p1 = float(pain1)
                p2 = float(pain2)
                j = float(jobsit)
                if j > 0:
                        if p1 == 3:
                                job2.append(j)
                        else:
                                if p2 == 3:
                                        job2.append(j)
        plt.subplot(223)                    
        weights = np.ones_like(job2)/float(len(job2)) # sum of bar heights => 1        
        n, bins, patches = plt.hist(x=job2, bins=[1,2,3,4], facecolor='blue',
                            alpha=0.6, rwidth=0.5, align='left', weights=weights)
        my_xticks = [1,2,3] #x-axis numbering
        plt.xticks(my_xticks)       
        plt.grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        plt.xlabel('')
        plt.ylabel('Sum of bar heights = 1',fontsize=10)
        plt.title('Job situation if relapsed pain',fontsize=14)
        plt.text(1.3, 0.3, '1 = full time job \n2 = part time job\n3 = retired or unemployed',
                 fontsize=10)
        maxfreq = n.max()

        csvfile.seek(0)
        next(reader)
        job3=[]
        for row in reader:
                pain1=row['sufferedpastpain']  
                pain2=row['sufferedpastsciaticapain']
                jobsit = row['jobsituation']
                pain = row['suffersnowpain']
                p1 = float(pain1)
                p2 = float(pain2)
                p = float(pain)
                j = float(jobsit)
                if j > 0:
                        if (p > 6):
                                if p1 == 3:
                                        job3.append(j)
                                else:
                                        if p2 == 3:
                                                job3.append(j)
                                                
        plt.subplot(224)      
        weights = np.ones_like(job3)/float(len(job3)) # sum of bar heights => 1
        n, bins, patches = plt.hist(x=job3, bins=[1,2,3,4], facecolor='blue',
                            alpha=0.6, rwidth=0.5, align='left', weights=weights)
        my_xticks = [1,2,3] #x-axis numbering
        plt.xticks(my_xticks)
        plt.grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        plt.xlabel('')
        plt.ylabel('Sum of bar heights = 1',fontsize=10)
        plt.title('Job situation if pain now and in past',fontsize=14)
        plt.text(1.3, 0.3, '1 = full time job \n2 = part time job\n3 = retired or unemployed',
                 fontsize=10)
        maxfreq = n.max() 
        plt.savefig("subplot_job.png")

##################################



           

def gender_vs_jobsituation(reader, csvfile):
        csvfile.seek(0)
        next(reader)
        mjob=[]
        fjob=[]
        for row in reader:
                j=row['jobsituation']
                g=row['gender']
                job = float(j)
                if not job == -1:
                        if g=='1' and not g=='-1':
                                mjob.append(job)
                        else:
                                fjob.append(job)

        plt.rcParams["patch.force_edgecolor"] = True
        fig12, axs = plt.subplots(1, 2, sharey=True, figsize=(10,6))
        weights = np.ones_like(mjob)/float(len(mjob)) # sum of bar heights => 1
        N, bins, patches = axs[0].hist(x=sorted(mjob), bins=[1,2,3,4], facecolor='blue',
                            alpha=0.8, rwidth=0.6, align='left', weights=weights)
        my_xticks = [1,2,3] #x-axis numbering
        plt.setp(axs, xticks = my_xticks)#, yticks = [0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45])
        axs[0].grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        axs[0].set_title('Males\' job situation',fontsize=14)
        axs[0].text(1.6, 0.42, '1 = full time job \n2 = part time job\n3 = retired or unemployed', fontsize=12)
        axs[0].set_ylabel('Sum of bar heights = 1')

        weights = np.ones_like(fjob)/float(len(fjob)) # sum of bar heights => 1
        N, bins, patches = axs[1].hist(x=sorted(fjob), bins=[1,2,3,4], facecolor='red',
                            alpha=0.8, rwidth=0.6, align='left', weights=weights)
        axs[1].grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        axs[1].set_title('Females\' job situation',fontsize=14)
        axs[1].text(1.6, 0.42, '1 = full time job \n2 = part time job\n3 = retired or unemployed', fontsize=12)      
        #plt.savefig("Gender_job_distribution.png")



def gender_vs_jobsituation_if_high_pain_now(reader, csvfile):
        csvfile.seek(0)
        next(reader)
        mjob=[]
        fjob=[]
        for row in reader:
                j=row['jobsituation']
                g=row['gender']
                p=row['suffersnowpain']
                pain=float(p)
                job = float(j)
                if not job == -1:
                        if pain > 7:
                                if g=='1' and not g=='-1':
                                        mjob.append(job)
                                else:
                                        fjob.append(job)
               
        plt.rcParams["patch.force_edgecolor"] = True
        fig14, axs = plt.subplots(1, 2, sharey=True, figsize=(10,6))
        weights = np.ones_like(mjob)/float(len(mjob)) # sum of bar heights => 1
        N, bins, patches = axs[0].hist(x=sorted(mjob), bins=[1,2,3,4], facecolor='blue',
                            alpha=0.8, rwidth=0.6, align='left', weights=weights)
        my_xticks = [1,2,3] #x-axis numbering
        plt.setp(axs, xticks = my_xticks)#, yticks = [0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45])
        axs[0].grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        axs[0].set_title('Males\' job situation if pain now > 7',fontsize=14)
        axs[0].text(1.36, 0.3, '1 = full time job \n2 = part time job\n3 = retired or\n       unemployed', fontsize=12)
        axs[0].set_ylabel('Sum of bar heights = 1')

        weights = np.ones_like(fjob)/float(len(fjob)) # sum of bar heights => 1
        N, bins, patches = axs[1].hist(x=sorted(fjob), bins=[1,2,3,4], facecolor='red',
                            alpha=0.8, rwidth=0.6, align='left', weights=weights)
        axs[1].grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        axs[1].set_title('Females\' job situation if pain now > 7',fontsize=14)
        axs[1].text(1.36, 0.3, '1 = full time job \n2 = part time job\n3 = retired or\n       unemployed', fontsize=12)      
        #plt.savefig("Gender_job_highpain_distribution.png")

def gender_vs_age(reader, csvfile):
        csvfile.seek(0)
        next(reader)
        mage=[]
        fage=[]
        for row in reader:
                a=row['age']
                g=row['gender']
                age = float(a)
                if abs(age) < 130:
                    if abs(age) > 5:
                        if g=='1' and not g=='-1':
                                mage.append(abs(age))
                        else:
                                fage.append(abs(age))
        
        plt.rcParams["patch.force_edgecolor"] = True
        fig13, axs = plt.subplots(1, 2, sharey=True, figsize=(10,6))
        weights = np.ones_like(mage)/float(len(mage)) # sum of bar heights => 1
        N, bins, patches = axs[0].hist(x=sorted(mage), bins=[20,25,30,35,40,45,50,55,60,65,70,75,80], facecolor='green',
                            alpha=0.8, rwidth=1.0, weights=weights)
        my_xticks = [20,25,30,35,40,45,50,55,60,65,70,75,80] #x-axis numbering
        plt.setp(axs, xticks = my_xticks)#, yticks = [0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45])
        axs[0].grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        axs[0].set_title('Males\' age distribution',fontsize=14)
        axs[0].set_ylabel('Sum of bar heights = 1')
        axs[0].set_xlabel('Age (years)')


        weights = np.ones_like(fage)/float(len(fage)) # sum of bar heights => 1
        N, bins, patches = axs[1].hist(x=sorted(fage), bins=[20,25,30,35,40,45,50,55,60,65,70,75,80], facecolor='orange',
                            alpha=1.0, rwidth=1.0, weights=weights)
        axs[1].grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        axs[1].set_title('Females\' age distribution',fontsize=14)
        axs[1].set_ylabel('Sum of bar heights = 1')
        axs[1].set_xlabel('Age (years)')      
        #plt.savefig("Gender_age_distribution.png")
        
		
		
def education_distribution(reader, csvfile):
        d=[]
        fig15 = plt.figure(15)
        figure = fig15
        csvfile.seek(0) # going back to...
        next(reader)    # ...the second line of csv file
        for row in reader:
                e=row['degree']
                edu=float(e)
                if edu > -1:
                        d.append(edu)

        plt.rcParams["patch.force_edgecolor"] = True
        weights = np.ones_like(d)/float(len(d)) # sum of bar heights => 1
        n, bins, patches = plt.hist(x=d, bins=[1,2,3,4,5,6,7,8,9],
                                    facecolor='orange',alpha=1.0, rwidth=0.6, weights=weights, align='left')
        plt.grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        plt.xlabel('Education',fontsize=16)
        plt.ylabel('Sum of bar heights = 1',fontsize=14)
        plt.title('Educational distribution of the users',fontsize=22)
        plt.text(2.6, 0.15, '1 = Lowest\n       education \n\n8 = Doctoral\n       degree',
                 fontsize=14)
        maxfreq = n.max()
        #plt.savefig("Educational_distribution.png") 

def education_vs_highpain(reader, csvfile):
        d=[]
        fig16 = plt.figure(16)
        figure = fig16
        csvfile.seek(0) # going back to...
        next(reader)    # ...the second line of csv file
        for row in reader:
                p=row['suffersnowpain']
                pain=float(p)
                e=row['degree']
                edu=float(e)
                if edu > -1 and pain > 7:
                        d.append(edu)

        plt.rcParams["patch.force_edgecolor"] = True
        weights = np.ones_like(d)/float(len(d)) # sum of bar heights => 1
        n, bins, patches = plt.hist(x=d, bins=[1,2,3,4,5,6,7,8,9],
                                    facecolor='red',alpha=0.7, rwidth=0.6, weights=weights, align='left')
        plt.grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        plt.xlabel('Education',fontsize=16)
        plt.ylabel('Sum of bar heights = 1',fontsize=14)
        plt.title('Education if pain now > 7',fontsize=22)
        plt.text(2.6, 0.15, '1 = Lowest\n       education \n\n8 = Doctoral\n       degree',
                 fontsize=14)
        maxfreq = n.max()
        #plt.savefig("Education_vs_highpain_distribution.png") 


def gender_vs_education(reader, csvfile):
        csvfile.seek(0)
        next(reader)
        medu=[]
        fedu=[]
        for row in reader:
                e=row['degree']
                g=row['gender']
                edu = float(e)
                if g=='1' and not g=='-1':
                        medu.append(edu)
                else:
                        fedu.append(edu)
                        
        plt.rcParams["patch.force_edgecolor"] = True
        fig17, axs = plt.subplots(1, 2, sharey=True, figsize=(10,6))
        weights = np.ones_like(medu)/float(len(medu)) # sum of bar heights => 1
        N, bins, patches = axs[0].hist(x=sorted(medu), bins=[1,2,3,4,5,6,7,8,9], facecolor='orange',
                            alpha=0.8, rwidth=0.6, weights=weights, align='left')
        my_xticks = [1,2,3,4,5,6,7,8] #x-axis numbering
        plt.setp(axs, xticks = my_xticks)#, yticks = [0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45])
        axs[0].grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        axs[0].set_title('Males\' education',fontsize=14)
        axs[0].set_ylabel('Sum of bar heights = 1')
        axs[0].set_xlabel('Education')


        weights = np.ones_like(fedu)/float(len(fedu)) # sum of bar heights => 1
        N, bins, patches = axs[1].hist(x=sorted(fedu), bins=[1,2,3,4,5,6,7,8,9], facecolor='red',
                            alpha=0.6, rwidth=0.6, weights=weights, align='left')
        axs[1].grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        axs[1].set_title('Females\' education',fontsize=14)
        axs[1].set_ylabel('Sum of bar heights = 1')
        axs[1].set_xlabel('Education')
        #plt.savefig("Gender_education_distribution.png")



