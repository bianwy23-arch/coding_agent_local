from __future__ import annotations

import sys

from pico.cli import build_agent, build_arg_parser


def main(argv=None):
    parser = build_arg_parser()
    args = parser.parse_args(argv)
    if args.prompt:
        print("pico-tui does not accept one-shot prompts; start the TUI and type there.", file=sys.stderr)
        return 2
    agent = build_agent(args)
    try:
        from pico.tui.app import PicoTuiApp
    except ModuleNotFoundError as exc:
        if exc.name != "textual":
            raise
        print(
            "TUI support requires the optional 'tui' extra. Install with: pip install 'pico[tui]'",
            file=sys.stderr,
        )
        return 1

    PicoTuiApp(agent).run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
