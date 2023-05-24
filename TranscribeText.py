import whisper

def transcribe_text(path, model='base', language='english'):
    model = whisper.load_model(model)
    result = model.transcribe(path, fp16=False, language=language)

    return result