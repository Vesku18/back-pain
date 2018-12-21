"""
NLP project 25
Back-pain
tiimi: NN, NN, NN
päiväys
"""

import ikkunasto

tila = {
    "laatikko": None,
}

def load_data():
    """
    seli seli
    """
    #koodia
    pass

def term_counts():
    """
    seli seli
    """
    # koodia
    pass

def tee_jotain():
    """
    seli seli
    """
    # koodia
    pass

def main():
    """
    Luodaan käyttöliittymäikkuna. Vasemmalla puolella on napit, Oikealla puolella on tulostukset.
    Tai sitten tulostukset omiin pop-up-ikkunoihin. Tekstiruutuun voi tulostaa ohjeta yms.
    """
    ikkuna = ikkunasto.luo_ikkuna("Back-pain")
    nappikehys = ikkunasto.luo_kehys(ikkuna) 
    ikkunasto.luo_tekstirivi(nappikehys, "Load data")
    ikkunasto.luo_nappi(nappikehys, "Load data", load_data)
    ikkunasto.luo_tekstirivi(nappikehys, "Word counts")
    ikkunasto.luo_nappi(nappikehys, "Term counts", term_counts)
    ikkunasto.luo_nappi(nappikehys, "Document overlap", tee_jotain)
    ikkunasto.luo_tekstirivi(nappikehys, "Sentiment analysis")
    ikkunasto.luo_nappi(nappikehys, "SA1", tee_jotain)
    ikkunasto.luo_nappi(nappikehys, "SA2", tee_jotain)
    ikkunasto.luo_tekstirivi(nappikehys, "Term-document matrix")
    ikkunasto.luo_nappi(nappikehys, "TDM1", tee_jotain)
    ikkunasto.luo_nappi(nappikehys, "TDM2", tee_jotain)
    ikkunasto.luo_tekstirivi(nappikehys, "Statistics")
    ikkunasto.luo_nappi(nappikehys, "Stat1", tee_jotain)
    ikkunasto.luo_nappi(nappikehys, "Stat2", tee_jotain)
    ikkunasto.luo_tekstirivi(nappikehys, "    ")
    ikkunasto.luo_nappi(nappikehys, "Quit", ikkunasto.lopeta)
    tila["laatikko"] = ikkunasto.luo_tekstilaatikko(nappikehys, 20, 20)
    viesti = "Tähän voi kirjoitaa ohjeita tai muuta dataa"
    ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"], viesti) 
    ikkunasto.kaynnista()


if __name__ == "__main__":
    main()