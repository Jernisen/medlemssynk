# medlemssynk

Lokalt verktyg för att jämföra en förenings medlemsregister i **Wondr** med
registret i **IdrottOnline** (och framöver Idrottsarenan), hitta avvikelser och
bygga en importfil som laddas upp manuellt.

Körs helt lokalt. Inga nätverksanrop, inga molntjänster.

## Vad verktyget gör

Tar två exporter:

- `data/wondr.csv` – export från Wondrs migrationsverktyg
- `data/idrottonline.xlsx` – export från IdrottOnline (Administration → Personer → Exportera)

och skriver till `out/`:

| Fil | Innehåll |
|---|---|
| `saknar_personnummer.xlsx` | Personer utan fullständigt 12-siffrigt personnummer |
| `nya_i_wondr.xlsx` | Aktiva i Wondr som saknas i IdrottOnline |
| `saknas_i_wondr.xlsx` | Finns i IdrottOnline men inte (aktiva) i Wondr |
| `avvikelser.xlsx` | Matchade personer med olika kontaktuppgifter |
| `import_YYYY-MM-DD.xlsx` | Importfil i IdrottOnlines mallformat |
| `rapport.txt` | Sammanfattning av körningen |

## Personuppgifter

Både indata och utdata innehåller personuppgifter (namn, personnummer,
kontaktuppgifter). Därför:

- `data/` och `out/` ignoreras av git. Committa aldrig en datafil.
- Wondr-exporten innehåller dessutom betalkortstokens och autogirouppgifter.
  Verktyget läser aldrig in de kolumnerna – men filen i sig ska raderas så fort
  körningen är klar.
- Kör på krypterad disk. Skicka aldrig filerna via e-post.
- En pre-commit-hook som stoppar personnummer finns i `hooks/`, se nedan.

## Installation

```sh
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cp config.example.toml config.local.toml   # redigera sedan
git config core.hooksPath hooks            # aktivera pre-commit-spärren
```

## Körning

```sh
medlemssynk --config config.local.toml
```

## Licens

MIT, se `LICENSE`.
