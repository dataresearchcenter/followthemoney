{% set type = select_type('phone') %}
# {{ type.plural }}

{% include 'templates/type.md' %}


## Python API

Validation and normalisation of URLs is performed by the functions in [rigour.urls][].

::: followthemoney.types.UrlType
    options:
        heading_level: 3