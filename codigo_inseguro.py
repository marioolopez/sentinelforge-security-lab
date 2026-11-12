# LABORATORIO DE SEGURIDAD
# Código intencionadamente inseguro.
# NO EJECUTAR. Solo para análisis estático.

import pickle
import subprocess


def evaluar(texto):
    return eval(texto)


def ejecutar(codigo):
    exec(codigo)


def lanzar(comando):
    subprocess.run(comando, shell=True)


def cargar(archivo):
    with open(archivo, "rb") as fichero:
        return pickle.load(fichero)
