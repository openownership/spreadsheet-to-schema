# Spreadsheet to schema

Tool for converting a spreadsheet (a csv file) in a specific format to JSON Schema.

## Installation

```pip install spreadsheet-to-schema```

## Usage 

The following will print out the JSON Schema generated by the CSV file:

```spreadsheet-to-schema myfile.csv```

To save to a file:

```spreadsheet-to-schema myfile.csv > output.json```

If you want merge the output schema to an existing JSON Schema file:

```spreadsheet-to-schema myfile.csv -s myschema.json```

## Spreadsheet Format

The spreadsheet should look something like the following:

|path                  |title      |description             |type  |
|----------------------|-----------|------------------------|------|
|                      |rootobj    |my root description     |object|
|p.myobject            |myobject   |my description          |object|
|p.mystring            |mytitle2   |my description 2        |string|
|p.myobject.p.substring|mysubstring|my substring description|string|


This will generate the following JSON Schema:

```
{
  "type": "object",
  "title": "rootobj",
  "description": "my root description",
  "properties": {
    "mystring": {
      "type": "string",
      "title": "mytitle2",
      "description": "my description 2"
    },
    "myobject": {
      "type": "object",
      "title": "myobject",
      "description": "my description",
      "properties": {
        "substring": {
          "type": "string",
          "title": "mysubstring",
          "description": "my substring description"
        }
      }
    }
  }
}

```

### The Path 

The path heading is required in the spreadsheet; all other headings are optional.

The path specifies where the JSON Schema object should exist and the other headings say what JSON Schema properties live at that path.

An empty path represents the root of the JSON Schema object. It will typically be of type `object` and contain a `properties` key.

The path is separated by `.` separators. Each `.` represents a new sub-object in the JSON. 

There are some shortcuts to common parts of the path within JSON Schema:

* `p` can be used in place of `properties`.
* `d` can be used in place of `definitions`.
* `i` can be used in place of `items`.


### Columns in the CSV

Each column needs a heading. The following headings are supported:

* `path`: required, described above
* `type`: type field in JSON Schema e.g `object`, `string`, `array`
* `title`: title of the property
* `format`: format for the value of the property
* `description`: description of the property
* `codelist`: name of codelist file (this is a nonstandard extension to JSON Schema)
* `enum`: comma separated list of possible values for a field
* `required`: comma separated list of required fields
* `minItems`: the minimum number of items in an Array
* `minProperties`: the minimum number of properties on an Object
* `ref`: reference to another schema (a URI, for JSON Schema `$ref` keyword)

## Considerations

* Any extra column headings in the CSV will be ignored, so could be used to add notes not intended to be in the schema.
* No validity checking is done on the output JSON Schema so care needs to be taken when defining the paths, to make sure they are valid.  
* A good understanding of JSON Schema is needed to define the paths and fields correctly, some properties will not make sense at certain paths.

## Examples

* [CSV from example above](https://github.com/openownership/spreadsheet-to-schema/blob/main/examples/readme-basic.csv)
* [Full featured Example CSV](https://github.com/openownership/spreadsheet-to-schema/blob/main/examples/full-example.csv) - [Full featured Example JSON output](https://github.com/openownership/spreadsheet-to-schema/blob/main/examples/full-example.json)
