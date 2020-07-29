## Project Summer: AI Lab & Glider: Process mining
----------

**Process mining** dolor sit amet, consectetur adipiscing elit. Pellentesque malesuada ornare diam condimentum elementum. Duis molestie at velit vel tempor. Praesent non rhoncus arcu. Fusce ultrices lacus at quam posuere, vel faucibus odio elementum. Pellentesque mattis ligula metus, ac sagittis orci auctor finibus. Nam gravida massa diam, in dignissim ipsum faucibus eu.

## Instalacja i setup środowiska
Zanim zaczniesz pracę stwórz i aktywuj swoje wirtualne środowisko:
```bash
python3 -m venv venv

# Windows
venv\Scripts\activate.bat

# Unix lub MacOS
source venv/bin/activate
```
Zainstaluj wymagane pakiety poprzez wykonanie `Makefile` przy uzyciu polecenia `make` lub:
```bash
# install required packages
pip install -r requirements.txt
```
`Makefile` uruchomi równiez lintowanie twojego kodu, mozesz to zrobic ręcznie poprzez:
```bash
flake8 path/to/your/code
```

## Workflow i rozwój projektu
Pracując nad nowym zadaniem/feature stwórz najpierw nowy [issue](https://github.com/Project-Summer-AI-Lab-Glider/process-mining/issues) i opisz co jest twoim zadaniem.

Następnie stwórz i przełącz się na nowego `brancha`:
```bash
git checkout -b "<issue-number>-<branch-name>"
```
Staraj się trzymac się konwencji podczas tworzenia nowych `branchy`, jako `issue-number` uzyj numeru `issue`.

### Struktura projektu
Pracując nad nowymi zadaniami trzymaj się odpowiedniej struktury projektu, twórz swój kod w kolejnych podkatalokach w folderze `src`.
```
    docs/
        ...
    src/
        feat1/
            ...
        your-task/
            your-code-here
    tests/
        ...
```

### Commity 
Tworząc commity zaleca się trzymac ustalonej konwencji, jego treśc powinna wyglądac następująco: `[#<issue-number>] <commit-prefix>:<commit-message>`, jako `issue-number` uzyj numeru `issue`, którego dotyczy aktualny commit, `commit-prefix` to przedrostek commitu informujący co było zrobione np. `feat`, `fix`, `docs` wg [tej](https://www.conventionalcommits.org/en/v1.0.0/) konwencji, na samym koncu krótko opisz co zostało wykonane w tym commicie.


### Dokumentacja
Dokumentacje, instrukcje, tłumaczenia rozwiązań i stosowanych metod twórz w katalogu `docs`.




## Licencja
Nulla facilisi. Fusce dui enim, viverra eu ipsum lacinia, dapibus pellentesque augue. Proin convallis leo dictum volutpat malesuada. Nunc volutpat, nunc a cursus imperdiet, erat arcu imperdiet massa, vitae laoreet lectus neque quis magna. Aliquam pellentesque laoreet nisi, vel aliquet magna bibendum et.