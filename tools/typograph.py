"""Простой типограф: неразрывные пробелы, чтобы предлоги, союзы, числа и тире не висели.

typo(text)          — обработать строку текста (без HTML)
typo_html(html)     — обработать только текст внутри <body>, не трогая теги, атрибуты и скрипты
"""
import re

NBSP = " "

# короткие слова, которые не должны оставаться в конце строки
SHORT = r"[А-Яа-яЁёA-Za-z]{1,2}|для|без|под|над|при|про|или|как"
_short = re.compile(r"(?<![\w\-])(%s) " % SHORT)
# число + следующее слово: «6 лет», «10+ страниц», «7 000+»
_num_word = re.compile(r"(\d[\d+%]*) (?=[\wА-Яа-яЁё])")
_thousands = re.compile(r"(?<!\d)(\d{1,3}) (?=\d{3}(?!\d))")
# тире не переносится в начало строки
_dash = re.compile(r" (—|–)")
# частицы, которые цепляются к предыдущему слову
_particle = re.compile(r" (же|ли|бы|ль)(?![\wА-Яа-яЁё])")


def typo(text: str) -> str:
    t = _thousands.sub(lambda m: m.group(1) + NBSP, text)
    t = _dash.sub(NBSP + r"\1", t)
    t = _particle.sub(NBSP + r"\1", t)
    # два прохода, чтобы цепочки вроде «и в» тоже склеились
    for _ in range(2):
        t = _short.sub(lambda m: m.group(1) + NBSP, t)
    t = _num_word.sub(lambda m: m.group(1) + NBSP, t)
    return t


def typo_html(html: str) -> str:
    head, sep, rest = html.partition("<body>")
    if not sep:
        return html
    parts = re.split(r"(<script\b.*?</script>|<[^>]+>)", rest, flags=re.S)
    out = [p if (p.startswith("<") or not p.strip()) else typo(p) for p in parts]
    return head + sep + "".join(out)
