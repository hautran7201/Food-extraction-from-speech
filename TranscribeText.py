import whisper
import sys

def transcribe_text(path, model='base', language='english'):
    model = whisper.load_model(model)
    result = model.transcribe(path, fp16=False, language=language)

    return result

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else None
    model = sys.argv[2] if len(sys.argv) > 2 else 'base'
    language = sys.argv[3] if len(sys.argv) > 3 else 'english'

    print('\nSpeech to text:\n')
    print(transcribe_text(path, model, language)['text'])