# Datasets and data catalogs 

## Data catalogs

Metadata is published in two different forms: as a dataset index file, or as a data catalog. Catalogs combine the metadata for multiple datasets into one file, with metadata for each dataset included in an array named `datasets`.

## Dataset metadata

The most important piece of metadata for any dataset is its `name`. Names are lowercase, underscore-linked short identifiers (eg. `us_ofac_sdn`) used in the actual entity data to reference a data source. Inside the metadata (or a catalog entry), the following fields can be found:

| **Section**          | **Field**         | **Description**    |
|----------------|---------------|---------------------------|
| `dataset`        |               |  |
|                | `name`          | Dataset’s unique identifier |
|                | `title`         | Human-readable title |
|                | `summary`       | Short summary string |
|                | `description`   | Detailed description of the dataset in markdown syntax |
|                | `tags`          | List of tags assigned to this dataset |
|                | `index_url`     | URL to dataset metadata file |
|                | `version`       | Latest dataset version. Each data update produces a new version ID, and version IDs can be relied on to be sortable strings.  |
|                | `last_change`   | Timestamp when any entity in the dataset last changed. This marks when the system discovered the change, not when published at source. Also note that changes to our data cleaning tools may result in changes reflected here as well. |
|                | `last_export`   | Timestamp of the most recent dataset crawl and export. This is the time of when the process in question was started, not when the resulting data was uploaded to our public archive.  |
|        | `datasets`              | All data sources (and enrichment datasets) included in this collection |
|                | `resources`     | Array of objects describing associated files, including exports and source data.  |
|         | `updated_at`    | Use `last_export` instead. |
| `coverage`       |               | Coverage metadata object. |
|                | `start`         | Date of the first time the dataset was included in the database. |
|                | `countries`     | List of the countries covered by this dataset. |
|                | `frequency`     | One of: `never`, `hourly`, `daily`, `weekly`, `monthly`, `annually` |
|                | `schedule`      | A more precise (cron-style) specification of the update frequency |
| `publisher`      |               |  |
|                | `name`          | Publishing source name  |
|                | `acronym`       | Pubshlishing source acronym (e.g. OFAC) |
|                | `description`   | Detailed description of publishing source, uses markdown. |
|                | `url`           | Link to the publisher's home page |
|                | `country`       | Originating country (code) of publishing source |
|                | `country_label` | Originating country (name) of publishing source |
|                | `official`      | `true` if the publisher is a government or inter-governmental organization. |
| `resources` |                   |                                                        |
|             | `name`            | Identifier for this export                             |
|             | `url`             | Direct download URL where the resource file is fetched |
|             | `checksum`        | SHA1 of the resource contents                          |
|             | `mime_type`       | The MIME type of the resource (eg. text/csv)           |
|             | `mime_type_label` | Human-readable label for the MIME type                 |
|             | `title`           | Title of the resource                                  |
|             | `size`            | Size of the resource in bytes                          |
