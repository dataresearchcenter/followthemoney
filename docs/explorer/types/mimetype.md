{% set type = select_type('mimetype') %}
# {{ type.plural }}

{% include 'templates/type.md' %}
