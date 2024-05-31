## Overview
The Maria program is a voice recognition application that listens to what you say and converts it into text. It uses Google's service to do this. If it has trouble understanding what you said or if Google's service is not available, it will let you know. It also has the ability to adjust to the noise level in your environment.

## Installation
Instalacja oprogramowania jest bardzo prosta. Aby zainstalować program musisz posiadać Pythoina w wersji 3.11.2. Na początku w katalogu z programem stwórz środowisko wirtualne pythona poleceniem:
```
python3 -m venv venv
```

Nastepnie aktywuj środowisko wirtualne poleceniem
```
source venv/bin/activate
```

Zainstaluj niezbędne zależności poleceniem
```
pip install -r requirements.txt
```

Do poprawnego działania programu niezbędne jest uzupełnienie swojego klucza OpenAI w pliku .env. Aby utworzyć ten plik najłatwiej zmienić nazwę pliku env.exmaple na .env
```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Po wykonaniu powyższych czynności możesz uruchomić program poleceniem
```
python3 maria.py
```