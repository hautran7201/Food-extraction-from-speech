# Food-extraction-from-speech
Diagram:
![inq5erdiagram](https://github.com/hautran7201/Food-extraction-from-speech/assets/100859592/f34cce0d-1c6e-4d5d-834c-9e649aa13c8c)


## Folder structure:
```bash
│   .gitignore
│   main.py
│   Ner.py
│   README.md
│   requirements.txt
│   TranscribeText.py
│   Utils.py
│
├───Audio
│       sample-0.mp3
│
├───Data
│       Source.txt
│
├───Item List
│   │   CreateItemList.py
│   │
│   └───Data
│           Source.txt
│
└───Mwe List
    │   CreateMweList.py
    │   MweCreation.py
    │
    └───Data
            Source.txt
```

- Data: 
    + Download data from lin: [link](https://www.kaggle.com/datasets/paultimothymooney/recipenlg)
    + Put the file RecipeNLG_dataset.csv to Data folder

- ItemList:
    + Download 2 files from link: [Item list](https://drive.google.com/drive/folders/1IOOSYrIxSwDZSNfZUwEt1zxIEGGB-wM2?usp=sharing)

- Mwe:
    + Download 2 files from link: [Mwe list](https://drive.google.com/drive/folders/17UKEvlf_xMnc2zKrM1p8zQm7MR0M0Iq6?usp=sharing)


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

