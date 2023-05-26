from __future__ import annotations


def stringlower(stringa: str, posizione_inizio: int, posizione_fine: int = None) -> str:
    stringa = list(stringa)  # sovrascrivere i parametri di una funzione è generalmente una bad practice

    if posizione_fine is None:
        stringa[posizione_inizio] = stringa[posizione_inizio].lower()
    else:
        # TODO puoi generalizzare questo for per farlo funzionare anche nel caso "if not", così puoi eliminare l'if completamente
        for x in range(posizione_inizio, posizione_fine):
            stringa[x] = stringa[x].lower()

    return "".join(stringa)


def stringUPPER(stringa: str, posizione_inizio: int, posizione_fine=None) -> str:
    stringa = list(stringa)

    if posizione_fine is None:
        stringa[posizione_inizio] = stringa[posizione_inizio].upper()
    else:
        # TODO same of stringlower()
        for x in range(posizione_inizio, posizione_fine):
            stringa[x] = stringa[x].upper()

    return "".join(stringa)
