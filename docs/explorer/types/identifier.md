{% set type = select_type('identifier') %}
# {{ type.plural }}

{% include 'templates/type.md' %}

## Python API

::: followthemoney.types.IdentifierType
    options:
        heading_level: 3
