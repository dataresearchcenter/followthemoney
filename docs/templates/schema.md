{% set schema = select_schema(page.title) %}

# {{ schema.label }}

{{ schema.description }}

## Inheritance

``` mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
  {% for s in schema.extends %}
  {{ s.name }} <-- {{ schema.name }}
  {% for se in s.extends %}
  {{ se.name }} <-- {{ s.name }}
  {% for sse in se.extends %}
  {{ sse.name }} <-- {{ se.name }}
  {% endfor %}
  {% endfor %}
  {% endfor %}
  {% for s in schema.descendants %}
  {{ schema.name }} <-- {{ s.name }}
  {% endfor %}
```

{% if schema.extends %}
### Extends
{% for s in schema.extends %}
- {{ schema_ref(s) }}
{% endfor %}
{% endif %}

{% if schema.descendants %}
### Descendants
{% for s in schema.descendants %}
- {{ schema_ref(s) }}
{% endfor %}
{% endif %}

{% if schema.matchable_schemata | length > 1 %}
### Matchable with
{% for s in schema.matchable_schemata %}
{% if s.name != schema.name %}- {{ schema_ref(s) }}{% endif %}
{% endfor %}
{% endif %}

## Info

<div class="grid cards" markdown>

- {{ bool_icon(schema.abstract )}} __Abstract__ Abstract schemata are used for inheritance only and shouldn’t be used directly.
- {{ bool_icon(schema.generated )}} __Generated__ Entities using a generated schema shouldn’t be created directly by users.
- {{ bool_icon(schema.matchable )}} __Matchable__ Entities using a matchable schema can be used for matching and cross-referencing.
- {{ bool_icon(schema.hidden )}} __Hidden__ Entities using a hidden schema shouldn’t be displayed in user interfaces or created by users.

</div>


## Semantics

FollowTheMoney has well-defined semantics for different representations of
entities, for example in a network graph or in a timeline.

- In a network graph, entities should be represented as a vertex.

## Properties

| Name | Label | Description | Type |
| ---- | ----- | ----------- | ---- |
{% for prop in schema.properties.values() %}| {{ prop_ref(prop) }}{ #{{ prop.name }} } | {{ prop.label }} | {{ prop.description or '' }} | {{ type_ref(prop.type) }} |
{% endfor %}

