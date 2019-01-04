"""
NLP project 25:  Mining Citizens’ Health Opinion
"Back-pain"
Team: Juha Mursula, Sakari Murtovaara, Juha Paaso, Riitta Rankinen, Vesa Similä, Aapo Ylisassi
Date: 7. 1. 2019
"""

import ikkunasto
import nlpprojekti
import csv
import operator
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
import pandas as pd
import seaborn as sns
import Statistics_for_UI
import histograms_tech_vocabulary
import os
from tkinter import *
from pandastable import Table, TableModel
import xlrd

tila = {
    "laatikko": None,
    "prosessoitu": False,
}

def load_data():
    """
    Load and process data
    """
#    nlpprojekti.lemmatize_files()
    nlpprojekti.create_vocabulary()
    nlpprojekti.create_histograms()
    nlpprojekti.create_sentiment_analysis()
    nlpprojekti.compare_documents_with_technical_voc()
    viesti = "Data processing done."
    ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"], viesti) 
    tila["prosessoitu"] = True

def term_counts():
    """ 
    Histogram of all words in users.csv and solutions.csv, stopwords removed
    Histograms by categories, words defined in technical_vocabulary.xsls
    - disease, symptom, therapy, life style   
    """
    sanasto = {}
    taudit = []
    oireet = []
    hoidot = []
    tavat = []

    if tila["prosessoitu"] == True:
        with open('output_dictionary.txt') as sanalista:
            for rivi in sanalista.readlines():
                sana, lkm = rivi.split(",")
                sana.strip()
                lkm.strip()
                if sana != '' and sana != 'None' and sana!='none' and sana !=' ' and sana != ';':
                    sanasto[sana]=int(lkm)   
            top_sanat = dict(sorted(sanasto.items(), key=operator.itemgetter(1),reverse=True) [:20])
        print("\nTop terms in user documents")
        print(top_sanat)

        workbook = xlrd.open_workbook("technical_vocabulary.xlsx")
        sheet = workbook.sheet_by_index(0)
        for rowx in range(sheet.nrows):
            cols = sheet.row_values(rowx)
            tauti = str(cols[0]).strip()
            if tauti != '':
                taudit.append(tauti)
            oire = str(cols[3]).strip()
            if oire != '':
                oireet.append(oire)
            hoito = str(cols[6]).strip()
            if hoito != '':
                hoidot.append(hoito)
            tapa = str(cols[9]).strip()
            if tapa != '':
                tavat.append(tapa)

        tauti_histo = {}
        for sana in sanasto:
            for tauti in taudit:
                if sana == tauti:
                    tauti_histo[sana] = sanasto[sana]
        print("\nTop diseases:")
        print(tauti_histo)
        top_taudit = dict(sorted(tauti_histo.items(), key=operator.itemgetter(1),reverse=True) [:10])

        oire_histo = {}
        for sana in sanasto:
            for oire in oireet:
                if sana == oire:
                    oire_histo[sana] = sanasto[sana]
        print("\nTop symptoms:")
        print(oire_histo)
        top_oireet = dict(sorted(oire_histo.items(), key=operator.itemgetter(1),reverse=True) [:10])

        hoito_histo = {}
        for sana in sanasto:
            for hoito in hoidot:
                if sana == hoito:
                    hoito_histo[sana] = sanasto[sana]
        print("\nTop therapies:")
        print(hoito_histo)
        top_hoidot = dict(sorted(hoito_histo.items(), key=operator.itemgetter(1),reverse=True) [:10])

        tapa_histo = {}
        for sana in sanasto:
            for tapa in tavat:
                if sana == tapa:
                    tapa_histo[sana] = sanasto[sana]
        print("\nTop life styles:")
        print(tapa_histo)
        top_tavat = dict(sorted(tapa_histo.items(), key=operator.itemgetter(1),reverse=True) [:10])

        # histogram: all terms
        names = list(top_sanat.keys())
        values = list(top_sanat.values())
        fig1, axs = plt.subplots(figsize=(8,6))
        axs.barh(names, values)
        fig1.suptitle('Top terms')
        axs.invert_yaxis()

        # histograms: disease, symptoms, therapies, life style
 
        fig2, axes = plt.subplots(nrows=2,ncols=2, figsize=(8,6))
        ax0, ax1, ax2, ax3 = axes.flatten()

        names = list(top_taudit.keys())
        values = list(top_taudit.values())
        ax0.barh(names, values)
        ax0.set_title("Top diseases")
        ax0.invert_yaxis()

        names = list(top_oireet.keys())
        values = list(top_oireet.values())
        ax1.barh(names, values)
        ax1.set_title('Top symptoms')
        ax1.invert_yaxis()

        names = list(top_hoidot.keys())
        values = list(top_hoidot.values())
        ax2.barh(names, values)
        ax2.set_title('Top therapies')
        ax2.invert_yaxis()

        names = list(top_tavat.keys())
        values = list(top_tavat.values())
        ax3.barh(names, values)
        ax3.set_title('Top life styles')
        ax3.invert_yaxis()

        fig2.tight_layout()
        plt.show()

    else:
        viesti = "Process data first!"
        ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"], viesti)

def tech_term_counts(): 
    """
    Histograms of technical vocabulary
    """
    if tila["prosessoitu"] == True:
        histograms_tech_vocabulary.Disease()
        histograms_tech_vocabulary.Symptoms()
        histograms_tech_vocabulary.Therapy()
        histograms_tech_vocabulary.life_style()
        plt.show() 
    else:
        viesti = "Process data first!"
        ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"], viesti)

def sentiment_pie_solutions():
    """
    Pie chart for "solutions.csv", where the slices will be ordered and plotted
    """
    if tila["prosessoitu"] == True:
        with open("output_sentiment_of_solutions.csv") as csvfile:
            reader = csv.DictReader(csvfile, ['Sentiment', 'Count'])
            print()
            print(' Plotting solutions.csv sentiment: ')
            for row in reader:
                print('   ', row['Sentiment'], 'sentiment documents count', row['Count'])
                if row['Sentiment'] == 'Positive':
                    senti_document_pos = str(row['Count'])
                if row['Sentiment'] == 'Negative':
                    senti_document_neg = str(row['Count'])
                else:
                    senti_document_neut = str(row['Count'])
        labels = ['Positive documents', 'Negative documents', 'Neutral documents']
        sizes = [senti_document_pos, senti_document_neg, senti_document_neut]
        colors =['lightgreen', 'red', 'lightgrey']
        explode = [0.1, 0.1, 0]
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', colors=colors, shadow=False, startangle=90)
        ax1.set_title('solutions.csv', fontsize=14)
        plt.tight_layout()
        plt.show()
    else:
        viesti = "Process data first!"
        ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"], viesti)

def sentiment_pie_users():
    """
    Pie chart for "users.csv", where the slices will be ordered and plotted
    """
    if tila["prosessoitu"] == True:
        with open("output_sentiment_of_users.csv") as csvfile:
            reader = csv.DictReader(csvfile, ['Sentiment', 'Count'])
            print()
            print(' Plotting users.csv sentiment: ')
            for row in reader:
                print('   ', row['Sentiment'], 'sentiment documents count', row['Count'])
                if row['Sentiment'] == 'Positive':
                    senti_document_pos = str(row['Count'])
                if row['Sentiment'] == 'Negative':
                    senti_document_neg = str(row['Count'])
                else:
                    senti_document_neut = str(row['Count'])
        labels = ['Positive documents', 'Negative documents', 'Neutral documents']
        sizes = [senti_document_pos, senti_document_neg, senti_document_neut]
        colors =['lightgreen', 'red', 'lightgrey']
        explode = [0.1, 0.1, 0]
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', colors=colors, shadow=False, startangle=90)
        ax1.set_title('users.csv', fontsize=14)
        plt.tight_layout()
        plt.show()
    else:
        viesti = "Process data first!"
        ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"], viesti)
    pass

def document_overlapping(): # TÄSTÄ löhtee
    #        import matplotlib
    #        import matplotlib.pyplot as plt
    #        import numpy as np

    words = []
    common_words = []
    if tila["prosessoitu"] == True:
        with open("output_document_commonality.csv") as csvfile:
            reader = csv.DictReader(csvfile, ['Id', 'Number of words', 'Number of common words with other documents'])
            for row in reader:
                words.append(row['Number of words'])
                common_words.append(row['Number of common words with other documents'])

        # Data for plotting
        t = np.arange(0, len(words), 1)
        s = words

        fig, ax = plt.subplots()
        ax.plot(t, words, 'b')
        ax.plot(t, common_words, 'k')
        ax.set(xlabel='Documents', ylabel='Number of words',
               title='Common words in documents, sorted by number of common words')
        ax.grid()

        fig.savefig("test.png")
        plt.show()

    else:
        viesti = "Process data first!"
        ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"], viesti)
    pass

def age_data():
    """
    Statistics of age data
    """
    if tila["prosessoitu"] == True:
        with open('users.csv') as csvfile:
                reader = csv.DictReader(csvfile)  
                Statistics_for_UI.ages_and_ages_with_pain(reader, csvfile)
                Statistics_for_UI.gender_vs_age(reader, csvfile)
                Statistics_for_UI.gender_vs_age_if_highpain(reader, csvfile)
                plt.show()
    else:
        viesti = "Process data first!"
        ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"], viesti)        
    
def correlation():
    """
    Calculating correlations of user data
    """
    if tila["prosessoitu"] == True:   
        with open('users.csv') as csvfile:
                reader = csv.DictReader(csvfile)  
                Statistics_for_UI.corr_matrix(reader, csvfile)
    else:
        viesti = "Process data first!"
        ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"], viesti)                   

def gender_data():
    """
    Statistics of gender data
    """
    if tila["prosessoitu"] == True:
        with open('users.csv') as csvfile:
                reader = csv.DictReader(csvfile)
                Statistics_for_UI.gender_subplot(reader, csvfile)
                Statistics_for_UI.gender_vs_nowpain(reader, csvfile)
                Statistics_for_UI.gender_vs_age_if_highpain(reader, csvfile)
                plt.show()
    else:
        viesti = "Process data first!"
        ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"], viesti)    

def pain_data():
    """
    Statistics of pain data
    """
    if tila["prosessoitu"] == True:
        with open('users.csv') as csvfile:
                reader = csv.DictReader(csvfile)
                Statistics_for_UI.pain(reader, csvfile)
                plt.show()
    else:
        viesti = "Process data first!"
        ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"], viesti)  
 
def job_data():
    """
    Statistics of job situation
    """
    if tila["prosessoitu"] == True:
        with open('users.csv') as csvfile:
                reader = csv.DictReader(csvfile)  
                Statistics_for_UI.job_subplot(reader, csvfile)
                plt.show()
    else:
        viesti = "Process data first!"
        ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"], viesti)   

def close_plots():
    """
    Closing all plots
    """
    if tila["prosessoitu"] == True:
        plt.close('all')
    else:
        viesti = "Process data first!"
        ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"], viesti)  

def quit_program():
    """
    Exiting program
    """
    close_plots()
    ikkunasto.lopeta()
 
def tee_jotain():
    """ poistetaan kunhan kaikki käsittelijäfunktiot on valmiita"""
    pass

def main():
    """
    Create GUI
    """
    ikkuna = ikkunasto.luo_ikkuna("Back-pain")
    nappikehys = ikkunasto.luo_kehys(ikkuna) 
    ikkunasto.luo_tekstirivi(nappikehys, "Data processing")
    ikkunasto.luo_nappi(nappikehys, "Load and process data", load_data)
    ikkunasto.luo_tekstirivi(nappikehys, "Word counts")
    ikkunasto.luo_nappi(nappikehys, "Term counts", term_counts)
    ikkunasto.luo_nappi(nappikehys, "Document overlapping", document_overlapping)
    ikkunasto.luo_nappi(nappikehys, "Technical term counts", tech_term_counts)
    ikkunasto.luo_tekstirivi(nappikehys, "Sentiment analysis")
    ikkunasto.luo_nappi(nappikehys, "for Document solutions", sentiment_pie_solutions)
    ikkunasto.luo_nappi(nappikehys, "for Documnet users", sentiment_pie_users)
    ikkunasto.luo_tekstirivi(nappikehys, "Term-document matrix")
    ikkunasto.luo_nappi(nappikehys, "TDM1", tee_jotain)
    ikkunasto.luo_nappi(nappikehys, "TDM2", tee_jotain)
    ikkunasto.luo_tekstirivi(nappikehys, "Statistics")
    ikkunasto.luo_nappi(nappikehys, "Correlations", correlation)
    ikkunasto.luo_nappi(nappikehys, "Pain", pain_data)
    ikkunasto.luo_nappi(nappikehys, "Age", age_data)
    ikkunasto.luo_nappi(nappikehys, "Gender", gender_data)
    ikkunasto.luo_nappi(nappikehys, "Job", job_data)
    ikkunasto.luo_tekstirivi(nappikehys, " ")
    ikkunasto.luo_nappi(nappikehys, "Close plots", close_plots)
    ikkunasto.luo_nappi(nappikehys, "Quit", quit_program)
    tila["laatikko"] = ikkunasto.luo_tekstilaatikko(nappikehys, 30, 15)
    viesti = "Source files:\n users.csv, solutions.csv\nLoad and process data first.\nNotice that data processing\ntakes a minute."
    ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"], viesti) 
    ikkunasto.kaynnista()


if __name__ == "__main__":
    main()