"""Matchning mellan Wondr- och IdrottOnline-register.

Primär nyckel: fullständigt personnummer.
Sekundär nyckel (för att hitta ofullständiga poster): normaliserat namn + födelsedatum.

Resultatet är fyra mängder:
- saknar_personnummer
- nya_i_wondr
- saknas_i_wondr
- avvikelser
"""

# TODO: def match(wondr_df, iol_df, config) -> MatchResult
