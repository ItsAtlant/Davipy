import pandas as pd


def extension_file(file: str) -> str:  # TODO usa pathlib/simili
    extension = file.split(".")[-1]
    return extension.lower()


def openfile(filename: str) -> pd.DataFrame:
    extension = extension_file(filename)
    reader = {
        "csv": pd.read_csv,
        "xls": pd.read_excel,
        "xlsx": pd.read_excel,
        "json": pd.read_json,
    }

    if extension not in reader:
        raise ValueError("This function cant open your file")

    return reader[extension](filename)


def reportfile(file: str) -> None:
    extension = extension_file(file)
    df = openfile(file)

    stats_na = df.isna().sum().to_string()
    all_null = df.isna().sum().sum()
    null_rows = df[df.isna().any(axis=1)].to_string()

    filename = file.split("/")[-1]
    filename = filename.split(".")[0]

    with open(f"Report_{filename}.{extension}", "w") as f:  # Perchè dividi filename ed extension se puoi li riuniusci?
        f.write(f"This file has been written in {extension}\n\n")
        f.write("First 10 rows: \n")
        f.write(df.head(10).to_string() + "\n\n")
        f.write("Last 10 rows: \n")
        f.write(df.tail(10).to_string() + "\n\n")
        f.write(f"In this dataframe you have: {all_null} number of NA \n\n")
        f.write("Na for colums:\n")
        f.write(stats_na + "\n\n")
        f.write("Here is the rows where you have NA records:\n")
        f.write(null_rows)
