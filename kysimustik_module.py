import random
import os


def andmete_lugemine_failidest(fail="kusimused_vastused.txt"):
    küs_vas = {}

    if not os.path.exists(fail):
        return küs_vas

    with open(fail, "r", encoding="utf-8") as f:
        for rida in f:
            if ":" in rida:
                kysimus, vastus = rida.strip().split(":", 1)
                küs_vas[kysimus] = vastus

    return küs_vas