import numpy as np
import csv
import matplotlib.pyplot as plt

input_file = csv.DictReader(open('users.csv'))

# Functions for drawing histograms:

# Age distribution:
def ages():
        d1=[]
        fig1 = plt.figure(1)
        for row in input_file:
                age=row['age']
                age=float(age)
                if abs(age) < 130:
                    if abs(age) > 5:
                        d1.append(abs(age))
        #print(min(d),max(d))
        plt.rcParams["patch.force_edgecolor"] = True
        n, bins, patches = plt.hist(x=d1, bins=[20,25,30,35,40,45,50,55,60,65,70,75,80],
                                    facecolor='green',alpha=0.9, rwidth=1.0)
        #plt.grid(axis='x', alpha=0.65, color='black')
        plt.xlabel('Age (years)',fontsize=16)
        plt.ylabel('Frequency',fontsize=14)
        plt.title('Age distribution of the users',fontsize=22)
        #plt.text(23, 45, r'$\mu=15, b=3$')
        maxfreq = n.max()
        fig1.show()
        return

# Job situations:
def jobsit():
        d=[]
        fig2 = plt.figure(2)
        for row in input_file:
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
        fig2.show()   
        return

# Pain at the moment:
def nowpain():
        d=[]
        fig3 = plt.figure(3)
        for row in input_file:
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
        fig3.show()   
        return
                
# Past pain ("normal" + sciatica):
def pastpain():
        d=[]
        fig4 = plt.figure(4)
        for row in input_file:
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
        fig4.show()   
        return        

# Print desired distribution (one by one, comment out the rest of the function calls):
#ages()
#jobsit()
#nowpain()
#pastpain()
