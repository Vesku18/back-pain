import numpy as np
import csv
import matplotlib.pyplot as plt
import matplotlib.colors
import pandas as pd


# Age distribution:
def ages(reader, csvfile):
        d=[]
        fig1 = plt.figure(1)
        csvfile.seek(0)
        next(reader)
        for row in reader:
                age=row['age']
                age=float(age)
                if abs(age) < 130:
                    if abs(age) > 5:
                        d.append(abs(age))
        #print(min(d),max(d))
        plt.rcParams["patch.force_edgecolor"] = True
        n, bins, patches = plt.hist(x=d, bins=[20,25,30,35,40,45,50,55,60,65,70,75,80],
                                    facecolor='green',alpha=0.9, rwidth=1.0)
        #plt.grid(axis='x', alpha=0.65, color='black')
        plt.xlabel('Age (years)',fontsize=16)
        plt.ylabel('Frequency',fontsize=14)
        plt.title('Age distribution of the users',fontsize=22)
        #plt.text(23, 45, r'$\mu=15, b=3$')
        maxfreq = n.max()
        # Set a clean upper y-axis limit.
        #plt.ylim(top=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10


# Job situations:
def jobsit(reader, csvfile):
        d=[]
        fig2 = plt.figure(2)
        csvfile.seek(0)
        next(reader)
        for row in reader:
                job=row['jobsituation']
                if not job == '-1':
                        d.append(job)                
        plt.rcParams["patch.force_edgecolor"] = True
        n, bins, patches = plt.hist(x=d, bins=[0,1,2,3], facecolor='blue',
                            alpha=1.0, rwidth=0.5, align='left')
        #plt.grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        plt.xlabel('')
        plt.ylabel('Frequency',fontsize=14)
        plt.title('Job situation of the users',fontsize=22)
        plt.text(0.75, 175, '1 = full time job \n2 = part time job\n3 = retired or unemployed',
                 fontsize=14)
        maxfreq = n.max()  

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
        n, bins, patches = plt.hist(x=sorted(d), bins=[-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13], facecolor='red',
                            alpha=1.0, rwidth=0.6, align='left')
        my_xticks = [0,1,2,3,4,5,6,7,8,9,10,11,12] #x-axis numbering
        plt.xticks(my_xticks)
        #plt.grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        plt.xlabel('')
        plt.ylabel('Frequency')
        plt.title('Users\' pain level at the moment',fontsize=22)
        plt.text(4.35, 100, '0 = no pain \n12 = maximal pain', fontsize=14)
        maxfreq = n.max()  

                
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
        n, bins, patches = plt.hist(x=sorted(d), bins=[0,1,2,3,4], facecolor='yellow',
                            alpha=1.0, rwidth=0.6, align='left')
        my_xticks = [0,1,2,3] #x-axis numbering
        plt.xticks(my_xticks)
        #plt.grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        plt.xlabel('')
        plt.ylabel('Frequency')
        plt.title('Users\' pain experience in the past',fontsize=22)
        plt.text(0.45, 300, '0 = no \n1 = yes \n2 = not relapsed \n3 = relapsed',fontsize=14)
        maxfreq = n.max()
         

# Gender distribution:
def gender(reader, csvfile):
        d=[]
        csvfile.seek(0)
        next(reader)
        fig5 = plt.figure(5)
        for row in reader:
                gend=row['gender']
                if not gend == '-1':
                        d.append(gend)
        #print(d)
        plt.rcParams["patch.force_edgecolor"] = True
        n, bins, patches = plt.hist(x=d, bins=[0,1,2,3], facecolor='blue',
                            alpha=0.6, rwidth=0.4, align='left')
        #plt.grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        plt.xlabel('')
        plt.ylabel('Frequency',fontsize=14)
        plt.title('Gender distribution of the users',fontsize=22)
        plt.text(1.55, 175, '1 = male \n2 = female', fontsize=14)
        maxfreq = n.max()
          

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
        print(len(d1),len(d2),len(d3),len(d4),len(d5),len(d6),len(d7),len(d8),len(d9))
        df = pd.DataFrame({'age': d1})
        df['jobsit.'] = d2
        df['gender'] = d3
        df['pastpain']= d4
        df['pastsciaticap.'] = d5
        df['nowpain'] = d6                                          
        df['howactive'] = d7
        df['surgerydone'] = d8
        df['education'] = d9

        dfcor = df.corr()
        dfcor_final = dfcor.round(3) # Taking 3 decimals to results
        dfcor_final.to_csv('corr_matrix.csv', sep=',', encoding='utf-8')

        with pd.option_context('display.max_rows', None, 'display.max_columns', None):
                print(dfcor_final)
                

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
                if (p > 7):
                        highpain.append(p)
                        job.append(j)
        '''
        print(len(job))                        
        df = pd.DataFrame({'highpain': highpain})
        df['jobsit.'] = job
        print(df.corr())
        '''
        #print(job)
        fig6 = plt.figure(6)             
        plt.rcParams["patch.force_edgecolor"] = True
        n, bins, patches = plt.hist(x=job, bins=[1,2,3,4], facecolor='blue',
                            alpha=1.0, rwidth=0.5, align='left')
        #plt.grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        plt.xlabel('')
        plt.ylabel('Frequency',fontsize=14)
        plt.title('Job situation if pain now > 7',fontsize=22)
        plt.text(1.3, 35, '1 = full time job \n2 = part time job\n3 = retired or unemployed',
                 fontsize=14)
        maxfreq = n.max()   


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
                if p1 == 3:
                        job.append(j)
                else:
                        if p2 == 3:
                                job.append(j)
        fig7 = plt.figure(7)             
        plt.rcParams["patch.force_edgecolor"] = True
        n, bins, patches = plt.hist(x=job, bins=[1,2,3,4], facecolor='blue',
                            alpha=1.0, rwidth=0.5, align='left')
        #plt.grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        plt.xlabel('')
        plt.ylabel('Frequency',fontsize=14)
        plt.title('Job situation if relapsed pain',fontsize=22)
        plt.text(1.3, 100, '1 = full time job \n2 = part time job\n3 = retired or unemployed',
                 fontsize=14)
        maxfreq = n.max()             


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
                if (p > 6):
                        if p1 == 3:
                                job.append(j)
                        else:
                                if p2 == 3:
                                        job.append(j)
        fig8 = plt.figure(8)             
        plt.rcParams["patch.force_edgecolor"] = True
        n, bins, patches = plt.hist(x=job, bins=[1,2,3,4], facecolor='blue',
                            alpha=1.0, rwidth=0.5, align='left')
        #plt.grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        plt.xlabel('')
        plt.ylabel('Frequency',fontsize=14)
        plt.title('Job situation if pain now and in past',fontsize=22)
        plt.text(1.3, 38, '1 = full time job \n2 = part time job\n3 = retired or unemployed',
                 fontsize=14)
        maxfreq = n.max()                         


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
        #print(len(mpain))
        #print(len(fpain))
        plt.rcParams["patch.force_edgecolor"] = True
        fig9, axs = plt.subplots(1, 2, sharey=True)
        N, bins, patches = axs[0].hist(x=sorted(mpain), bins=[-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13], facecolor='blue',
                            alpha=1.0, rwidth=0.6, align='left')
        axs[0].set_title('Males\' pain level at the moment',fontsize=14)
        axs[0].text(2.15, 70, '0 = no pain \n12 = maximal pain', fontsize=12)
        axs[0].set_ylabel('Number of users')

        N, bins, patches = axs[1].hist(x=sorted(fpain), bins=[-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13], facecolor='red',
                            alpha=1.0, rwidth=0.6, align='left')
        axs[1].set_title('Females\' pain level at the moment',fontsize=14)
        axs[1].text(2.15, 70, '0 = no pain \n12 = maximal pain', fontsize=12)      


def gender_vs_relapsed_pain(reader, csvfile):
        csvfile.seek(0)
        next(reader)
        gender = []
        for row in reader:
                pain1=row['sufferedpastpain']  
                pain2=row['sufferedpastsciaticapain']
                g=row['gender']
                p1 = float(pain1)
                p2 = float(pain2)
                if not (p1 == -1 and p2 == -1):
                        if p1 == 3 or p2 == 3:
                                if g=='1' and not (g=='-1' or g=='3'):
                                        gender.append(g);
                                else:
                                        gender.append(g);
        #print(len(gender))
        fig10 = plt.figure(10)
        figure = fig10
        plt.rcParams["patch.force_edgecolor"] = True
        n, bins, patches = plt.hist(x=sorted(gender), bins=[0,1,2,3], facecolor='blue',
                            alpha=0.6, rwidth=0.4, align='left')
        #plt.grid(axis='y', alpha=0.75, color='grey',linestyle='dashed')
        plt.xlabel('')
        plt.ylabel('Number of users',fontsize=14)
        plt.title('Users with relapsed pain',fontsize=22)
        plt.text(1.4, 180, '1 = male \n2 = female',
                 fontsize=14)
        maxfreq = n.max()         

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

        #print(len(d))
        fig11 = plt.figure(11)
        figure = fig11
        plt.rcParams["patch.force_edgecolor"] = True
        n, bins, patches = plt.hist(x=d, bins=[20,25,30,35,40,45,50,55,60,65,70,75,80],
                                    facecolor='green',alpha=0.9, rwidth=1.0)
        #plt.grid(axis='x', alpha=0.65, color='black')
        plt.xlabel('Age (years)',fontsize=16)
        plt.ylabel('Frequency',fontsize=14)
        plt.title('Age distribution if pain now > 7',fontsize=22)
        #plt.text(23, 45, r'$\mu=15, b=3$')
        maxfreq = n.max()

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
                
                plt.show()

if __name__ == '__main__':
    main()

