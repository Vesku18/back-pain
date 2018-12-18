import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#matplotlib inline

df = pd.read_excel('technical_vocabulary_v6.xlsx', 
   sheet_name = 'vocabulary-1')

# Disease distribution:
ax=sns.countplot(x='disease_ID', data=df, color='C0')
plt.title('Disease distribution',fontsize=16)
#plt.ylabel('Number of Disease',fontsize=14)

# Symptoms:
ax=sns.countplot(x='symptom_ID', data=df, color='C0')
plt.title('Symptoms',fontsize=16)
#plt.ylabel('Number of Symptoms',fontsize=14)

# Therapy:
ax=sns.countplot(x='therapy_ID', data=df, color='C0')
plt.title('Therapy',fontsize=16)
#plt.ylabel('Number of Therapies',fontsize=14)

# life style:
ax=sns.countplot(x='life style_ID', data=df, color='C0')
plt.title('Life Style',fontsize=16)
#plt.ylabel('Number of Life Styles',fontsize=14)