# Django – Individual In-Depth Study

Ett enkelt webbprojekt byggt med **Django** för kursens Individual In-Depth Study. Projektet är en liten prototyp där användaren kan visa, skapa, redigera och ta bort inlägg.

## Kom igång

### 1. Installera beroenden

Installera Django:

```bash
pip install django
```

### 2. Uppdatera databasen

Kör kommandot i terminalen, i samma mapp som `manage.py`:

```bash
python manage.py migrate
```

Det tillämpar projektets befintliga migreringar och skapar eller uppdaterar databasschemat.

Om du har ändrat modeller i `models.py` och behöver skapa nya migreringar kör du först:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Starta servern

```bash
python manage.py runserver
```

Öppna sedan adressen som visas i terminalen, vanligtvis http://127.0.0.1:8000/.

Stoppa servern med `Ctrl+C`.

## Funktioner

- Visa en lista över inlägg.
- Skapa nya inlägg.
- Redigera befintliga inlägg.
- Ta bort inlägg med en bekräftelse.
- Bootstrap används för en enkel och responsiv layout.

## Bra att veta

- Kör kommandona från projektmappen där `manage.py` ligger.
- Databasen och dess inställningar konfigureras i `settings.py`.
- `migrate` tillämpar befintliga migreringar. Om modellerna ändras behöver du normalt köra `makemigrations` först.

## Testdata

`GenerateSeedData.py` skapar 10 testinlägg med olika Lorem Ipsum-texter och slumpmässiga datum från de senaste 30 dagarna.

Kör kommandot från projektmappen där `manage.py` ligger:

```bash
python GenerateSeedData.py
```

Kör det efter att databasen har migrerats. Varje körning skapar 10 nya inlägg, så upprepade körningar ger fler poster.
