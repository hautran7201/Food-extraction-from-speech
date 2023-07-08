# **Food-extraction-from-speech**

## Desciption:
Extract food and ingredient entity from audio file.

## Diagram:
![inq5erdiagram](https://github.com/hautran7201/Food-extraction-from-speech/assets/100859592/1e116d3d-917d-4877-873d-dc397854e3a6)

## Folder structure:

```bash
├── .gitignore
├── Data/
│   ├── Audio
│   ├── Document
│   ├── Entity
│   └── Source/
│       └── Source.txt
├── Mwe List/
│   ├── CreateMweList.py
│   ├── CreateRankList.py
│   ├── Data/
│   │   ├── food_ranking.npy
│   │   ├── ingredient_ranking.npy
│   │   ├── mwe.npy
│   │   └── Source.txt
│   ├── Food_ranking.py
│   ├── Ingredient_ranking.py
│   └── MweCreation.py
├── Ner.py
├── README.md
├── requirements.txt
├── TranscribeText.py
├── tree.py
└── Utils.py
```

## Installation:

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
```
DownLoad data
```
    python Utils.py download_data
```

# Usage 
### From command line
```
    $ # Speech to text 
    $ python TranscribeText.py Data\Audio\sample.mp3
    In a heavy 2-quart saucepan, mix brown sugar and nuts.
        
    $ # Entity extraction
    $ python Ner.py Data\Document\sample.txt
    ['saucepan', 'brown sugar', 'nuts']
```

