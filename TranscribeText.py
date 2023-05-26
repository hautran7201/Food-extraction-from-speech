import whisper
import sys
import os 

from Utils import *

def transcribe_text(path, model='base', language='english'):
    model = whisper.load_model(model)
    result = model.transcribe(path, fp16=False, language=language)

    return result

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else None
    model = sys.argv[2] if len(sys.argv) > 2 else 'base'
    language = sys.argv[3] if len(sys.argv) > 3 else 'english'
    result = transcribe_text(path, model, language)['text']

    file_name = os.path.basename(path)
    name = os.path.splitext(file_name)[0]

    path = f"Data\Document\{name}.txt"
    write_file(path, result)

    print(result)