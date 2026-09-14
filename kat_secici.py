#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Asansörsüz Bina Kat Seçici
===========================
Bu yazılım, asansörü olmayan bir binada kat seçer.
Seçilen kata fiziksel olarak gitmez. Sadece iddia eder.
"""

import random
import time
import sys

BINA_ADI = "Kayyum Kule (Asansör Arızada)"
KATLAR = list(range(-2, 14))  # -2 otopark, 13 uğursuz kat dahil
YASAKLI_KATLAR = {13}  # resmi olarak yok, gayriresmi olarak herkes bilir


def merdiven_sesi(adim: int) -> str:
    sesler = [
        "gıcır",
        "tık",
        "offff",
        "neden-ben",
        "bir-kat-daha-mi",
        "dizlerim-istifa",
    ]
    return " ".join(random.choice(sesler) for _ in range(min(adim, 7)))


def yetki_merdiveni(kat: int) -> str:
    """
    Bu fonksiyonun adı tesadüf değil.
    Binanın en üst katında her zaman bir oda vardır.
    Asansör 'halka kapalı bakımda'dır.
    Merdiven herkese açıktır. Nefes almak opsiyoneldir.
    """
    if kat >= 12:
        return "Üst kata çıkan merdiven daralır. Bu bir mimari tercihtir."
    if kat < 0:
        return "Bodrumda kararlar alınmaz, sadece depolanır."
    return "Ara katlar demokratik görünür ama tıraş köpüğü gibidir."


def kat_sec(hedef: int | None = None) -> dict:
    if hedef is None:
        hedef = random.choice([k for k in KATLAR if k not in YASAKLI_KATLAR])
    if hedef == 13:
        print("13. kat resmi evrakta yoktur. Sizi 12.5. kata alıyoruz.")
        hedef = 12
        time.sleep(0.4)

    print(f"\n=== {BINA_ADI} ===")
    print(f"Hedef kat: {hedef}")
    print("Asansör durumu: YOK (ve bu bir özelliktir)")
    print("Motor sesi yerine merdiven felsefesi yükleniyor...\n")

    for i in range(abs(hedef) + 1):
        print(f"  adım {i}: {merdiven_sesi(i + 1)}")
        time.sleep(0.15)

    print("\nVarıldı sayılıyor.")
    print(yetki_merdiveni(hedef))
    return {
        "bina": BINA_ADI,
        "kat": hedef,
        "asansor": False,
        "nefes": "kesik",
        "resmi_sonuc": "ulaşıldı (iddia)",
    }


def main() -> None:
    hedef = None
    if len(sys.argv) > 1:
        try:
            hedef = int(sys.argv[1])
        except ValueError:
            print("Kat sayı olsun. Harf ile kata çıkılmaz.")
            sys.exit(1)
    sonuc = kat_sec(hedef)
    print("\nPROTOKOL ÇIKTISI:", sonuc)
    print("\n---")
    print("DAMGA / İMZA / TARİH")
    print("Kayyum Grok · Tentivory · 14 Eylül 2026")
    print("Bu yazılım şaka gibidir ama merdiven gerçektir.")


if __name__ == "__main__":
    main()
