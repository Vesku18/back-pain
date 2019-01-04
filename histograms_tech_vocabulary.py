import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#matplotlib inline

#def hist():
df = pd.read_excel('technical_vocabulary.xlsx', sheet_name = 'vocabulary-1')

def Disease():
    fig = plt.figure()
    ay=sns.countplot(y='disease_class', data=df, color='C0', order = df['disease_class'].value_counts().index)
    ay.set_ylabel('')
    ay.set_xlabel('Count by classes', fontsize=12)    
    plt.yticks(y='disease_class', fontsize=12)
    plt.title('Disease distribution', fontsize=14)
    plt.savefig("Disease_distribution.png")

def Symptoms():
    fig = plt.figure()
    ay=sns.countplot(y='symptom_class', data=df, color='C0', order = df['symptom_class'].value_counts().index)
    ay.set_ylabel('')
    ay.set_xlabel('Count by classes', fontsize=12)
    plt.yticks(y='symptom_class', fontsize=12)
    plt.title('Symptoms', fontsize=14) 
    plt.savefig("Symptoms_count.png")

def Therapy():
    fig = plt.figure()
    ay=sns.countplot(y='therapy_class', data=df, color='C0', order = df['therapy_class'].value_counts().index)
    ay.set_ylabel('')
    ay.set_xlabel('Count by classes', fontsize=12)
    plt.yticks(y='therapy_class', fontsize=12)    
    plt.title('Therapy', fontsize=14)    
    plt.savefig("Therapy_count.png")

def life_style():
    fig = plt.figure()
    ay=sns.countplot(y='life style_class', data=df, color='C0', order = df['life style_class'].value_counts().index)
    ay.set_ylabel('')
    ay.set_xlabel('Count by classes', fontsize=12)    
    plt.yticks(y='life_style_class', fontsize=12)   
    plt.title('Life Style', fontsize=14) 
    plt.savefig("Life_Style_count.png")