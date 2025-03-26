import numpy as np
import pandas as pd
from scipy.stats import pearsonr, spearmanr
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from pandas import read_csv
from pandas.plotting import scatter_matrix

try:
    fichier = "BeansDataSet.csv"
    col = ['Channel', 'Region', 'Robusta', 'Arabica', 'Espresso', 'Lungo', 'Latte', 'Cappuccino']
    article = [f'article_{i}' for i in range(1, 439)]  
    data = read_csv(fichier, names=col)
    data.index = article
    pd.set_option('display.width', 100)
    pd.set_option('display.float_format', '{:.2f}'.format)
except:
    st.markdown("<h1 style='text-align: center;'>Beans&Pods</h1>", unsafe_allow_html=True)

#--------Menu barre lateral
st.sidebar.markdown("<h1 style='color: white;'>Analyse de données BeansDataSet</h1>", unsafe_allow_html=True)
menu = st.sidebar.selectbox("Navigation", ["Peek at the date", "Statisques descriptives", "Compte rendu"])

if menu == "Peek at the date":
    st.subheader("Description des données :")
    st.write(data)
    st.subheader("Affichage des 5 premiers :")
    peek = data.head(5)    
    st.write(peek)
    st.subheader("Affichage des 5 derniers :")
    peek = data.tail(5)
    st.write(peek)
    st.subheader("Dimension des données :")
    st.write(data.shape)
    st.write(data.shape[0])
    st.write(data.shape[0])
    st.subheader("Absence des valeurs :")
    x = data.isnull()
    st.write(x)
    st.subheader("Total des valeurs manquantes :")
    Total_val_manquante = data.isnull().sum()
    st.write(Total_val_manquante)
    st.subheader("Nombre de vente Online et Store :")
    Channel_count = data.groupby('Channel').size()
    st.write(Channel_count)
    st.subheader("Nombre de vente au Centre/North/South :")
    Channel_count1 = data.groupby('Region').size()
    st.write(Channel_count1)

elif menu == "Statisques descriptives":
    st.header("Statisques descriptives")
    st.subheader("Description des données :")
    descr = data.describe().round(2)
    st.dataframe(descr, width=1000)
    
    st.subheader("Etude de correlation :")
    correlation = data.select_dtypes(include='number').corr().round(2)
    st.dataframe(correlation, width=1000)
    
    st.subheader("Carte de chaleur :")
    fig, ax = plt.subplots(figsize=(10, 10))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
    plt.suptitle("Carte de chaleur", fontsize=16)
    st.pyplot(fig)
    
    st.subheader("Boite a moustache :")
    fig, ax = plt.subplots(figsize=(10, 10))
    sns.boxplot(data=data, ax=ax)
    plt.suptitle("Boite a moustache", fontsize=16)
    st.pyplot(fig)
    
    st.subheader("Histogramme :")
    fig, ax = plt.subplots(2, 3, figsize=(10, 10))  
    data.hist(bins=15, ax=ax, rwidth=0.8, color='skyblue', edgecolor='black')
    plt.suptitle("Histogramme", fontsize=16)
    st.pyplot(fig)
    
    st.subheader("Matrice de dispersion :")
    fig, ax = plt.subplots(figsize=(15, 10))
    scatter_matrix(data, ax=ax, color='g')
    plt.suptitle("Matrice de dispersion", fontsize=22)
    st.pyplot(fig)
    
    st.subheader("Matrice de dispersion par la variable channel :")
    fig = sns.pairplot(data, hue='Channel')
    fig.fig.suptitle("Matrice de dispersion", fontsize=26)
    fig.fig.tight_layout()
    fig.fig.subplots_adjust(top=0.95)
    st.pyplot(fig)
    
    st.subheader("Histogramme en cercle des sommes des corrélations :")
    data = read_csv(fichier, names=col)
    corr = data.select_dtypes(include='number').corr()
    sums = corr.sum()
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(aspect="equal"))
    colors = plt.cm.tab20c.colors
    wedges, texts, autotexts = ax.pie(sums, labels=sums.index,
    autopct='%1.1f%%', startangle=90, colors=colors)
    fig.suptitle("Histogramme en cercle", fontsize=16)
    st.pyplot(fig)

elif menu == "Compte rendu":    
    st.markdown("<h1 style='text-align: center;'>Compte rendu</h1>", unsafe_allow_html=True)

    st.markdown("""
### 1. Analyse des Données  
#### Canal de Distribution et Région  
**Canal de vente :** 142 ventes proviennent de la plateforme **Online**, tandis que 298 sont réalisées en **magasin**. Cela reflète une préférence marquée pour les ventes en boutique.  

**Région :** La majorité des ventes proviennent de la région **Sud** (316), suivie par le **Nord** (77) et le **Centre** (47). Cela pourrait indiquer une présence ou une popularité plus forte dans le Sud.  

#### Statistiques par Produit  
Voici un aperçu des performances par type de café :  
- Les ventes moyennes et les écarts types sont calculés pour chaque produit afin d'évaluer leur popularité.  
- **Espresso** et **Robusta** se démarquent comme les plus vendus, tandis que **Latte** et **Cappuccino** enregistrent des ventes plus faibles.  

---

### 2. Modèles et Tendances Identifiés  
#### Analyse par Canal  
En comparant les ventes moyennes par produit sur les canaux **Online** et **magasin**, certaines tendances émergent :  
- **Espresso** et **Robusta** sont plus populaires en magasin, probablement en raison de la préférence pour les produits prêts à consommer.  
- **Lungo** se vend davantage en ligne, suggérant une attractivité spécifique pour ce type de produit sur ce canal.  

#### Corrélations Entre Produits  
L'analyse de la matrice de corrélation révèle des associations notables entre certains cafés :  
- **Espresso** et **Latte** montrent une corrélation positive, ce qui peut indiquer que les clients achetant l’un ont tendance à acheter l’autre. Cela ouvre des opportunités pour des offres combinées.  

---

### 3. Recommandations pour la Nouvelle Campagne Marketing  
#### Ventes Croisées et Offres Groupées :  
- Créer des **offres combinées** incluant **Espresso** et **Latte**, en exploitant leur corrélation de vente.  

#### Promotions Ciblées par Canal :  
- **Online :** Mettre en avant des produits comme le **Lungo**, plus populaire sur ce canal, avec des promotions spécifiques pour attirer davantage de clients en ligne.  
- **Magasin :** Renforcer la promotion des produits phares (**Robusta** et **Espresso**) via des **programmes de fidélité** afin d’encourager la récurrence des achats.  

#### Approche Régionale :  
- Concentrer les efforts marketing sur la région **Sud**, qui génère la majorité des ventes, en intensifiant les campagnes publicitaires et les offres locales.  

---

### 4. Données Supplémentaires à Collecter  
Pour affiner l’analyse et optimiser les décisions marketing, il serait pertinent de collecter :  
- **Données démographiques des clients** (âge, genre, localisation précise)  
- **Fréquence d'achat et historique client** (pour identifier les habitudes)  
- **Périodes de vente** (saisonnalité des achats)  
- **Retours clients et avis** (pour identifier les préférences et les points d’amélioration)  
""", unsafe_allow_html=True)
