import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#matplotlib inline

df = pd.read_excel('technical_vocabulary.xlsx', 
   sheet_name = 'vocabulary-1')

# Disease distribution:
fig=plt.figure()
ax=sns.countplot(x='disease_ID', data=df, color='C0')
plt.title('Disease distribution',fontsize=16)
fig.show()

# Symptoms:
fig=plt.figure()
ax=sns.countplot(x='symptom_ID', data=df, color='C0')
plt.title('Symptoms',fontsize=16)
fig.show()

# Therapy:
fig=plt.figure()
ax=sns.countplot(x='therapy_ID', data=df, color='C0')
plt.title('Therapy',fontsize=16)
fig.show()

# life style:
fig=plt.figure()
ax=sns.countplot(x='life style_ID', data=df, color='C0')
plt.title('Life Style',fontsize=16)
fig.show()