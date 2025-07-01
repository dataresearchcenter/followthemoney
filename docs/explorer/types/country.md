{% set type = select_type('country') %}
# {{ type.plural }}

{% include 'templates/type.md' %}

## Territories

This table lists the full set of geographic territories described in `rigour`. A subset of them are currently supported as property values in FtM, with the rest being mapped to existing country codes as stated here. `rigour` also provides alternate codes and Wikidata QIDs for some territories, expanding the ability to import data from unconventional sources.

| Code | Label | FtM | Country | Jurisdiction | Historical | Wikidata |
| ---- | ----- | --- | ------- | ------------ | ---------- | -------- |
{%- for terr in rigour_territories %}
| `{{terr.code}}` | {{terr.name}} | `{{ terr.ftm_country }}` | {{ bool_icon(terr.is_country) }} | {{ bool_icon(terr.is_jurisdiction) }} | {{ bool_icon(terr.is_historical) }} | [`{{ terr.qid }}`](https://www.wikidata.org/wiki/{{terr.qid}}) |
{%- endfor -%}

## Python API

::: followthemoney.types.CountryType
    options:
        heading_level: 3