import davipy as dv


url = "https://www.chess.com/"
print(dv.ping(url))


# combined example usage
if dv.ping(url):  # TODO concettualmente sbagliato: se ne hai bisogno, dovresti spostare questo controllo in .listlink()
    dv.listlink(url)
