# Journal metadata

Main periodical dataset is [ISSN](https://www.issn.org/), as of 2023-12-03 there are
[2337362](https://github.com/miku/issnlister) registered ISSN, of which a
fraction is scientific and accessible online.

## Sources

Each source may have a different format, distribution mechanism or update interval.

* [ ] LOCKSS
* [ ] CLOCKSS
* [ ] Portico
* [ ] JSTOR
* [ ] PKP-PLN
* [ ] ISSN-L
* [ ] Entrez
* [ ] DOAJ
* [ ] Crossref
* [ ] ROAD
* [ ] Sherpa
* [ ] Norwegian
* [ ] Scielo
* [ ] Hathitrust
* [ ] Scholarsportal
* [ ] Cariniana
* [ ] Szczepanski
* [ ] EZB
* [ ] ZDB
* [ ] ZDB-FIZE
* [ ] Gold-OA
* [ ] Wikidata
* [ ] Openapc
* [ ] SIM
* [ ] ManualHomepage
* [ ] VanishedDisappeared
* [ ] VanishedInactive
* [ ] AustralianERA
* [ ] AWOL
* [ ] MAG
* [ ] OpenAlex
* [ ] Wiley

## Bits of interest

In general, per container metadata like title, publisher, publication time
spans, open access (OA) status. OA status may differ within a single journal.

## KBART

> [Knowledge Base And Related
> Tools](https://www.niso.org/standards-committees/kbart), example file:
> [wiley_fullcollection_2024_2023-11-01-1700488387777.TXT](static/wiley_fullcollection_2024_2023-11-01-1700488387777.TXT)

Example columns (may vary):

```
$ head -1 wiley_fullcollection_2024_2023-11-01.TXT  | tr '\t' '\n' | cat -n
     1  publication_title
     2  print_identifier
     3  online_identifier
     4  date_first_issue_online
     5  num_first_vol_online
     6  num_first_issue_online
     7  date_last_issue_online
     8  num_last_vol_online
     9  num_last_issue_online
    10  title_url
    11  first_author
    12  title_id
    13  embargo_info
    14  coverage_depth
    15  notes
    16  publisher_name
    17  publication_type
    18  date_monograph_published_print
    19  date_monograph_published_online
    20  monograph_volume
    21  monograph_edition
    22  first_editor
    23  parent_publication_title_id
    24  preceding_publication_title_id
    25  access_type
    26  OCLC_Control_Number
    27  additional_notes
```
