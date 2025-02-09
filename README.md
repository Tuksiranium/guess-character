# Guess Character Game

## But du jeu
Le but de ce jeu est de trouver quel est le personnage que l'IA représente.
Vous posez des questions à l'IA, elle vous répond en vous donnant toujours plus de détail sur la personne qu'elle représente.
Dès que vous trouvez le nom de cette personne, vous avez gagné.

## Usage
Pour lancer le projet, vous aurez besoin de `python >3.10`.

1. Créez un environnement python : `python -m venv .venv`
2. Activez l'environnement : `source .venv/bin/activate` (bash) ou `.\.venv\Scripts\activate` (pwsh)
3. Importez les dépendances : `pip install -r ./requirements.txt`
4. Créer un fichier `.env` dans le root du dépôt, dans lequel vous mettez `HF_TOKEN={votre token hugginfaces}`.
4. Lancez `python main.py`

## Notes
Modèle utilisé : **Llama 3.2 1B**
