#!/usr/bin/env python3
"""Convert a STAR-CCM+ case file to VTU format.

This script expects a STAR-CCM+ exported case file, typically with a
``.cas`` extension (compatible with Ansys Fluent).  The conversion uses
``meshio`` which must be installed separately.

Usage::

    python starccm_case_to_vtu.py input.cas output.vtu
"""
import sys

try:
    import meshio
except ImportError as exc:  # pragma: no cover - meshio might be absent
    raise SystemExit("meshio is required to run this script: {}".format(exc))


def convert(case_file: str, vtu_file: str) -> None:
    """Read *case_file* and write the mesh to *vtu_file*."""
    mesh = meshio.read(case_file)
    meshio.write(vtu_file, mesh)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: starccm_case_to_vtu.py <input.cas> <output.vtu>")
        sys.exit(1)
    convert(sys.argv[1], sys.argv[2])
