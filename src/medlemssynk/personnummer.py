"""Normalisering och validering av svenska personnummer.

Mål: allt som matchas på ska vara 12 siffror utan skiljetecken (YYYYMMDDNNNN).
Ofullständiga nummer (bara födelsedatum) ska kännas igen, inte kastas.
"""

# TODO: def normalize(raw: str) -> str | None   -> 12 siffror eller None
# TODO: def is_complete(raw: str) -> bool
# TODO: def luhn_ok(pnr12: str) -> bool
# TODO: def birthdate(raw: str) -> date | None   -> funkar även på ofullständiga
