{% set type = select_type('email') %}
# {{ type.plural }}

{% include 'templates/type.md' %}
