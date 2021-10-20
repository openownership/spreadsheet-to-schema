# Spreadsheet to schema

Tool for converting a spreadsheet (a csv file) in a specific format to jsonschema.

## Installation

```pip install spreadsheet-to-schema```

## Usage 

The following will print out the JSONSchema generated by the CSV file:

```spreadsheet-to-schema myfile.csv```

To save to a file:

```spreadsheet-to-schema myfile.csv > output.json```

If you want merge the output schema to an existing JSONSchema file:

```spreadsheet-to-schema myfile.csv -s myschema.json```

## Spreadsheet Format

The spreadheet should look something like the following:

|path                |title      |description           |type  |
|--------------------|-----------|----------------------|------|
|                    |rootobj    |myrootdescription     |object|
|p.myobject          |myobejct   |mydescription         |object|
|p.mystring          |mytitle2   |mydescription2        |string|
|myobject.p.substring|mysubstring|mysubstringdescription|object|


This will represent JSONSchema

```
{
  "type": "object",
  "title": "rootobj",
  "description": "myrootdescription",
  "properties": {
    "myobject": {
      "type": "object",
      "title": "myobejct",
      "description": "mydescription"
    },
    "mystring": {
      "type": "string",
      "title": "mytitle2",
      "description": "mydescription2"
    }
  },
  "myobject": {
    "properties": {
      "substring": {
        "type": "object",
        "title": "mysubstring",
        "description": "mysubstringdescription"
      }
    }
  }
}
```

### The Path 

The path heading is required in the spreadsheet; all other headings are optional.

The path specifies where the JSONSchema object should exist and the other headings say what JSONSchema properties live at that path.

An empty path represents the root of the JSONSchmema object. It will typically be of type `object` and contain properties.

The path is seperated by `.` seperators. Each `.` represents a new sub object in the JSON. 

There are some shortcuts to common parts of the path within JSONSchema:

* `p` can be used inplace of `properties`.
* `d` can be used inplace of `definitions`.
* `i` can be used inplace of `items`.


### Columns in the CSV

Each column needs a heading. The following headings are supported:

* `type`: type filed in JSONSchemad e.g object, string, array
* `title`: title field
* `format`: format field
* `description`: description field
* `codelist`: name of codelist file (not in JSONSchema spec)
* `enum`: comma seperated list of enum values
* `required`: comma seperated of required fields
* `minItems`: minItems field
* `minProperties`: minItems field
* `ref`: ref field

## Examples

* [CSV from example above](https://github.com/openownership/spreadsheet-to-schema/blob/main/examples/readme-basic.csv)
* [Full featured Example CSV](https://github.com/openownership/spreadsheet-to-schema/blob/main/examples/full-example.csv) - [Full featured Example JSON output](https://github.com/openownership/spreadsheet-to-schema/blob/main/examples/full-example.json)
