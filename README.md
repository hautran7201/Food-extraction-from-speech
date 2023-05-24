# Food-extraction-from-speech
(description)

## Folder structure:
```
    .
    ├── Audio
    ├── Data        * Data folder   
    ├── env         * Environment folder (created after run command below)
    ├── ITemList    * .npy folder
    ├── main.py
    ├── Mwe         * .Mwe folder
    ├── MweCreattion.py
    ├── Ner.py
    ├── __pycache__
    ├── README.md
    ├── TranscribeText.py
    └── Utils.py
```

- Data: 
    + Download data from link: https://www.kaggle.com/datasets/paultimothymooney/recipenlg
    + Put the file RecipeNLG_dataset.csv to Data folder

- ItemList:
    + Download 2 files from link: https://drive.google.com/drive/folders/1IOOSYrIxSwDZSNfZUwEt1zxIEGGB-wM2?usp=sharing

- Mwe:
    + Download 2 files from link: https://drive.google.com/drive/folders/17UKEvlf_xMnc2zKrM1p8zQm7MR0M0Iq6?usp=sharing


## Run Command:
Update pip:
```
    pip install --upgrade pip
```

Create and start virtual environments:
```
    pip install virtualenv
    python -m venv env
    
    # Windows activate
    env\Scripts\activate
    deactivate

    # Linux activate
    source env/bin/activate
    deactivate
```

Installing required packages:
```
    pip install -r requirements.txt
    python -m spacy download en_core_web_sm
```

Run Food extraction:
```
    python main.py
```

