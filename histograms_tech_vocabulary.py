import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#matplotlib inline

#def hist():
df = pd.read_excel('technical_vocabulary.xlsx', sheet_name = 'vocabulary-1')


def Disease():
    fig = plt.figure()
    ax=sns.countplot(x='disease_class', data=df, color='C0')
    plt.xticks(x='disease_class', rotation='vertical')
    plt.title('Disease distribution',fontsize=16)
    plt.savefig("Disease_distribution.png")

def  Symptoms():
    fig = plt.figure()
    ax=sns.countplot(x='symptom_class', data=df, color='C0')
    plt.xticks(x='symptom_class', rotation='vertical')
    plt.title('Symptoms',fontsize=16)
    plt.savefig("Symptoms_count.png")

def Therapy():
    fig = plt.figure()
    ax=sns.countplot(x='therapy_class', data=df, color='C0')
    plt.xticks(x='therapy_class', rotation='vertical')
    plt.title('Therapy',fontsize=16)
    plt.savefig("Therapy_count.png")

def life_style():
    fig = plt.figure()
    ax=sns.countplot(x='life style_class', data=df, color='C0')
    plt.xticks(x='life style_class', rotation='vertical')
    plt.title('Life Style',fontsize=16)
    plt.savefig("Life_Style_count.png")