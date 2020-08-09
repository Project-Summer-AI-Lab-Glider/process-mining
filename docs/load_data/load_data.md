## Paczka `load_data` 

Paczka `load_data` słuzy do pobierania i ładowania zbioru danych maili z Apache do wybranego pliku.

```bash
python3 load_data.py --help
usage: load_data.py [-h] [-v] [-p PATH]

Script used to download data and save in data/ directory. You can specify path to save data.

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Setting verbose debug inform
```

### Instalacja potrzebnych pakietów
Przed użyciem musisz zainstalować wymagane pakiety, takie jak `selenium`, `pandas` czy `numpy`:
```bash
pip install -r requirements.txt
```
Następnie musisz zainstalować driver do Google Chrome dla pakietu `selenium`:
* [Dokumentacja nt. instalacji](https://selenium-python.readthedocs.io/installation.html)
* [Webdrivery do Google Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)
```bash
# rozpakuj pobrany plik, np.
tar -zxvf chromedriver_mac64.zip

# usuń plik .zip
rm chromedriver_mac64.zip

# dodaj uprawnienia do wykonywania
chmod +x ./chromedriver

# przenieś chromedriver do bin (dla OS X jest to /usr/local/bin)
sudo mv chromedriver /usr/local/bin
```
* Pamiętaj, że wersja webdrivera musi się zgadzać z wersją Google Chrome.


### Przykłady użycia
```bash 
# domyślne wywołanie - zapis do pliku ../../data/raw_data.csv
python3 load_data.py

# zapis danych do wybranego pliku
python3 load_data.py -p /path/to/file

# zapis danych do wybranego pliku i włączenie komunikatów
python3 load_data.py -p /path/to/file --verbose
```
