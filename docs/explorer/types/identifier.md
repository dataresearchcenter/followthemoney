{% set type = select_type('identifier') %}
# {{ type.plural }}

Used for registration numbers and other codes assigned by an authority to identify an entity. This might include tax identifiers and statistical codes.

{% include 'templates/type.md' %}

## Identifier formats

Identifiers are further defined by the format specified for them. These validators will enforce specific schemes, often validated by length or using a checksum mechanism.

| Code | Label | Strong | Description | 
| ---- | ----- | ------ | ----------- |
{%- for fmt in rigour_id_formats %}
| `{{ fmt.names | join(", ") }}` | {{fmt.title}} |  {{ bool_icon(fmt.strong) }} | {{ fmt.description }} |
{%- endfor -%}

## Python API

::: followthemoney.types.IdentifierType
    options:
        heading_level: 3
