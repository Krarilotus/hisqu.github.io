# DMW vocabularies

The files behind `https://w3id.org/hisqu/dmw/<vocabulary>`. The redirects are in
`ids/hisqu/.htaccess` of `perma-id/w3id.org`: a client asking for `text/turtle` gets the
Turtle file, everyone else the HTML documentation.

| File | Served at | Is |
| --- | --- | --- |
| `process.ttl` | `https://www.hisqu.de/dmw/process.ttl` | the latest release of the DMW process vocabulary (`dmwp:`, `https://w3id.org/hisqu/dmw/process#`) |
| `process/index.html` | `https://www.hisqu.de/dmw/process/` | its documentation |
| `process/<n>.ttl` | `https://www.hisqu.de/dmw/process/<n>.ttl` | release `<n>` (`owl:versionIRI` `https://w3id.org/hisqu/dmw/process/<n>`) |
| `process/<n>.html` | `https://www.hisqu.de/dmw/process/<n>.html` | the documentation of release `<n>` |

## Releases of the process vocabulary

| Release | `owl:versionInfo` | From DMW commit | Changes |
| --- | --- | --- | --- |
| [1](https://w3id.org/hisqu/dmw/process/1) | `dmw-process@1` | `91b3de4c` | First release: process items and their versions, Workflows, steps, ports, roles, bindings, libraries and projects, aligned with PROV-O, P-Plan, wfdesc and schema.org. |

## How to cite

Cite the release you used by its version IRI, for example:

> DMW process vocabulary, release 1 (`dmw-process@1`). HisQu project, 2026.
> https://w3id.org/hisqu/dmw/process/1

In RDF, name the terms by the namespace `https://w3id.org/hisqu/dmw/process#`, which stays
the same across releases, and the release by its version IRI, for example with
`dcterms:conformsTo <https://w3id.org/hisqu/dmw/process/1>`.

## Rules

- Each Turtle file is copied byte for byte from a release of the DMW repository
  (`server/src/dmw/content/process/graph/dmw-process.ttl`). It is never edited here.
- A release file never changes after it is published. A new release adds `process/<n>.ttl`
  and replaces `process.ttl` with a copy of it.
- Each HTML file is generated from its Turtle file with pyLODE, never edited by hand:
  `uv run scripts/dmw-vocabulary-docs.py public/dmw/process/<n>.ttl public/dmw/process/<n>.html`.
  `process/index.html` is a copy of the latest release's page.
- Vocabularies added later (`terms`) follow the same layout.
