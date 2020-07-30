## Project Summer: AI Lab & Glider: Process mining
----------

**Process mining** to zbiór narzędzi pozwalających na budowę modeli procesów zachodzących w projecie i ich weryfikację. Analiza przeprowadzana jest przy użyciu danych pochodzących z dzienników zdarzeń (logów), powszechnie dostępnych we współczesnych systemach informatycznych. Realne dane pozwalają na odkrycie ogólnej struktury działania firmy oraz zachodzącego w niej workflow. Celem naszego projektu jest odkrycie tego modelu procesu, na podstawie bazy maili wymienianych w trakcie trwania projektu.

Praca inspirowana jest artykułem wydanym przez naukowców z Defence Science and Technology Edinburgh oraz MIT Lincoln Laboratory Lexington. W projekcie użyto 250 maili z Apache Camel oraz zdefiniowany został 'ground truth', czyli manualne określenie kategorii dla zbioru słów kluczowych, użytych w mailu. 


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
