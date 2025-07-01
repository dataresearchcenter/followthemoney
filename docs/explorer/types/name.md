{% set type = select_type('name') %}
# {{ type.plural }}

{% include 'templates/type.md' %}

## Python API

::: followthemoney.types.NameType
    options:
        heading_level: 3
