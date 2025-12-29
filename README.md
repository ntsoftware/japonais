# Mégaliste de vocabulaire japonais

## Liste

### Colonnes

| # | Label     | Description
|---|-----------|------------
| 1 | guid      | Identifiant unique Anki
| 2 | fr        | Français
| 3 | ja        | Katakana / Kanji
| 3 | furigana  | Furigana
| 2 | romaji    | Romaji
| 7 | sound     | Son
| 8 | picto     | Pictogramme
| 6 | tags      | Tags Anki

### En-tête CSV

```
#separator:tab
#html:true
#guid column:1
#tags column:8
#columns:id	fr	ja	furigana	romaji	sound	picto	tags
```

### Vim modeline

Pour que vim affiche les colonnes de façon ordonnée lors de l'ouverture en mode
texte du fichier, ajouter une modeline en première lignre du fichier. Cette
ligne est ignorée par Anki lors de l'import.

```
# vim: vts=16,32,32,32,32,48 noet nowrap
```

## Anki

### Importer la liste

Sélectionner la liste
Cliquer sur "Importer" (en bas de la fenêtre)

Sélectionner le fichier `liste.csv`  puis cliquer sur "Ouvrir"

#### Fichier

- Séparateur de champ : Tabulation
- Tolérer du HTML dans les champs : oui

#### Options d'importation

| Option                            | Valeur
|-----------------------------------|-------
| Type de note                      | <liste>
| Paquet                            | <liste>
| Notes existantes                  | Mettre à jour
| Étendue de la correspondance      | Type de note
| Étiquetter toutes les notes       | <vide>
| Étiquetter les notes mises à jour | <vide>

### Exporter la liste

Icône "engrenages" > Exporter

- Format d'exportation : Notes en texte (.txt)
- Inclure : <liste>

Options d'exportation :

- [x] Include le HTML et les références vers les médias
- [x] Inclure les étiquettes
- [ ] Inclure le nom du paquet
- [ ] Inclure le nom du type de note
- [x] Inclure l'identifiant unique

Cliquer sur "Exporter..."

### Documentation

[Anki Manual - Text files](https://docs.ankiweb.net/importing/text-files.html)

## Accents

[Rechercher l'accent d'un mot](https://www.gavo.t.u-tokyo.ac.jp/ojad/fre/search/index)

## Sons

[Rechercher la prononciation d'un mot sur forvo](https://fr.forvo.com/languages/ja/)

## Pictos

### Rechercher un pictogramme

- [Picto facile](https://www.pictofacile.com/fr/download-picto)
- [ARASAAC](https://arasaac.org/pictograms/search)
- [Open Symbols](https://www.opensymbols.org/)
- [Pixabay vectors](https://pixabay.com/vectors/)

### Convertir un pictogramme

Les pictogrammes de la base sont des images au format `.png` de taille 500x500
pixels.

Avec `imagemagick` :

```shell
magick <image.svg> -resize 500x500 <image.png>
```

