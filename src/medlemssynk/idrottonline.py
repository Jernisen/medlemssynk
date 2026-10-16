"""Inläsning av IdrottOnline-export och skrivning av IdrottOnline-importfil.

Ansvar:
- Läsa exporten (Administration -> Personer -> Exportera till Excel).
- Skriva importfil med exakt de kolumnnamn IdrottOnlines mall använder.

Kolumnnamnen i mallen fylls i när mallen är nedladdad (se docs/kolumner.md).
"""

IMPORT_TEMPLATE_COLUMNS: tuple[str, ...] = ()

# TODO: def read(path) -> pandas.DataFrame
# TODO: def write_import(df, path) -> None
