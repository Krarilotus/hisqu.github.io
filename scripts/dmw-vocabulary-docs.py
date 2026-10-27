# /// script
# requires-python = ">=3.11"
# dependencies = ["pylode==3.6.0", "kurra==3.0.5"]
# ///
"""Generate the HTML documentation of a DMW vocabulary release with pyLODE.

Usage: uv run scripts/dmw-vocabulary-docs.py public/dmw/process/2.ttl public/dmw/process/2.html

The Turtle file is the release and is never changed. pyLODE has no language choice and
picks any one of a term's labels, so the page is generated from a copy that keeps only the
English label or comment wherever a term has one in several languages.
"""

import sys
from pathlib import Path

from pylode import OntPub
from rdflib import Graph, Literal

DOCUMENTATION_LANGUAGE = "en"


def english_only(graph: Graph) -> Graph:
    for subject, predicate in set(graph.subject_predicates()):
        values = list(graph.objects(subject, predicate))
        languages = {value.language for value in values if isinstance(value, Literal)}
        if DOCUMENTATION_LANGUAGE not in languages:
            continue
        for value in values:
            if isinstance(value, Literal) and value.language not in (None, DOCUMENTATION_LANGUAGE):
                graph.remove((subject, predicate, value))
    return graph


def main(release_ttl: Path, page_html: Path) -> None:
    graph = english_only(Graph().parse(release_ttl, format="turtle"))
    html = OntPub(graph.serialize(format="turtle"), sort_subjects=True).make_html()
    page_html.write_bytes(html.replace("\r\n", "\n").encode("utf-8"))


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]))
