#!/usr/bin/env python3
"""Генерирует страницы кейсов cases/<slug>.html из данных ниже.

Запуск из папки site:  python3 tools/build_cases.py
Тексты правим здесь, потом перезапускаем скрипт — HTML пересоберётся.
"""
import os
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CASES = [
    dict(
        slug="segmentstream", title="SegmentStream",
        lead="Сайт SaaS-платформы маркетинговой аналитики, который растёт вместе с продуктом.",
        cover="case-segmentstream.jpg",
        facts=[("клиент", "SaaS-платформа маркетинговой аналитики, Великобритания"),
               ("что делала", "Страница сайта и ведение команды"),
               ("команда", "Веб-дизайнер и иллюстратор"),
               ("объём", "10+ страниц, адаптив")],
        task="Продукт вырос, а визуальный стиль за ним не успевал. Нужен был сайт, который легко расширять на новые фичи и решения.",
        role=["Сделала страницу сайта и передала проект веб-дизайнеру",
              "Дальше вела веб-дизайнера и иллюстратора: следила за работой и качеством макетов"],
        done=["Обновили key visual — глубже, премиальнее, увереннее",
              "Собрали дизайн-систему страниц: фичи, решения, цены, кейсы — под все размеры экранов и готовую к разработке",
              "Иллюстратор сделал систему иллюстраций, которая по шагам объясняет атрибуцию и incrementality-тесты"],
        result="Сайт собран как система: новые страницы делаются из готовых шаблонов — командой или AI-агентом.",
        tags=["многостраничный сайт", "тимлид", "дизайн-система"],
    ),
    dict(
        slug="fraxis", title="Fraxis",
        lead="Многостраничный сайт-каталог для производителя кабельных сборок.",
        cover="case-fraxis.jpg",
        facts=[("клиент", "Производство кабельных сборок на заказ"),
               ("что делала", "Структура, дизайн и сборка сайта-каталога"),
               ("формат", "B2B, многоуровневый каталог"),
               ("платформа", "Tilda + кастомный код")],
        task="У компании широкая линейка продуктов и услуг для разных отраслей, собственное производство и контрактная разработка. Нужен был сайт-витрина, который показывает всё — и при этом остаётся понятным.",
        role=["Разработала многоуровневый сайт-каталог на Tilda",
              "Разложила продукцию и услуги в понятную структуру с удобной навигацией",
              "С помощью кода вышла за рамки типовых блоков платформы и собрала сложный B2B-сайт"],
        done_label="что сделала",
        done=["Сайт-витрина всей продукции и услуг компании",
              "Кастомный код вместо ограничений стандартных блоков Tilda",
              "Навигация, в которой не теряешься даже в большом каталоге"],
        result="По словам директора по маркетингу клиента, после запуска выросло количество заявок и средний чек.",
        tags=["многостраничный сайт", "tilda"],
    ),
    dict(
        slug="brs", title="BRS",
        lead="Минималистичный сайт на Webflow для ремонтной компании из Дубая.",
        cover="case-brs.jpg",
        facts=[("клиент", "Ремонт полного цикла: виллы, квартиры, офисы, Дубай"),
               ("что делала", "Страница сайта и ведение веб-дизайнера"),
               ("платформа", "Webflow + CMS"),
               ("основа", "Обновлённый логотип и айдентика студии")],
        task="Компания обновила визуальный стиль и хотела масштабировать маркетинг. Нужен был простой сайт, которым клиент управляет сам.",
        role=["Сделала страницу сайта и передала проект веб-дизайнеру",
              "Дальше следила за его работой до запуска"],
        done=["Минималистичный сайт в новом стиле бренда",
              "Webflow CMS с несколькими коллекциями — клиент сам обновляет весь контент"],
        result=None,
        tags=["многостраничный сайт", "тимлид", "webflow"],
    ),
    dict(
        slug="vet-workshop", title="vet_workshop",
        lead="Новая айдентика и редизайн сайта крупнейшей ветеринарной онлайн-школы.",
        cover="case-vet.jpg",
        facts=[("клиент", "Онлайн-школа для ветеринаров: 7000+ студентов, 17 направлений"),
               ("что делала", "Новая айдентика, редизайн главной, каталога и шаблонов курсов"),
               ("потом", "3 года вела веб-дизайнера на поддержке"),
               ("платформа", "Tilda")],
        task="Сделать продукт понятным для пользователей и при этом передать тематику школы.",
        role=["Сделала новую айдентику школы",
              "Переделала главную: структура и современный дружелюбный дизайн",
              "Масштабировала визуальную систему на каталоги курсов и шаблоны описаний",
              "Передала проект веб-дизайнеру и три года следила за его работой на поддержке"],
        done_label="что сделала",
        done=["Новая айдентика",
              "Новая главная страница",
              "Каталог курсов с фильтром — давняя проблема клиента, которую раньше не мог решить никто",
              "Шаблоны страниц курсов"],
        result="По отзыву соосновательницы школы, задачи сдавались в срок или раньше, а каталог-фильтр собрали за один день.",
        tags=["айдентика", "многостраничный сайт", "тимлид", "tilda"],
    ),
    dict(
        slug="bravestone", title="Bravestone",
        lead="Сайт агентства недвижимости в Португалии.",
        cover="case-bravestone.jpg",
        facts=[("клиент", "Помогает покупать недвижимость в Португалии"),
               ("что делала", "Дизайн сайта"),
               ("платформа", "Webflow"),
               ("основа", "Готовая айдентика студии")],
        task="Передать на сайте премиальный и уверенный образ бренда — для нового поколения инвесторов.",
        role=["Сделала сайт на основе готовой айдентики"],
        done_label="что сделала",
        done=["Сдержанный премиальный сайт в стиле бренда",
              "Сайт на Webflow"],
        result=None,
        tags=["многостраничный сайт", "webflow"],
    ),
    dict(
        slug="neon-insights", title="Neon Insights",
        lead="Айдентика с нуля и маркетинговый сайт консалтинга по данным и AI.",
        cover="case-neon.jpg",
        facts=[("клиент", "Консалтинг по анализу данных и AI, Нидерланды"),
               ("что делала", "Айдентика с нуля, дизайн сайта и сборка в Webflow"),
               ("платформа", "Webflow"),
               ("стиль", "Чистый, с неоновыми акцентами")],
        task="С нуля создать айдентику и сайт, которые помогут компании привлекать корпоративных партнёров и клиентов.",
        role=["Сделала айдентику с нуля",
              "Сделала дизайн маркетингового сайта",
              "Сама собрала его в Webflow"],
        done_label="что сделала",
        done=["Компактная визуальная система: чистый стиль с неоновыми элементами — про современные инструменты и простые решения",
              "Маркетинговый сайт на Webflow",
              "Обложки для соцсетей в том же стиле"],
        result=None,
        tags=["айдентика", "сайт", "webflow"],
    ),
    dict(
        slug="joompro", title="ДжумПро",
        lead="Новый маркетинговый сайт сервиса закупки и доставки товаров из Китая.",
        cover="case-joompro.jpg",
        facts=[("клиент", "Логистический сервис команды маркетплейса Joom"),
               ("что делала", "Редизайн сайта"),
               ("платформа", "Tilda + CMS «Потоки»"),
               ("основа", "Брендбук ДжумПро")],
        task="Развить существующий брендбук и разложить много информации так, чтобы её было легко читать.",
        role=["Сделала дизайн сайта, который продолжает и развивает брендбук ДжумПро",
              "Придумала блочную систему, которая структурирует информацию",
              "Сделала яркие иллюстрации, которые передают смысл",
              "Кастомизировала «Потоки» — CMS Tilda, — чтобы команда сама публиковала кейсы и статьи"],
        done_label="что сделала",
        done=["Новый маркетинговый сайт на Tilda",
              "Блочная система и иллюстрации",
              "CMS для кейсов и статей"],
        result=None,
        tags=["редизайн", "tilda"],
    ),
]

GALLERY_DIR = {"segmentstream": "segmentstream", "fraxis": "fraxis", "brs": "brs",
               "vet-workshop": "vet", "bravestone": "bravestone",
               "neon-insights": "neon", "joompro": "joompro"}


# картинки галереи, которые повторяют обложку (обложка и так стоит наверху) — пропускаем
DUPLICATES = {"fraxis": ["g01.jpg"], "brs": ["g05.jpg"], "vet": ["g01.jpg"],
              "bravestone": ["g03.jpg"], "joompro": ["g01.jpg"]}


def gallery(slug):
    d = GALLERY_DIR[slug]
    files = sorted(f for f in os.listdir(os.path.join(ROOT, "assets/img/cases", d))
                   if f.endswith(".jpg") and f not in DUPLICATES.get(d, []))
    return [f"/assets/img/cases/{d}/{f}" for f in files]


MENU = """  <aside class="menu">
    <div class="menu__top">
      <a href="/"><img class="menu__avatar" src="/assets/img/avatar-menu.png" width="40" height="40" alt="На главную"></a>
      <p class="menu__name">Перелыгина Айаана<br><span>Lead Web Designer</span></p>
      <nav class="menu__nav" aria-label="Разделы">
        <a class="pill" href="/#portfolio">портфолио</a>
        <a class="pill" href="/#ai">ai-проекты</a>
        <a class="pill" href="/#experience">опыт</a>
      </nav>
    </div>
    <div class="menu__bottom">
      <p class="menu__meta">Якутск<br>удалённо или релокация</p>
      <a class="btn btn--outline" href="/cv.pdf" download>скачать cv</a>
      <a class="btn btn--dark" href="https://t.me/ayafester" target="_blank" rel="noopener">написать мне в telegram</a>
    </div>
  </aside>"""

# Фото в футере: (файл, подпись). Добавляйте сюда новые страны.
PHOTOS_LIST = [(f"gallery/photo-{i:02d}.jpg", "Якутия") for i in range(1, 11)]


def photos_html(prefix):
    lazy = ' loading="lazy"'
    imgs = "".join(f'<img src="{prefix}assets/img/{f}" alt="{cap}" data-caption="{cap}"{lazy if i else ""}>'
                   for i, (f, cap) in enumerate(PHOTOS_LIST))
    return (f'    <figure class="photo reel" data-interval="2000">\n      {imgs}\n'
            f'      <figcaption class="display">{PHOTOS_LIST[0][1]}</figcaption>\n    </figure>')


PHOTOS = photos_html("/")

FOOTER = f"""    <section class="col footer">
      <ul class="links">
        <li><a href="https://t.me/ayafester" target="_blank" rel="noopener">Telegram</a></li>
        <li><a href="https://www.linkedin.com/in/ayafester/" target="_blank" rel="noopener">LinkedIn</a></li>
        <li><a href="#" data-todo="hh">hh.ru</a></li>
        <li><a href="mailto:ayafester@gmail.com">почта</a></li>
        <li><a href="https://www.instagram.com/ayafester/" target="_blank" rel="noopener">Instagram</a></li>
      </ul>
    </section>

{PHOTOS}"""


def ul(items):
    return "\n".join(f"          <li>{escape(i)}</li>" for i in items)


def page(c, others):
    e = escape
    facts = "\n".join(f'        <div><dt class="label">{e(k)}</dt><dd>{e(v)}</dd></div>' for k, v in c["facts"])
    shots = "\n".join(f'      <img src="{src}" alt="{e(c["title"])} — экран {i}" loading="lazy">'
                      for i, src in enumerate(gallery(c["slug"]), 1))
    more = "\n".join(
        f'''        <a class="more__card" href="/cases/{o["slug"]}.html">
          <img src="/assets/img/{o["cover"]}" alt="" loading="lazy">
          <span class="more__name">{e(o["title"])}</span>
        </a>''' for o in others)
    result = ""
    if c["result"]:
        result = f"""
    <section class="col story">
      <div class="story__item">
        <p class="label">результат</p>
        <p class="story__lead">{e(c["result"])}</p>
      </div>
    </section>
"""
    return f"""<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(c["title"])} — кейс · Перелыгина Айаана</title>
  <meta name="description" content="{e(c["lead"])}">
  <meta property="og:image" content="/assets/img/{c["cover"]}">
  <link rel="icon" href="/assets/img/avatar-menu.png">
  <link rel="preload" href="/assets/fonts/VelaSans-GX.ttf" as="font" type="font/ttf" crossorigin>
  <link rel="preload" href="/assets/fonts/Sexsmith.otf" as="font" type="font/otf" crossorigin>
  <link rel="stylesheet" href="/styles.css">
</head>
<body>
<!-- Сгенерировано tools/build_cases.py — правьте тексты там -->

{MENU}

  <main class="page">

    <section class="col case-hero">
      <a class="back" href="/#portfolio">← на главную</a>
      <h1 class="display case-hero__title">{e(c["title"])}</h1>
      <p class="story__lead">{e(c["lead"])}</p>
      <ul class="tags">{"".join(f"<li>{e(t)}</li>" for t in c["tags"])}</ul>
      <dl class="facts">
{facts}
      </dl>
    </section>

    <img class="case__img" src="/assets/img/{c["cover"]}" alt="{e(c["title"])} — обложка">

    <section class="col story">
      <div class="story__item">
        <p class="label">задача</p>
        <p class="story__lead">{e(c["task"])}</p>
      </div>
      <div class="story__item">
        <p class="label">моя роль</p>
        <ul class="story__list">
{ul(c["role"])}
        </ul>
      </div>
      <div class="story__item">
        <p class="label">{e(c.get("done_label", "что сделали"))}</p>
        <ul class="story__list">
{ul(c["done"])}
        </ul>
      </div>
    </section>

    <div class="shots">
{shots}
    </div>
{result}
    <section class="more">
      <p class="label more__label">ещё кейсы</p>
      <div class="more__grid">
{more}
      </div>
    </section>

{FOOTER}

  </main>

  <script src="/menu.js"></script>
  <script src="/reel.js"></script>
</body>
</html>
"""


def main():
    os.makedirs(os.path.join(ROOT, "cases"), exist_ok=True)
    n = len(CASES)
    for i, c in enumerate(CASES):
        others = [CASES[(i + k) % n] for k in (1, 2, 3)]
        with open(os.path.join(ROOT, "cases", c["slug"] + ".html"), "w", encoding="utf-8") as f:
            f.write(page(c, others))
        print("cases/%s.html  (%d картинок)" % (c["slug"], len(gallery(c["slug"]))))
    update_index_reels()
    update_index_photos()


REEL_FRAMES = 6  # обложка + 5 картинок из галереи
NO_REEL = {"bravestone", "neon-insights", "joompro"}  # маленькие карточки — одна картинка


def update_index_reels():
    """Пересобирает шоурилы на карточках главной: обложка + следующие картинки без повторов."""
    import re
    p = os.path.join(ROOT, "index.html")
    s = open(p, encoding="utf-8").read()
    for c in CASES:
        pat = re.compile(r'<div class="case__img reel"><img src="assets/img/%s" alt="([^"]*)">.*?</div>|<img class="case__img" src="assets/img/%s" alt="([^"]*)" loading="lazy">' % (re.escape(c["cover"]), re.escape(c["cover"])))
        m = pat.search(s)
        if not m:
            print("  нет шоурила на главной для", c["slug"]); continue
        if c["slug"] in NO_REEL:
            s = s[:m.start()] + f'<img class="case__img" src="assets/img/{c["cover"]}" alt="{m.group(1) or m.group(2)}" loading="lazy">' + s[m.end():]
            continue
        frames = [f'<img src="assets/img/{c["cover"]}" alt="{m.group(1) or m.group(2)}">']
        frames += [f'<img src="{src[1:]}" alt="" loading="lazy">' for src in gallery(c["slug"])[:REEL_FRAMES - 1]]
        s = s[:m.start()] + '<div class="case__img reel">' + "".join(frames) + "</div>" + s[m.end():]
    open(p, "w", encoding="utf-8").write(s)
    print("index.html: шоурилы обновлены")



def update_index_photos():
    import re
    p = os.path.join(ROOT, "index.html")
    t = open(p, encoding="utf-8").read()
    t2 = re.sub(r'    <figure class="photo[^"]*".*?</figure>', lambda m: photos_html(""), t, count=1, flags=re.S)
    open(p, "w", encoding="utf-8").write(t2)
    print("index.html: галерея фото обновлена")


if __name__ == "__main__":
    main()
