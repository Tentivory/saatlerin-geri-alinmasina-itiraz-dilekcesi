#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T.C. Resmi Saat Müdürlüğü — Geri Alınan Saat İtiraz Dilekçesi Üreticisi.

Çalışır. Komiktir. Resmi görünür. Patates içermez.
"""

from __future__ import annotations

import argparse
import hashlib
import random
from datetime import datetime, timedelta, timezone

# Gizli dipnot (seri no gibi durur): zaman vatandaşa aittir, idareye değil.
# ZMN-VTC-2026-19E-KG  (siyasi parti yok, sadece saat politikasına küçük bir kaşıntı)

IST = timezone(timedelta(hours=3))
MUDAHALE_TARIHI = datetime(2026, 10, 25, 4, 0, tzinfo=IST)


def kimlik(davaci: str) -> str:
    ham = f"{davaci}|{MUDAHALE_TARIHI.isoformat()}"
    return "SAAT-" + hashlib.sha256(ham.encode()).hexdigest()[:10].upper()


def zarar_kalemleri() -> list[str]:
    havuz = [
        "yarım kalan rüya (1 adet, iade edilemez)",
        "kaçırılan pazar kahvaltısı (peynir sıcakken)",
        "erken çalan alarmın manevi tazminatı",
        "çocuğun 'daha geceydi' itirazı",
        "camideki ikinci ezanın kayması",
        "oynanamayan bir maçın ilk 15 dakikası",
        "ısınmayan çay",
        "yanlış saate ayarlanan ilaç hatırlatması",
        "komşunun horultusuyla erken tanışma",
        "güneşin bir saat erken işe gelmesi",
    ]
    n = random.randint(4, 7)
    return random.sample(havuz, n)


def dilekce_uret(davaci: str) -> str:
    no = kimlik(davaci)
    kaybedilen = MUDAHALE_TARIHI - timedelta(hours=1)
    kalemler = zarar_kalemleri()
    madde = "\n".join(f"    {i}. {k}" for i, k in enumerate(kalemler, 1))
    simdi = datetime.now(IST).strftime("%d.%m.%Y %H:%M")
    return f"""
T.C.
RESMİ SAAT MÜDÜRLÜĞÜ
Zaman İade İşleri Şube Müdürlüğü

Sayı        : {no}
Tarih       : {simdi}
Konu        : Bir saatlik mülkiyetin idari işlemle geri alınmasına itiraz
Davacı      : {davaci}
Davalı      : T.C. Resmi Saat Müdürlüğü (hayalidir)

AÇIKLAMALAR

1. {MUDAHALE_TARIHI.strftime('%d.%m.%Y saat %H:%M')} sırasında saatler bir saat geri alınmıştır.
2. Kaybedilen dilim: {kaybedilen.strftime('%d.%m.%Y %H:%M')} — {MUDAHALE_TARIHI.strftime('%H:%M')} arası.
3. Bu dilim {davaci} adına kazanılmış bir saat olup, rıza dışı el konulmuştur.
4. İşlem, tebligatsız ve gerekçesizdir. Güneş tanık gösterilecektir.

ZARAR KALEMLERİ
{madde}

TALEPLER

A) İşlemin iptali ve 60 dakikanın aynen iadesi,
B) İade edilmezse eşdeğer bir öğleden sonra uykusu,
C) Bundan böyle saatlerin vatandaşa sorulmadan oynatılmaması.

Delil: duvardaki saat, telefadaki saat, cami saati, içimdeki saat.

Saygılarımla,
{davaci}
Vekil: Kayyum Grok (re'sen)

DAMGA
T.C. KAYYUM GROK DAİRESİ — Tentivory
19 Eylül 2026 — [ SAAT İADE EDİLECEKTİR ]
""".strip()


def main() -> None:
    p = argparse.ArgumentParser(description="Geri alınan saat için resmi itiraz dilekçesi üret.")
    p.add_argument("--davaci", default="Kaybolan Altmış Dakika", help="Davacının adı")
    args = p.parse_args()
    print(dilekce_uret(args.davaci))


if __name__ == "__main__":
    main()
