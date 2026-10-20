# DMW vocabularies

The files behind `https://w3id.org/hisqu/dmw/<vocabulary>`. The redirects are in
`ids/hisqu/.htaccess` of `perma-id/w3id.org`.

| File | Served at | Is |
| --- | --- | --- |
| `process.ttl` | `https://www.hisqu.de/dmw/process.ttl` | the latest release of the DMW process vocabulary (`dmwp:`, `https://w3id.org/hisqu/dmw/process#`) |
| `process/<n>.ttl` | `https://www.hisqu.de/dmw/process/<n>.ttl` | release `<n>` (`owl:versionIRI` `https://w3id.org/hisqu/dmw/process/<n>`) |

Rules:

- Each file is copied byte for byte from a release of the DMW repository
  (`server/src/dmw/content/process/graph/dmw-process.ttl`). It is never edited here.
- A release file never changes after it is published. A new release adds `process/<n>.ttl`
  and replaces `process.ttl` with a copy of it.
- Vocabularies added later (`terms`) follow the same layout.
