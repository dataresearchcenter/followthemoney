{% set type = select_type('url') %}
# {{ type.plural }}

Text URL property type is used for link references. Only the schemes `http`, `https`, `ftp`, and `mailto` are supported.

Validation and normalisation of URLs is performed by the functions in [rigour.urls][].

{% include 'templates/type.md' %}

## Python API

::: followthemoney.types.UrlType