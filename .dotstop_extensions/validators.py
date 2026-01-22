import os
from typing import TypeAlias


yaml: TypeAlias = str | int | float | bool | list["yaml"] | dict[str, "yaml"]


def hello_bin(configuration: dict[str, yaml]) -> tuple[float, list[Exception | Warning]]:
    src = configuration.get('src')
    dest = configuration.get('dest')

    if src is None or dest is None:
        return (0.0, [ValueError('missing src or dest')])

    if not os.path.exists(src):
        return (0.0, [ValueError('missing src')])

    if not os.path.exists(dest):
        return (0.0, [ValueError('missing dest')])

    if os.path.getsize(dest) > 20 * 1024:
        return (0.2, [ValueError('file exceeds expected size')])
    
    return (1.0, [])
