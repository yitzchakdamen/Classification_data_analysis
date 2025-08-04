# Classification data analysis

## Data analysis and basic data cleaning system for textual information (anti-Semitic and non-anti-Semitic tweets)

* **DataAnalyzer**
     - classifies into categories, and performs analysis on the file according to categories.

* **DataCleaning**
    - performs cleaning on the file.

* **FileHandling**
    - handles uploading and saving files.

* **ReportBuilder**
    - handles creating a dictionary from several dictionaries.

* **SystemManagement**
    - manages the entire process - uploads a file - analyzes - cleans - and saves.

* **main**
    - calls SystemManagement with the required parameters.


___ Example of an analysis file ___
```
{
    "common_words": {
        "total": [
            ...
        ],
        "antisemitic": [
            ...
        ],
        "non_antisemitic": [
            ...
        ],
        "unspecified": [
            ...
        ]
    },
    "longest_3_tweets": {
        "total": [
            ...,
            ...,
            ...
        ],
        "antisemitic": [
            ...,
            ...,
            ...
        ],
        "non_antisemitic": [
            ...,
            ...,
            ...
        ],
        "unspecified": [
            ...,
            ...,
            ...
        ]
    },
    "total_tweets": {
        "total": 0,
        "antisemitic": 0,
        "non_antisemitic": 0,
        "unspecified": 0
    },
    "average_length": {
        "total": 0,
        "antisemitic": 0,
        "non_antisemitic": 0,
        "unspecified": 0
    },
    "uppercase_words": {
        "total": 0,
        "antisemitic": 0,
        "non_antisemitic": 0,
        "unspecified": 0
    }
}
```