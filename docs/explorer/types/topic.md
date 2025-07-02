{% set type = select_type('topic') %}
# {{ type.plural }}

Topics are descriptive qualifiers for entities. They can be used to say things like *this {{ schema_ref('Company') }} is a bank*, or *this {{ schema_ref('Person') }} is a politician*, or *this {{ schema_ref('Position') }} is a political office on a sub-national level of government*.

Some topics imply a risk association of an entity (eg. `sanction`, `wanted`, `crime.war`), while others act as a purely descriptive taxonomy of the business and geopolitical world.

Besides the informative value, topics are ultimately supposed to bear fruits in the context of graph-based data analysis, where they would enable queries such as *find all paths between a government procurement award and a politician*.

{% include 'templates/type.md' %}

## Data reference

| Code | Label |
| ---- | ----- |
{%- for code, label in select_type('topic').names.items() %}
| `{{code}}` | {{label}} |
{%- endfor -%}


## Python API

::: followthemoney.types.TopicType
    options:
        heading_level: 3
