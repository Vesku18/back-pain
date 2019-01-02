"""
NLP project 25:  Mining Citizens’ Health Opinion
"Back-pain"
Team: Juha Mursula, Sakari Murtovaara, Juha Paaso, Riitta Rankinen, Vesa Similä, Aapo Ylisassi
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

tila = {
    "laatikko": None,
}

def load_data():
    nlpprojekti.lemmatize_files()
    nlpprojekti.create_vocabulary()
    nlpprojekti.create_histograms()
    nlpprojekti.create_sentiment_analysis()
    nlpprojekti.compare_documents_with_technical_voc()
    viesti = "Data procressing ready"
    ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"], viesti) 

def term_counts():
    sanasto = {}
    with open('output_dictionary.txt') as sanalista:
        for rivi in sanalista.readlines():
            sana, lkm = rivi.split(",")
            sana.strip()
            lkm.strip()
            if sana != '' and sana != 'None' and sana!='none' and sana !=' ' and sana != ';':
                sanasto[sana]=int(lkm)   
        top15 = dict(sorted(sanasto.items(), key=operator.itemgetter(1),reverse=True) [:30])
    print(top15)

    # plot histogram #    
    names = list(top15.keys())
    values = list(top15.values())
    fig, axs = plt.subplots()
    plt.xticks(rotation=45)
    axs.bar(names, values)
    fig.suptitle('Top words')
    plt.show()

def classed_histo():
    taudit = []
    oireet = []
    hoidot = []
    elintavat = []
    pass

def tech_term_counts(): 
    histograms_tech_vocabulary.Disease()
    histograms_tech_vocabulary.Symptoms()
    histograms_tech_vocabulary.Therapy()
    histograms_tech_vocabulary.life_style()
    plt.show() 

def tee_jotain():
    pass

def age_data():
        with open('users.csv') as csvfile:
                reader = csv.DictReader(csvfile)  
                Statistics_for_UI.ages_and_ages_with_pain(reader, csvfile)
                Statistics_for_UI.gender_vs_age(reader, csvfile)
                Statistics_for_UI.gender_vs_age_if_highpain(reader, csvfile)
                plt.show()
    
def correlation():
        with open('users.csv') as csvfile:
                reader = csv.DictReader(csvfile)  
                Statistics_for_UI.corr_matrix(reader, csvfile)
                
def gender_data():
        with open('users.csv') as csvfile:
                reader = csv.DictReader(csvfile)
                Statistics_for_UI.gender_subplot(reader, csvfile)
                Statistics_for_UI.gender_vs_nowpain(reader, csvfile)
                Statistics_for_UI.gender_vs_age_if_highpain(reader, csvfile)
                plt.show()

def pain_data():
        with open('users.csv') as csvfile:
                reader = csv.DictReader(csvfile)
                Statistics_for_UI.pain(reader, csvfile)
                plt.show()

def job_data():
        with open('users.csv') as csvfile:
                reader = csv.DictReader(csvfile)  
                Statistics_for_UI.job_subplot(reader, csvfile)
                plt.show()

def close_plots():
    plt.close('all')

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
    ikkunasto.luo_nappi(nappikehys, "Categorized histograms", classed_histo)
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
    ikkunasto.luo_nappi(nappikehys, "Quit", ikkunasto.lopeta)
    tila["laatikko"] = ikkunasto.luo_tekstilaatikko(nappikehys, 20, 20)
    viesti = "Load and process data first.\nNotice that data processing takes a minute"
    ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"], viesti) 
    ikkunasto.kaynnista()


if __name__ == "__main__":
    main()