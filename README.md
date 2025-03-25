## scolaire
projet de groupe : Tom et Evann
utiliser la programation orientée objet et le format infixe pour effectuer des opérations mathématiques.
Une calculatrice web utilisant Flask (backend) et HTML/CSS (frontend).
- Backend : Import de calcul et derive depuis calculate.
- Flask : Routes / pour le formulaire et /calculate pour le calcul.
- Gestion de la requête POST pour traiter l'expression.

## instalation
1) Cloner le dépot avec `git clone https://github.com/AKtomik/fixcalc`
2) Installer et configurer python >3.10.

pour l'interface web :

3) Installer [Flask](https://flask.palletsprojects.com/en/stable/installation/).
4) Nous envoyer 3 bitcoins
5) Exécuter [index.py](./index.py)
6) S'amuser à dériver et calculer !
  
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
- [ ] affichage des erreurs de syntaxe
- [ ] fractions avec plusieurs unitées au dénominateur
- [ ] affichage des racines

## url 
https://nsi.t-lab.ovh
