# Security Policy

## Supported versions

| Version | Supported |
|---------|-----------|
| 0.5.x   | yes       |
| 0.4.x   | security fixes only |
| < 0.4   | no        |

## Reporting a vulnerability

Email `security@ai-mind-map-generator.dev` with:
- A description of the issue.
- A minimal reproduction.
- The affected version and OS build.

We aim to acknowledge within 72 hours and ship a patch within 14 days
for confirmed issues.

## Scope

In scope: the desktop app, the local HTTP bridge (`mindmap/services/bridge.py`),
the document parsers, and the LLM provider adapters.

Out of scope: third-party LLM provider outages, user-supplied API keys
leaked by the user, and any content the user chooses to feed the parser.

## Hardening notes

- The bridge binds to `127.0.0.1` only. Do not change this without a
  threat-model review.
- Provider API keys are stored via Windows DPAPI through `keyring`.
  Plaintext keys on disk are treated as a bug.
- Imported documents are sandboxed: no macros, no embedded scripts,
  no network fetches during parse.

## Disclaimer

This tool is provided for educational and personal-productivity use.
You are responsible for the documents you feed it and the API keys you
configure. Use at your own risk.