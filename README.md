## Scolaire
projet de groupe : Tom et Evann
### Une logique objet !
La chaine de caractère subit plusieurs conversions pour être correctement calculée.

str → infix → postfix → Result → str
- Transformation en infixe → reconnaitre les nombres et sépare les éléments.
- Conversion en postfixe → ordonner les oppérateurs en suivant la logique humaine.
- Calcul dans l'ordre infixé → itération et calculs en manipulant les classes Résultat et Opérations qui utilisent la surcharge d'opérateurs.
- Affichage en chaine de caractères → tranformation de l'objet Résultat en quelque chose de lisible.
### Une interface web !
Une calculatrice web utilisant Flask (backend) et HTML/CSS (frontend).
- Backend : Import de calcul et derive depuis calculate.
- Flask : Routes / pour le formulaire et /calculate pour le calcul.
- Gestion de la requête POST pour traiter l'expression.

## Utilisation
Le projet est utilisable ici : https://fixcalc.onrender.com/
-# Le serveur se met en veille après une periode d'innactivitée. Prends environ 15s pour le réveiller.

## Instalation
1) Cloner le dépot avec `git clone https://github.com/AKtomik/fixcalc`
2) Installer et configurer python >3.10.

pour l'interface web :

1) Installer les dépendances avec `pip install -r requirements.txt`
2) Nous envoyer 3 bitcoins
3) Exécuter [index.py](./index.py) avec python `python index.py`
4) S'amuser à dériver et calculer !
  
pour l'interface python :

1) En haut de votre fichier `from fixcalc import *`
2) (avancé) Definir des paramètres avec classe `Sett`
3) Utiliser `calcul(str)->Result` et `derive(str)->Result` pour effectuer des operations.

## réalisation
- [x] conversions infixe/postfixe
- [x] calcul d'expression numériques
- [x] frontend
- [x] résultats orientés objet
- [x] opérations orientées objet
- [x] calcul d'expression avec X
- [x] calcul d'expression avec X^n
- [x] dériver un résultat
- [x] opérations sur les dérivées
- [ ] opérations à entrée unique (log, e)
- [x] constantes connues (e, pi)
- [ ] nème distributivitée
- [ ] affichage des erreurs de syntaxe
- [ ] fractions avec plusieurs unitées au dénominateur
- [ ] affichage des racines
- [ ] thème sombre
