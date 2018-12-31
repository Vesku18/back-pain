import numpy as np
import csv
import matplotlib.pyplot as plt
import matplotlib.colors
#matplotlib.style.use('ggplot')
import pandas as pd


# Age distribution:
def ages(reader, csvfile):
        d=[]
        fig1 = plt.figure(1)
        csvfile.seek(0) # going back to...
        next(reader)    # ...the second line of csv file
        for row in reader:
                age=row['age']
                age=float(age)
                if abs(age) < 130:
                    if abs(age) > 5:
                        d.append(abs(age))

        plt.rcParams["patch.force_edgecolor"] = True
        weights = np.ones_like(d)/float(len(d)) # sum of bar heights => 1
        n, bins, patches = plt.hist(x=d, bins=[20,25,30,35,40,45,50,55,60,65,70,75,80],
                                    facecolor='green',alpha=0.9, rwidth=1.0, weights=weights)
        plt.grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        plt.xlabel('Age (years)',fontsize=16)
        plt.ylabel('Sum of bar heights = 1',fontsize=14)
        plt.title('Age distribution of the users',fontsize=22)

        maxfreq = n.max()
        plt.savefig("Age_distribution.png")

# Job situations:
def jobsit(reader, csvfile):
        d=[]
        fig2 = plt.figure(2)
        csvfile.seek(0)
        next(reader)
        for row in reader:
                j=row['jobsituation']
                job=float(j)
                if not job == -1:
                        d.append(job)                
        plt.rcParams["patch.force_edgecolor"] = True
        weights = np.ones_like(d)/float(len(d)) # sum of bar heights => 1
        n, bins, patches = plt.hist(x=d, bins=[1,2,3,4], facecolor='blue',
                            alpha=1.0, rwidth=0.5, align='left', weights=weights)
        my_xticks = [1,2,3] #x-axis numbering
        plt.xticks(my_xticks)
        plt.grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        plt.xlabel('')
        plt.ylabel('Sum of bar heights = 1',fontsize=14)
        plt.title('Job situation of the users',fontsize=22)
        plt.text(1.6, 0.32, '1 = full time job \n2 = part time job\n3 = retired or unemployed',
                 fontsize=14, alpha=1.0)
        maxfreq = n.max()
        plt.savefig("Job_situation_distribution.png")


# Pain at the moment:
def nowpain(reader, csvfile):
        d=[]
        fig3 = plt.figure(3)
        csvfile.seek(0)
        next(reader)
        for row in reader:
                pain=row['suffersnowpain']
                p = float(pain)
                if not p == -1:
                        d.append(p)
        plt.rcParams["patch.force_edgecolor"] = True
        weights = np.ones_like(d)/float(len(d)) # sum of bar heights => 1
        n, bins, patches = plt.hist(x=sorted(d), bins=[0,1,2,3,4,5,6,7,8,9,10,11,12,13], facecolor='red',
                            alpha=1.0, rwidth=0.6, align='left', weights=weights)
        my_xticks = [0,1,2,3,4,5,6,7,8,9,10,11,12] #x-axis numbering
        plt.xticks(my_xticks)
        plt.grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        plt.xlabel('')
        plt.ylabel('Sum of bar heights = 1')
        plt.title('Users\' pain level at the moment',fontsize=22)
        plt.text(4.35, 0.16, '0 = no pain \n12 = maximal pain', fontsize=14)
        maxfreq = n.max()  
        plt.savefig("Now_pain_distribution.png")

                
# Past pain ("normal" + sciatica):
def pastpain(reader, csvfile):
        d=[]
        csvfile.seek(0)
        next(reader)
        fig4 = plt.figure(4)
        for row in reader:
                pain1=row['sufferedpastpain']  
                pain2=row['sufferedpastsciaticapain']
                p1 = float(pain1)
                p2 = float(pain2)
                if not p1 == -1:
                        d.append(p1)
                if not p2 == -1:
                        d.append(p2)        
        plt.rcParams["patch.force_edgecolor"] = True
        weights = np.ones_like(d)/float(len(d)) # sum of bar heights => 1
        n, bins, patches = plt.hist(x=sorted(d), bins=[0,1,2,3,4], facecolor='yellow',
                            alpha=1.0, rwidth=0.6, align='left', weights=weights)
        my_xticks = [0,1,2,3] #x-axis numbering
        plt.xticks(my_xticks)
        plt.grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        plt.xlabel('')
        plt.ylabel('Sum of bar heights = 1')
        plt.title('Users\' pain experience in the past',fontsize=22)
        plt.text(0.45, 0.3, '0 = no \n1 = yes \n2 = not relapsed \n3 = relapsed',fontsize=14)
        maxfreq = n.max()
        plt.savefig("Past_pain_distribution.png")
         

# Gender distribution:
def gender(reader, csvfile):
        d=[]
        csvfile.seek(0)
        next(reader)
        fig5 = plt.figure(5)
        for row in reader:
                g=row['gender']
                gend=float(g)
                if not gend == -1:
                        d.append(gend)
        
        plt.rcParams["patch.force_edgecolor"] = True
        weights = np.ones_like(d)/float(len(d)) # sum of bar heights => 1
        n, bins, patches = plt.hist(x=d, bins=[1,2,3], facecolor='blue',
                            alpha=0.8, rwidth=0.3, align='left', weights=weights)
        my_xticks = [1,2] #x-axis numbering
        plt.xticks(my_xticks)
        plt.grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        plt.xlabel('')
        plt.ylabel('Sum of bar heights = 1',fontsize=14)
        plt.title('Gender distribution of the users',fontsize=22)
        plt.text(1, 0.41, '1 = male \n2 = female', fontsize=14)
        maxfreq = n.max()
        plt.savefig("Gender_distribution.png")

# Correlations:
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
        dfcor_final.to_csv('corr_matrix.csv', sep=',', encoding='utf-8')
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):
                print(dfcor_final)
                
        # Correlation "heatmap":
        fig20 = plt.figure(20)
        fig20.set_size_inches(8, 7.5)
        plt.imshow(df.corr(method='pearson'), cmap=plt.cm.Reds, interpolation='none')
        plt.colorbar()
        tick_marks = [i for i in range(len(df.columns))]
        plt.xticks(tick_marks, df.columns, rotation='vertical')
        plt.yticks(tick_marks, df.columns)
        plt.title('Pearson correlations between variables',fontsize=18)
        plt.savefig('Corr_heatmap.png')
                

# Current high pain rate and job situation:
def painjob(reader, csvfile):
        csvfile.seek(0)
        next(reader)
        highpain=[]
        job=[]
        for row in reader:
                pain = row['suffersnowpain']
                jobsit = row['jobsituation']
                p = float(pain)
                j = float(jobsit)
                if (p > 7 and j > 0):
                        highpain.append(p)
                        job.append(j)

        fig6 = plt.figure(6)             
        plt.rcParams["patch.force_edgecolor"] = True
        weights = np.ones_like(job)/float(len(job)) # sum of bar heights => 1
        n, bins, patches = plt.hist(x=job, bins=[1,2,3,4], facecolor='blue',
                            alpha=1.0, rwidth=0.5, align='left', weights=weights)
        my_xticks = [1,2,3] #x-axis numbering
        plt.xticks(my_xticks)
        plt.grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        plt.xlabel('')
        plt.ylabel('Sum of bar heights = 1',fontsize=14)
        plt.title('Job situation if pain now > 7',fontsize=22)
        plt.text(1.3, 0.3, '1 = full time job \n2 = part time job\n3 = retired or unemployed',
                 fontsize=14)
        maxfreq = n.max()   
        plt.savefig("Job_situation_if_high_pain.png")
        

def relapsed_vs_job(reader, csvfile):
        csvfile.seek(0)
        next(reader)
        job=[]
        for row in reader:
                pain1=row['sufferedpastpain']  
                pain2=row['sufferedpastsciaticapain']
                jobsit = row['jobsituation']
                p1 = float(pain1)
                p2 = float(pain2)
                j = float(jobsit)
                if j > 0:
                        if p1 == 3:
                                job.append(j)
                        else:
                                if p2 == 3:
                                        job.append(j)
        fig7 = plt.figure(7)             
        plt.rcParams["patch.force_edgecolor"] = True
        weights = np.ones_like(job)/float(len(job)) # sum of bar heights => 1
        n, bins, patches = plt.hist(x=job, bins=[1,2,3,4], facecolor='blue',
                            alpha=1.0, rwidth=0.5, align='left', weights=weights)
        my_xticks = [1,2,3] #x-axis numbering
        plt.xticks(my_xticks)       
        plt.grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        plt.xlabel('')
        plt.ylabel('Sum of bar heights = 1',fontsize=14)
        plt.title('Job situation if relapsed pain',fontsize=22)
        plt.text(1.3, 0.3, '1 = full time job \n2 = part time job\n3 = retired or unemployed',
                 fontsize=14)
        maxfreq = n.max()             
        plt.savefig("Job_situation_if_relapsed_pain")

def now_and_past_vs_job(reader, csvfile):
        csvfile.seek(0)
        next(reader)
        job=[]
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
                                        job.append(j)
                                else:
                                        if p2 == 3:
                                                job.append(j)
        fig8 = plt.figure(8)             
        plt.rcParams["patch.force_edgecolor"] = True
        weights = np.ones_like(job)/float(len(job)) # sum of bar heights => 1
        n, bins, patches = plt.hist(x=job, bins=[1,2,3,4], facecolor='blue',
                            alpha=1.0, rwidth=0.5, align='left', weights=weights)
        my_xticks = [1,2,3] #x-axis numbering
        plt.xticks(my_xticks)
        plt.grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        plt.xlabel('')
        plt.ylabel('Sum of bar heights = 1',fontsize=14)
        plt.title('Job situation if pain now and in past',fontsize=22)
        plt.text(1.3, 0.3, '1 = full time job \n2 = part time job\n3 = retired or unemployed',
                 fontsize=14)
        maxfreq = n.max()                         
        plt.savefig("Job_situation_pain_now_and_past")

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
        fig9, axs = plt.subplots(1, 2, sharey=True, figsize=(12,8))
        weights = np.ones_like(mpain)/float(len(mpain)) # sum of bar heights => 1
        N, bins, patches = axs[0].hist(x=sorted(mpain), bins=[-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13], facecolor='blue',
                            alpha=1.0, rwidth=0.6, align='left', weights=weights)
        my_xticks = [0,1,2,3,4,5,6,7,8,9,10,11,12] #x-axis numbering
        plt.setp(axs, xticks = my_xticks, yticks = [0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45])
        axs[0].grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        axs[0].set_title('Males\' pain level at the moment',fontsize=14)
        axs[0].text(2.15, 0.22, '0 = no pain \n12 = maximal pain', fontsize=12)
        axs[0].set_ylabel('Sum of bar heights = 1')

        weights = np.ones_like(fpain)/float(len(fpain)) # sum of bar heights => 1
        N, bins, patches = axs[1].hist(x=sorted(fpain), bins=[-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13], facecolor='red',
                            alpha=1.0, rwidth=0.6, align='left', weights=weights)
        axs[1].grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        axs[1].set_title('Females\' pain level at the moment',fontsize=14)
        axs[1].text(2.15, 0.22, '0 = no pain \n12 = maximal pain', fontsize=12)      
        plt.savefig("Gender_pain_distribution.png")


def gender_vs_relapsed_pain(reader, csvfile):
        csvfile.seek(0)
        next(reader)
        gender = []
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
                                        gender.append(g);
                                else:
                                        gender.append(g);
        
        fig10 = plt.figure(10)
        figure = fig10
        plt.rcParams["patch.force_edgecolor"] = True
        weights = np.ones_like(gender)/float(len(gender)) # sum of bar heights => 1
        n, bins, patches = plt.hist(x=sorted(gender), bins=[1,2,3], facecolor='blue',
                            alpha=0.8, rwidth=0.3, align='left', weights=weights)
        my_xticks = [1,2] #x-axis numbering
        plt.xticks(my_xticks)
        plt.grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        plt.xlabel('')
        plt.ylabel('Sum of bar heights = 1',fontsize=14)
        plt.title('Users with relapsed pain',fontsize=22)
        plt.text(1.2, 0.3, '1 = male \n2 = female',
                 fontsize=14)
        maxfreq = n.max()         
        plt.savefig("Users_with_relapsed_pain.png")
        
# Age distribution whose pain now > 7: 
def highpain_ages(reader, csvfile):
        csvfile.seek(0)
        next(reader)
        d=[]
        for row in reader:
                p = float(row['suffersnowpain'])
                age = float(row['age'])
                if (abs(age) < 130 and abs(age) > 5):
                    if p > 7:
                        d.append(abs(age))


        fig11 = plt.figure(11)
        figure = fig11
        plt.rcParams["patch.force_edgecolor"] = True
        weights = np.ones_like(d)/float(len(d)) # sum of bar heights => 1
        n, bins, patches = plt.hist(x=d, bins=[20,25,30,35,40,45,50,55,60,65,70,75,80],
                                    facecolor='green',alpha=0.9, rwidth=1.0, weights=weights)

        plt.grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        plt.xlabel('Age (years)',fontsize=16)
        plt.ylabel('Sum of bar heights = 1',fontsize=14)
        plt.title('Age distribution if pain now > 7',fontsize=22)
        plt.savefig("High_pain_age_distribution.png")

def users_with_no_pain(reader, csvfile):
        csvfile.seek(0)
        next(reader)
        count = 0
        for row in reader:
                pain1=row['suffersnowpain']
                pain2=row['sufferedpastpain']
                pain3=row['sufferedpastsciaticapain']
                if pain1 == '0' and pain2 == '0' and pain3 == '0':
                        count += 1
        print("Number of users with no pain at all: " + str(count))

def users_with_all_sorts_of_pain(reader, csvfile):
        csvfile.seek(0)
        next(reader)
        count = 0
        for row in reader:
                p1=row['suffersnowpain']
                p2=row['sufferedpastpain']
                p3=row['sufferedpastsciaticapain']
                pain1 = float(p1)
                pain2 = float(p2)
                pain3 = float(p3)
                if pain1 > 0 and pain2 > 0 and pain3 > 0:
                        count += 1
        print("Number of users with all sorts of pain: " + str(count))    

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
        plt.savefig("Gender_job_distribution.png")

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
        plt.savefig("Gender_age_distribution.png")
        


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
        plt.savefig("Gender_job_highpain_distribution.png")

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
        plt.savefig("Educational_distribution.png") 

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
        plt.savefig("Education_vs_highpain_distribution.png") 


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
        plt.savefig("Gender_education_distribution.png")


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
        fig18, axs = plt.subplots(1, 2, sharey=True, figsize=(10,6))
        weights = np.ones_like(mage)/float(len(mage)) # sum of bar heights => 1
        N, bins, patches = axs[0].hist(x=sorted(mage), bins=[20,25,30,35,40,45,50,55,60,65,70,75,80], facecolor='green',
                            alpha=1.0, rwidth=1.0, weights=weights)
        my_xticks = [20,25,30,35,40,45,50,55,60,65,70,75,80] #x-axis numbering
        plt.setp(axs, xticks = my_xticks)#, yticks = [0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45])
        axs[0].grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        axs[0].set_title('Males\' age distribution if pain now > 7',fontsize=14)
        axs[0].set_ylabel('Sum of bar heights = 1')
        axs[0].set_xlabel('Age (years)')


        weights = np.ones_like(fage)/float(len(fage)) # sum of bar heights => 1
        N, bins, patches = axs[1].hist(x=sorted(fage), bins=[20,25,30,35,40,45,50,55,60,65,70,75,80], facecolor='orange',
                            alpha=0.5, rwidth=1.0, weights=weights)
        axs[1].grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        axs[1].set_title('Females\' age distribution if pain now > 7',fontsize=14)
        axs[1].set_ylabel('Sum of bar heights = 1')
        axs[1].set_xlabel('Age (years)')      
        plt.savefig("Gender_age_if_high_pain_distribution.png")

# Print desired distribution (comment out not needed function calls):
def main():
        with open('users.csv') as csvfile:
                reader = csv.DictReader(csvfile)
                
                ages(reader, csvfile)
                jobsit(reader, csvfile)                
                nowpain(reader, csvfile)
                pastpain(reader, csvfile)
                
                gender(reader, csvfile)
                
                corr_matrix(reader, csvfile)
                
                painjob(reader, csvfile)
                relapsed_vs_job(reader, csvfile)
                now_and_past_vs_job(reader, csvfile)
                
                gender_vs_nowpain(reader, csvfile)
                gender_vs_relapsed_pain(reader, csvfile)
                highpain_ages(reader, csvfile)
                
                gender_vs_jobsituation(reader, csvfile)
                gender_vs_age(reader, csvfile)
                gender_vs_jobsituation_if_high_pain_now(reader, csvfile)
                
                education_distribution(reader, csvfile)
                education_vs_highpain(reader, csvfile)
                gender_vs_education(reader, csvfile)
                
                gender_vs_age_if_highpain(reader, csvfile)
        
                #plt.show()

                

if __name__ == '__main__':
    main()

