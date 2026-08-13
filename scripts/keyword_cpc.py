#!/usr/bin/env python3
"""
Прогон ниш по реальным данным Google Ads через DataForSEO — гео: ES / AR / RU.

Фокус на трёх больших неанглийских языках, где англоязычные обёртки не
локализованы, а CPC в разы дешевле: испанский (Испания, Мексика),
арабский (Саудия, ОАЭ, Египет), русский (РФ).

Что делает: берёт кластеры ключей В РОДНОМ ЯЗЫКЕ по каждой нише + гео,
дёргает DataForSEO Google Ads "search_volume/live" и печатает таблицу:
объём, реальный CPC, конкуренция, ставки — и сразу считает грубый CAC.

DataForSEO: аккаунт Google Ads НЕ нужен. Депозит $50, логин/пароль к API.
Весь прогон — меньше $1.

ВАЖНО про деньги: РФ как рынок обслуживается, но приём оплаты из РФ на
финское юрлицо заблокирован санкциями (см. ideas/2026-07-wb-sellers...).
Испанский и арабский (Залив) чище: Stripe/эквайринг работает.

Запуск:
  export DATAFORSEO_LOGIN='...'; export DATAFORSEO_PASSWORD='...'
  python3 scripts/keyword_cpc.py                       # все ниши, все гео
  python3 scripts/keyword_cpc.py bank_statement tts    # выбранные ниши
  python3 scripts/keyword_cpc.py --geo ES MX SA        # выбранные гео
  python3 scripts/keyword_cpc.py --csv out.csv         # выгрузка в CSV

Зависимостей нет (stdlib). Python 3.8+.
"""

import base64
import csv
import json
import os
import sys
import urllib.request

API_URL = "https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live"

# CAC = CPC / (клик→оплата). Консервативно 2.5% для холодного поиска в оплату.
CONV_VISIT_TO_PAID = 0.025

# гео → (location_code, language_code) по справочнику DataForSEO/Google Ads.
GEO = {
    # испанский
    "ES": (2724, "es"),   # Испания
    "MX": (2484, "es"),   # Мексика
    # арабский
    "SA": (2682, "ar"),   # Саудовская Аравия
    "AE": (2784, "ar"),   # ОАЭ
    "EG": (2818, "ar"),   # Египет
    # русский
    "RU": (2643, "ru"),   # Россия
}

# Ниши-лидеры из разбора 2026-08. Ключи заданы отдельно под каждый язык:
#   es — испанский, ar — арабский, ru — русский.
# geos — где карман предположительно живой (что и проверяем реальным CPC).
NICHES = {
    "bank_statement": {   # 8/10 — конвертер выписок → Excel
        "geos": ["ES", "MX", "SA", "AE", "RU"],
        "es": ["convertir extracto bancario a excel", "extracto bancario pdf a excel",
               "convertidor de extractos bancarios"],
        "ar": ["تحويل كشف حساب بنكي الى اكسل", "تحويل كشف الحساب pdf الى excel",
               "تحويل كشف حساب الى excel"],
        "ru": ["конвертер банковских выписок в excel", "выписка pdf в excel",
               "распознать банковскую выписку"],
    },
    "podcast_notes": {    # 8/10 — транскрибация/шоуноуты подкастов
        "geos": ["ES", "MX", "SA", "RU"],
        "es": ["transcripción de podcast", "transcribir podcast", "notas de podcast ia"],
        "ar": ["تفريغ بودكاست", "تحويل بودكاست الى نص", "تفريغ صوتي الى نص"],
        "ru": ["транскрибация подкаста", "расшифровка подкаста", "подкаст в текст"],
    },
    "tts_voiceover": {    # 6/10 — озвучка текста голосом
        "geos": ["ES", "MX", "SA", "AE", "EG", "RU"],
        "es": ["generador de voz ia", "texto a voz", "voz en off ia"],
        "ar": ["تحويل النص الى كلام", "توليد صوت ذكاء اصطناعي", "تعليق صوتي ذكاء اصطناعي"],
        "ru": ["синтез речи онлайн", "озвучка текста", "генератор голоса нейросеть"],
    },
    "video_dubbing": {    # 6/10 — дубляж/перевод видео голосом
        "geos": ["ES", "MX", "SA", "AE", "EG", "RU"],
        "es": ["doblaje de video ia", "traducir video con voz ia", "doblar video ia"],
        "ar": ["دبلجة فيديو بالذكاء الاصطناعي", "ترجمة فيديو بالصوت", "دبلجة الفيديو"],
        "ru": ["озвучка видео нейросеть", "перевод видео голосом", "дубляж видео ии"],
    },
    "paraphrase": {       # 6/10 — рерайт/перефраз для студентов
        "geos": ["ES", "MX", "SA", "EG", "RU"],
        "es": ["parafrasear texto", "reformular texto online", "reescribir texto"],
        "ar": ["اعادة صياغة النص", "اعادة صياغة نص", "تحسين صياغة النص"],
        "ru": ["перефразировать текст", "рерайт текста онлайн", "уникализатор текста"],
    },
    "virtual_staging": {  # 6/10 — виртуальный стейджинг (Залив — богатая недвижка)
        "geos": ["ES", "MX", "SA", "AE", "RU"],
        "es": ["home staging virtual", "amueblar habitación virtual ia",
               "puesta en escena virtual inmobiliaria"],
        "ar": ["فرش افتراضي للعقارات", "تصميم داخلي بالذكاء الاصطناعي",
               "ديكور افتراضي للشقق"],
        "ru": ["виртуальный стейджинг", "виртуальная меблировка квартиры",
               "дизайн интерьера нейросеть"],
    },
    "yt_thumbnail": {     # 6/10 — превью для ютуберов
        "geos": ["ES", "MX", "SA", "EG", "RU"],
        "es": ["miniaturas para youtube", "generador de miniaturas ia",
               "creador de miniaturas youtube"],
        "ar": ["تصميم صور مصغرة يوتيوب", "صانع ثامبنيل", "تصميم غلاف فيديو يوتيوب"],
        "ru": ["превью для youtube", "генератор превью нейросеть",
               "сделать обложку для видео"],
    },
}


def fetch(login, password, keywords, location_code, language_code):
    payload = json.dumps([{
        "keywords": keywords,
        "location_code": location_code,
        "language_code": language_code,
    }]).encode()
    token = base64.b64encode(f"{login}:{password}".encode()).decode()
    req = urllib.request.Request(
        API_URL, data=payload,
        headers={"Authorization": f"Basic {token}",
                 "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.load(resp)
    if data.get("status_code") != 20000:
        raise RuntimeError(f"API error: {data.get('status_message')}")
    return data["tasks"][0].get("result") or []


def cac(cpc):
    return round(cpc / CONV_VISIT_TO_PAID, 2) if cpc else None


def main():
    login = os.environ.get("DATAFORSEO_LOGIN")
    password = os.environ.get("DATAFORSEO_PASSWORD")
    if not login or not password:
        sys.exit("Задай DATAFORSEO_LOGIN и DATAFORSEO_PASSWORD в окружении.")

    argv = sys.argv[1:]
    csv_path = None
    geo_filter = None
    if "--csv" in argv:
        i = argv.index("--csv"); csv_path = argv[i + 1]; del argv[i:i + 2]
    if "--geo" in argv:
        i = argv.index("--geo")
        geo_filter = []
        j = i + 1
        while j < len(argv) and argv[j] in GEO:
            geo_filter.append(argv[j]); j += 1
        del argv[i:j]
    selected = argv or list(NICHES.keys())

    rows = []
    for niche in selected:
        cfg = NICHES.get(niche)
        if not cfg:
            print(f"  ! неизвестная ниша: {niche}")
            continue
        for geo in cfg["geos"]:
            if geo_filter and geo not in geo_filter:
                continue
            loc, lang = GEO[geo]
            kws = cfg.get(lang, [])
            if not kws:
                continue
            try:
                items = fetch(login, password, kws, loc, lang)
            except Exception as e:
                print(f"  ! {niche}/{geo}: {e}")
                continue
            for it in items:
                rows.append({
                    "niche": niche, "geo": geo, "keyword": it.get("keyword"),
                    "volume": it.get("search_volume"), "cpc": it.get("cpc"),
                    "competition": it.get("competition"),
                    "low_bid": it.get("low_top_of_page_bid"),
                    "high_bid": it.get("high_top_of_page_bid"),
                    "cac_est": cac(it.get("cpc")),
                })

    rows.sort(key=lambda r: (r["cpc"] is None, r["cpc"] or 0))

    hdr = f'{"niche":15} {"geo":3} {"keyword":34} {"vol":>7} {"cpc":>6} {"comp":>5} {"CAC~":>7}'
    print("\n" + hdr + "\n" + "-" * len(hdr))
    for r in rows:
        print(f'{r["niche"]:15} {r["geo"]:3} {str(r["keyword"])[:34]:34} '
              f'{str(r["volume"] or "-"):>7} {str(r["cpc"] or "-"):>6} '
              f'{str(r["competition"] or "-"):>5} {str(r["cac_est"] or "-"):>7}')

    print(f'\n  CAC = CPC / {CONV_VISIT_TO_PAID:.1%}. Бьётся, если LTV ниши > CAC.')
    print('  Напоминание: приём оплаты из РФ на финское юрлицо заблокирован — '
          'ES и арабский Залив по деньгам чище.')

    if csv_path and rows:
        with open(csv_path, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader(); w.writerows(rows)
        print(f"  CSV: {csv_path}")


if __name__ == "__main__":
    main()
