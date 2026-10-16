"""Kommandoradsgränssnitt. `medlemssynk --config config.local.toml`."""

from __future__ import annotations

import argparse
import sys


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="medlemssynk")
    parser.add_argument("--config", default="config.local.toml")
    args = parser.parse_args(argv)

    # TODO: läs config, kör wondr.read -> idrottonline.read -> match -> report
    print(f"medlemssynk: inget implementerat än (config: {args.config})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
