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
    ay.set_xlabel('Count by classes')
    plt.title('Disease distribution')
    plt.savefig("Disease_distribution.png")

def Symptoms():
    fig = plt.figure()
    ay=sns.countplot(y='symptom_class', data=df, color='C0', order = df['symptom_class'].value_counts().index)
    plt.title('Symptoms') 
    ay.set_ylabel('')
    ay.set_xlabel('Count by classes')
    plt.savefig("Symptoms_count.png")

def Therapy():
    fig = plt.figure()
    ay=sns.countplot(y='therapy_class', data=df, color='C0', order = df['therapy_class'].value_counts().index)
    plt.title('Therapy')    
    ay.set_ylabel('')
    ay.set_xlabel('Count by classes')
    plt.savefig("Therapy_count.png")

def life_style():
    fig = plt.figure()
    ay=sns.countplot(y='life style_class', data=df, color='C0', order = df['life style_class'].value_counts().index)
    plt.xticks(x='life_style_class', rotation='vertical')
    plt.title('Life Style')
    ay.set_ylabel('')
    ay.set_xlabel('Count by classes')
    plt.savefig("Life_Style_count.png")