from typing import Any
from followthemoney import model, __version__
from followthemoney import registry
from followthemoney.property import Property
from followthemoney.schema import Schema
from followthemoney.types.common import PropertyType


def define_env(env):
    """
    This is the hook for the variables, macros and filters.
    """

    env.variables["model"] = model
    env.variables["registry"] = registry
    env.variables["ftm_version"] = __version__

    @env.macro
    def bool_icon(val: bool) -> str:
        if val:
            return ":material-check:"
        return ":material-close:"

    @env.macro
    def doc_string(val: Any) -> str:
        return val.__doc__ or ""

    @env.macro
    def schema_ref(schema: Schema | str) -> str:
        if isinstance(schema, Schema):
            schema = schema.name
        return f"[`{schema}`](/explorer/schemata/{schema}.md)"

    @env.macro
    def type_ref(type_: PropertyType | str) -> str:
        return f"[`{type_}`](/explorer/types/{type_}.md)"

    @env.macro
    def prop_ref(prop: Property | str) -> str:
        if isinstance(prop, Property):
            schema, name = prop.schema.name, prop.name
        else:
            schema, name = prop.split(":")
        qname = ":".join((schema, name))
        return f"[`{qname}`](/explorer/schemata/{schema}#{name})"

    @env.macro
    def select_schema(name: str) -> Schema:
        s = model.get(name)
        assert s is not None, f"Schema not in model: `{name}`"
        return s

    @env.macro
    def select_type(name: str) -> PropertyType:
        t = registry.get(name)
        assert t is not None, f"Property type not in model: `{name}`"
        return t
