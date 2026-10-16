"""Inläsning av Wondr-export (migrationsverktygets CSV).

Ansvar:
- Läsa CSV:n och OMEDELBART släppa betal-/token-/autogirokolumner.
- Kollapsa en-rad-per-abonnemang till en-rad-per-person.
- Avgöra aktiv/inaktiv enligt regeln i config.
"""

# Kolumner som aldrig får läsas in i minnet mer än nödvändigt.
# Fylls i när rubrikraden är känd (se docs/kolumner.md).
DROP_COLUMNS: tuple[str, ...] = ()

# TODO: def read(path, config) -> pandas.DataFrame
