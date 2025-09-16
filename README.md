# langChain_structured_output

In LangChain, structured output refers to the practice of having language models return
responses in a well-defined data format (for example, JSON), rather than free-form text. This
makes the model output easier to parse and work with programmatically.


## Why do we need Structured Output: 
Data Extraction
API building
Agents

## TypedDict
TypedDict is a way to define a dictionary in Python where you specify what keys and values
should exist. It helps ensure that your dictionary follows a specific structure.
### Why use TypedDict?
It tells Python what keys are required and what types of values they should have.
It does not validate data at runtime (it just helps with type hints for better coding).

-> simple TypedDict

-> Annotated TypedDict

-> Literal

-> More complex 

-> with pros and cons

## Pydantic
Pydantic is a data validation and data parsing library for Python. It ensures that the data you
work with is correct, structured, and type-safe.

Basic example:

Default values

Optional fields

Coerce

Builtin validation

Field Function -> default values, constraints, description, regex
expressions

Returns pydantic object -> convert to json/dict


## When to use what?

### Use TypedDict if:

You only need type hints (basic structure enforcement).

You don't need validation (e.g., checking numbers are positive).

You trust the LLM to return correct data.


### Use Pydantic if:

You need data validation (e.g., sentiment must be "positive", "neutral", or "negative").

You need default values if the LLM misses fields.

You want automatic type conversion (e.g., "100"->100).


### Use JSON Schema if:

You don't want to import extra Pythen libraries (Pydantic)

You need validation but don't need Python objects.

You want to define structure in a standard JSON format.


