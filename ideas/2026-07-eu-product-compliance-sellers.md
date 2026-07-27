# Проверка гипотезы: товарный комплаенс для продавцов в ЕС (GPSR / EPR / PPWR)

Дата разбора: 2026-07-27
Оценка по [framework.md](../framework.md)
Проверка гипотезы, выдвинутой в [прогоне YC RFS](2026-07-yc-rfs-screening.md) (тема 12)

**Вердикт: 24/40, S4 = 1. Гипотеза не подтвердилась — не брать.**

Что подтвердилось: боль реальна, дедлайны жёсткие, деньги за это уже платят — я угадал
и рынок, и готовность платить. Что не подтвердилось: клин пуст. Он занят десятком мелких
игроков, а часть ядра бесплатно отдаёт сам Amazon.

---

## 1. Что подтвердилось: боль и деньги

Тут я был прав, и цифры лучше, чем ожидал.

**Дедлайны жёсткие, датированные и прямо сейчас:**

- GPSR действует с 13.12.2024. Amazon уже не «предупреждает», а снимает листинги без
  Responsible Person, без документов и с неполной маркировкой.
- Календарь принуждения Amazon 2026: **5 марта** — нельзя заливать новые товары без данных
  производителя; **1 апреля** — существующие без данных начинают уходить в офлайн;
  **июнь** — полное принуждение, листинги гаснут навсегда.
- **PPWR вступает в силу 12 августа 2026** — то есть через две недели. Действует напрямую
  во всех 27 странах, без национальной имплементации и **без переходного периода для
  существующих остатков**. Продавец обязан зарегистрироваться в EPR-системе **каждой**
  страны, где он размещает упакованный товар. «Producer» определён широко и включает
  дистанционных продавцов.
- DPP/ESPR — а вот это пока хайп, а не деньги: делегированный акт по текстилю ожидается
  к концу 2027, обязательность — конец 2028 / середина 2029. Всё, что продаётся сегодня
  под соусом DPP, продаёт будущее.

**Готовность платить доказана деньгами, а не опросами:**

| Услуга | Цена |
|---|---|
| EU Responsible Person (типовая вилка) | €150–500 в год |
| EaseCert, RP | €400 разово (€500 для рисковых категорий) |
| Eldris, RP | £195 разово за страну |
| Euverify, доп. представитель | £200 в год |
| Eldris, EPR под ключ | **от £995 за страну** |
| ekoniq, EPR-подписка на 27 стран | от €29/мес |
| Сами EPR-сборы у среднего продавца | €100–1000 в год |

Это якорь «5» по оси S2 без всяких натяжек: ядро — прямые деньги покупателя, и он их уже
отдаёт.

## 2. Что не подтвердилось: клин занят плотно

### 2.1 Amazon отдаёт проверку состояния бесплатно

У Amazon есть дашборд **Manage Your Compliance** в Seller Central: статус соответствия по
каждому товару, готовые списки ASIN, требующих внимания, история соответствия, **алерты в
реальном времени** и уведомления о недостающих или просроченных документах.

То есть продукт «просканируй мой каталог и покажи, что не соответствует» — уже написан
владельцем платформы и раздаётся даром. Это тот же паттерн, что убил конструктор магазинов
(Яндекс KIT, Ozon) и миграцию с Etsy (Shopify Store Migration). **Третий раз подряд:
владелец платформы бесплатно закрывает ровно ту функцию, вокруг которой я предлагал строить
продукт.**

### 2.2 На клине уже стоит десяток игроков

Нашлись по одному кругу поиска, без специальных усилий:

- **Amazon-сторона**: Listara (проверка документов и GPSR-полей по SKU, бесплатный
  первичный чек), Autron + ComplyGPSR (массовая загрузка и автосабмит в комплаенс-портал
  Amazon), Amazon Listing Audit Tool, Helium 10 Listing Analyzer, SellerEngine, epinium,
  VATai, SpaceGoats, Assortiqo.
- **EPR/RP-сервисы**: Eldris, EaseCert, Euverify, ekoniq, ecosistant, AVASK,
  Deutsche Recycling, Minefield Navigator, Landmark Global.
- **И, самое неприятное, ровно мой продукт**: **EUSeller** — отслеживание EPR-регистраций
  по всем 27 странам ЕС, алерты по дедлайнам, напоминания о квартальной отчётности, модули
  по GPSR, FIC, косметике и PPWR. Это дословно то, что я предложил, уже построенное.
  Рядом **SolidwareTools** (трекер принуждения, дашборд дедлайнов, еженедельное обновление
  из EUR-Lex, изменения в течение 48 часов), **EuroComply**, **RegDossier** (трекер
  дедлайнов ЕС, сверенный с EUR-Lex), **Euverify** (GPSR, CE/UKCA, косметика, медизделия,
  GDPR ст. 27).

### 2.3 Сегмент «свой магазин» тоже закрыт

Моя запасная идея была: у Amazon есть MYC, а у мерчанта на Shopify нет ничего — вот и
дырка, тем более что канал (App Store) закрывает G2 и G4. Проверил: дырки нет. В Shopify
App Store уже висят **GPSR Kit** (профиль безопасности с данными производителя, RP,
предупреждениями, пиктограммами и документами — массово на сотни товаров),
**EU GPSR Compliance Suite Pro**, **GC — GPSR Compliance Dashboard**, **EU GPSR Compliance
Manager**.

Более широкий контекст по категории тоже не в пользу: комплаенс-приложения в Shopify App
Store — это давно сформированный сегмент с бесплатными планами и ценами от $2.99/мес
(Consentmo, Pandectes, Avada, Nova в GDPR-нише). Ценовое дно там уже пробито.

### 2.4 Побочная находка: SP-API стал платным для разработчиков

С **31 января 2026** все сторонние разработчики, интегрированные с Amazon SP-API, платят
годовую подписку плюс ежемесячную плату за объём GET-вызовов. Для продукта, который
регулярно вычитывает чужие каталоги, это переменная себестоимость на юнит, растущая с
размером каталога клиента — прямой удар по G6. Публичные приложения вдобавок требуют
одобрения Amazon и листинга в Selling Partner Appstore.

Само по себе не смертельно, но окончательно снимает тезис «себестоимость копейки».

## 3. Скоринг

| Ось | Балл | Обоснование |
|---|---|---|
| S1 SEO | 4 | Единственная хорошая новость: SERP — мелкие SaaS, консультанты и юрфирмы, гигантов с DR80 нет, long-tail по названиям регламентов и датам бесконечный |
| S2 WTP | 5 | Доказано ценниками выше. Ядро = деньги покупателя |
| S3 Неконсолидированность | 3 | Доминирующего инкумбента нет, «Vanta этого рынка» не существует — рынок реально фрагментирован |
| S4 Конкуренция на клине | **1** | Десяток прямых игроков, включая дословный аналог (EUSeller), плюс бесплатный дашборд самого Amazon. Якорь «1» буквально: «инкумбенты прямо тут» |
| S5 Переиспользование | 3 | Скрейперы под сайты регуляторов и EUR-Lex переиспользуются, но корпус источников надо собирать заново |
| S6 Маржа / LTV:CAC | 3 | Чек хороший и подписка липкая, но SP-API-сборы и ценовое дно в App Store поджимают |
| S7 Моат | 2 | Курируемый корпус источников — нормальный моат, но его уже собрали конкуренты, а я захожу с нуля и позже |
| S8 Скорость до кэша | 3 | Продукт за недели, но органику надо накапливать против тех, кто пишет контент с 2024 года |

**Сумма: 24 / 40.** Формально «серая зона» (20–27), фактически — нет: S4 = 1 при том, что
именно пустота клина была всей причиной заходить. Гипотеза falsified.

## 4. Главный вывод: проблема в источнике идей, а не в идеях

Пять проверок подряд дали один и тот же результат:

| Идея | Итог | Причина |
|---|---|---|
| Конструктор магазинов для селлеров WB | STOP | Оплата и санкционка; ядро бесплатно раздают Яндекс и Ozon |
| Etsy → Shopify, синхронизация | STOP | Etsy не выдаёт API-ключ |
| Etsy → Shopify, разовая миграция | 17/40 | Ядро бесплатно раздаёт Shopify |
| 11 тем YC RFS | STOP | Капитал, железо, команда, лицензии |
| Товарный комплаенс ЕС | 24/40 | Клин занят десятком игроков + бесплатный дашборд Amazon |

Общий знаменатель у всех пяти один: **идея бралась из публично видимого, датированного,
широко обсуждаемого триггера** — исход с WB, комиссии Etsy, дедлайн GPSR, список YC.
А видимый триггер по определению означает, что его увидели все. GPSR действует с декабря
2024 — за двадцать месяцев любой соло-разработчик с теми же навыками успел построить то же
самое, и, как видно из списка выше, десяток их и построил.

Твой фреймворк требует S4 = 5, то есть пустого клина. **Пустой клин и горячая тема —
взаимоисключающие вещи.** Пока источником идей остаются новости, тренды и чужие списки,
результат будет воспроизводиться: боль настоящая, деньги настоящие, место занято.

## 5. Что делать вместо

Менять не идею, а источник. Идея должна приходить оттуда, куда никто не смотрит, а не
оттуда, куда смотрят все:

1. **Собственные активы и собственная операционная боль.** Под что ты писал свои
   Apify-парсеры? Задача, которую ты решал для себя руками, — это ниша, которую по
   определению не видно снаружи, и у неё S5 = 5 сразу.
2. **Кандидаты, которые у тебя уже есть.** В якорях самого фреймворка мелькают
   «ЖКХ-переплата» (S2 = 5, S3 = 5) и «профессии в LinkedIn» (S4 = 5) — то есть у тебя уже
   есть идеи, которым ты сам поставил пятёрки по самым дорогим осям. Прогнать их по
   гейтам полезнее, чем искать шестую новую.
3. **Языковые и гео-ниши.** Все найденные конкуренты в комплаенсе — англоязычные и
   EU-wide. Спрос, у которого нет обслуживания на его языке, — это S4 = 5 без всякой
   новизны продукта.

Конкретно: дай список того, что у тебя уже лежит — активы, парсеры, недоделанные проекты,
идеи с пятёрками. Я прогоню их по фреймворку. Это даст больше, чем ещё один разбор темы
из ленты.

---

## Источники

- [GPSR Requirements for Amazon Sellers 2026](https://eugpsr.eu/blog/gpsr-amazon-sellers)
- [Amazon EU Compliance Guide for Sellers 2026 (Assortiqo)](https://assortiqo.com/compliance/amazon-compliance-guide)
- [GPSR Deadline 2026: What Non-EU Sellers Need to Know (AuraDPP)](https://auradpp.com/blog/gpsr-deadline-2026-what-sellers-need-to-know)
- [New GPSR Requirements: Monitoring Your IDQ and Account Health (SellerEngine)](https://sellerengine.com/new-gspr-requirements-for-amazon-sellers-monitoring-your-idq-and-account-health/)
- [GPSR Amazon: essential compliance guide (Epinium)](https://epinium.com/en/blog/gpsr-amazon-essential-guide-for-sellers/)
- [The new EU Packaging Regulation: Key requirements from August 2026 (Gleiss Lutz)](https://www.gleisslutz.com/en/know-how/new-eu-packaging-regulation-key-requirements-august-2026)
- [EU PPWR requirements effective from August (Intertek)](https://www.intertek.com/products-retail/insight-bulletins/2026/1536-eu-ppwr-requirements-effective-from-august/)
- [PPWR: New Compliance Requirements for E-Commerce (Greenberg Traurig)](https://www.gtlaw.com/en/insights/2025/8/eu-packaging-and-packaging-waste-regulation-new-compliance-requirements-for-e-commerce)
- [GPSR Responsible Person Cost 2026: 5-Provider Price Comparison (Eldris)](https://responsible.eldris.ai/data-centre/eu-responsible-person-compliance/gpsr-responsible-person-cost-breakdown-2026/)
- [EU Responsible Person Cost — GPSR Pricing Guide 2026](https://eugpsr.eu/blog/gpsr-cost-pricing-guide)
- [WEEE Registration & EPR Compliance for Amazon Sellers (Eldris)](https://epr.eldris.ai/)
- [ekoniq — EPR Compliance for Amazon & E-Commerce Sellers](https://ekoniq.eu/)
- [EUSeller — EU compliance tooling for online sellers](https://euseller.com/)
- [SolidwareTools — European compliance software for SMEs](https://solidwaretools.com/)
- [RegDossier — EU Compliance Deadline Tracker 2026-2028](https://regdossier.eu/eu-compliance-deadlines/)
- [Euverify — Regulatory Compliance for EU & UK Product Sellers](https://euverify.com/)
- [Listara — Amazon Compliance Documents by SKU](https://www.listara.eu/en/amazon-compliance-documents)
- [GPSR Kit — Shopify App Store](https://apps.shopify.com/gpsr-kit)
- [EU GPSR Compliance Suite Pro — Shopify App Store](https://apps.shopify.com/eu-gpsr-compliance-suite-pro)
- [GC ‑ GPSR Compliance — Shopify App Store](https://apps.shopify.com/gpsr-compliance-dashboard)
- [Amazon SP-API: изменения для разработчиков с 31 января 2026](https://emagicone.com/important-amazon-sp-api-update-action-required-before-january-31-2026/)
- [SP-API Registration Overview (Amazon)](https://developer-docs.amazon.com/sp-api/docs/sp-api-registration-overview)
- [ESPR / DPP timeline for textiles (Cycle Intelligence)](https://www.cycle-platform.com/knowledge/eu-digital-product-passport-textiles/)
