import pathlib
import typing as t

import structlog

log = structlog.get_logger()


def read_file(path: pathlib.Path) -> str:
    with open(path) as f:
        return f.read()


def write_file(path: pathlib.Path, content: t.Any) -> None:
    with open(path, "w") as f:
        f.write(content)
    log.debug("Successfully saved file:\n", file=path)
