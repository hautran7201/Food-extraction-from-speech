# **Food-extraction-from-speech**

## Desciption:
Extract food and ingredient entity from audio file.

## Diagram:
![inq5erdiagram](https://github.com/hautran7201/Food-extraction-from-speech/assets/100859592/f34cce0d-1c6e-4d5d-834c-9e649aa13c8c)


## Folder structure:

```bash
│   .gitignore
│   Ner.py
│   README.md
│   requirements.txt
│   TranscribeText.py
│   Utils.py
│
├───Data
│   ├───Audio
│   │       sample-0.mp3
│   │
│   ├───Document
│   │       Recipe.txt
│   │
│   └───Source
│           Source.txt
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
    python -m spacy download en_core_web_sm
    python -m nltk.downloader punkt
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

