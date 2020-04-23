# app-generare-numere-pseudo-aleatoare-bbs

## Cerinte preliminare
[Descarca si instaleaza Python3](https://www.python.org/downloads/)
`Comenzile se executa din CMD in interiorul directorului proiectului clonat`

## Dezvoltare
Dupa ce se cloneaza local proiectul, se executa
```
py AppGenerareNumerePseudoAleatoareBBS.py
```

## Impachetare
[Descarca si instaleaza `pip`](https://pip.pypa.io/en/stable/installing/)

Se instaleaza `pyinstaller` folosind pip
```
py -m pip install pyinstaller
```
Se impacheteaz(pentru Windows) efectiv prin
```
pyinstaller --onefile --noconsole .\AppGenerareNumerePseudoAleatoareBBS.py
```
