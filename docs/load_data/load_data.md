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

### Przykłady uzycia
```bash 
# domyślne wywołanie - zapis do pliku ../../data/raw_data.csv
python3 load_data.py

# zapis danych do wybranego pliku
python3 load_data.py -p /path/to/file

# zapis danych do wybranego pliku i włączenie komunikatów
python3 load_data.py -p /path/to/file --verbose
```