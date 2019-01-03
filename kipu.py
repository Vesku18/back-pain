"""
NLP project 25:  Mining Citizens’ Health Opinion
"Back-pain"
Team: Juha Mursula, Sakari Murtovaara, Juha Paaso, Riitta Rankinen, Vesa Similä, Aapo Ylisassi
Date: xx. xx 2019
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
    nlpprojekti.lemmatize_files()
    nlpprojekti.create_vocabulary()
    nlpprojekti.create_histograms()
    nlpprojekti.create_sentiment_analysis()
    nlpprojekti.compare_documents_with_technical_voc()
    viesti = "Data processing ready."
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
        print(tauti_histo)
        top_taudit = dict(sorted(tauti_histo.items(), key=operator.itemgetter(1),reverse=True) [:10])

        oire_histo = {}
        for sana in sanasto:
            for oire in oireet:
                if sana == oire:
                    oire_histo[sana] = sanasto[sana]
        print(oire_histo)
        top_oireet = dict(sorted(oire_histo.items(), key=operator.itemgetter(1),reverse=True) [:10])

        hoito_histo = {}
        for sana in sanasto:
            for hoito in hoidot:
                if sana == hoito:
                    hoito_histo[sana] = sanasto[sana]
        print(hoito_histo)
        top_hoidot = dict(sorted(hoito_histo.items(), key=operator.itemgetter(1),reverse=True) [:10])

        tapa_histo = {}
        for sana in sanasto:
            for tapa in tavat:
                if sana == tapa:
                    tapa_histo[sana] = sanasto[sana]
        print(tapa_histo)
        top_tavat = dict(sorted(tapa_histo.items(), key=operator.itemgetter(1),reverse=True) [:10])

        # histogram: all words   
        names = list(top_sanat.keys())
        values = list(top_sanat.values())
        fig, axs = plt.subplots()
        plt.xticks(rotation=75)
        axs.bar(names, values)
        fig.suptitle('Top words')

        # histogram: diseases
        names = list(top_taudit.keys())
        values = list(top_taudit.values())
        fig, axs = plt.subplots()
        plt.xticks(rotation=75)
        axs.bar(names, values)
        fig.suptitle('Top diseases')

        # histogram: symptoms
        names = list(top_oireet.keys())
        values = list(top_oireet.values())
        fig, axs = plt.subplots()
        plt.xticks(rotation=75)
        axs.bar(names, values)
        fig.suptitle('Top symptoms')

        # histogram: therapy
        names = list(top_hoidot.keys())
        values = list(top_hoidot.values())
        fig, axs = plt.subplots()
        plt.xticks(rotation=75)
        axs.bar(names, values)
        fig.suptitle('Top therapies')

       # histogram: life styles
        names = list(top_tavat.keys())
        values = list(top_tavat.values())
        fig, axs = plt.subplots()
        plt.xticks(rotation=75)
        axs.bar(names, values)
        fig.suptitle('Top life styles')

        plt.show()

    else:
        viesti = "Process data first!"
        ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"], viesti)

def tech_term_counts(): 
    if tila["prosessoitu"] == True:
        histograms_tech_vocabulary.Disease()
        histograms_tech_vocabulary.Symptoms()
        histograms_tech_vocabulary.Therapy()
        histograms_tech_vocabulary.life_style()
        plt.show() 
    else:
        viesti = "Process data first!"
        ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"], viesti)

def tee_jotain():
    pass

def age_data():
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
    if tila["prosessoitu"] == True:   
        with open('users.csv') as csvfile:
                reader = csv.DictReader(csvfile)  
                Statistics_for_UI.corr_matrix(reader, csvfile)
    else:
        viesti = "Process data first!"
        ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"], viesti)                   

def gender_data():
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
    if tila["prosessoitu"] == True:
        with open('users.csv') as csvfile:
                reader = csv.DictReader(csvfile)
                Statistics_for_UI.pain(reader, csvfile)
                plt.show()
    else:
        viesti = "Process data first!"
        ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"], viesti)  
 
def job_data():
    if tila["prosessoitu"] == True:
        with open('users.csv') as csvfile:
                reader = csv.DictReader(csvfile)  
                Statistics_for_UI.job_subplot(reader, csvfile)
                plt.show()
    else:
        viesti = "Process data first!"
        ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"], viesti)   

def close_plots():
    if tila["prosessoitu"] == True:
        plt.close('all')
    else:
        viesti = "Process data first!"
        ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"], viesti)  

def quit_program():
    close_plots()
    ikkunasto.lopeta()
 
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
    ikkunasto.luo_nappi(nappikehys, "Document overlapping", tee_jotain)
    ikkunasto.luo_nappi(nappikehys, "Tech term counts", tech_term_counts)
    ikkunasto.luo_tekstirivi(nappikehys, "Sentiment analysis")
    ikkunasto.luo_nappi(nappikehys, "SA1", tee_jotain)
    ikkunasto.luo_nappi(nappikehys, "SA2", tee_jotain)
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
    viesti = "Load and process data first.\nNotice that data processing\ntakes a minute."
    ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"], viesti) 
    ikkunasto.kaynnista()


if __name__ == "__main__":
    main()
