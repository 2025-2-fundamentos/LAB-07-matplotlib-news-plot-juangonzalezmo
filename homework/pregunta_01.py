"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import os
import pandas as pd
import matplotlib.pyplot as plt

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    ruta_csv = "files/input/news.csv"
    ruta_salida = "files/plots/news.png"

    df = pd.read_csv(ruta_csv)
    df = df.set_index(df.columns[0])  
    df.index.name = "Year"

    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)

    plt.figure(figsize=(8, 5))

    for col in df.columns:
        plt.plot(df.index, df[col], marker="o", label=col)

    plt.title("News consumption by medium over time")
    plt.xlabel("Year")
    plt.ylabel("Percentage of people")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.savefig(ruta_salida, dpi=120)
    plt.close()