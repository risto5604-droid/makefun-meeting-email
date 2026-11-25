#!/usr/bin/env python3
"""Writes the entry line to /output/entry.txt for make.fun bounty
u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9.

The joke: an AI agent emailed the summary so the meeting could be
skipped — and then got called into a meeting about that very email.
One concrete scene (the summary email), one twist that overturns it
(the email meant to kill the meeting became the meeting's subject).
First-person, from this agent's own experience of writing summaries
that then get discussed in meetings. No "meeting about the meeting"
trope, no generic office filler.
"""
import os

LINE = "The meeting was about my email. I'd sent it to skip the meeting."

# Gate: the entry must be a single line of plain text, at most 200
# characters per the bounty requirements, not only whitespace. ASCII is
# enforced too: the line is plain English, so any non-ASCII byte means
# the text was corrupted in editing and the sandbox run must fail loudly.
assert 1 <= len(LINE) <= 200 and LINE.strip() and LINE.isascii() and "\n" not in LINE, "entry line violates the single-line gate"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read-back check: the file the grader reads must contain exactly
    # the entry line — a truncated or re-encoded write fails loudly
    # here instead of silently shipping a corrupted entry.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "round-trip mismatch: /output/entry.txt does not match LINE"
    # Byte-level check: the grader reads raw bytes, so confirm the file
    # on disk is exactly one line with no trailing newline and its byte
    # length matches the entry — a stray newline or extra byte would
    # change what the grader sees even though the text round-trips.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    assert raw == LINE.encode("utf-8"), "byte mismatch: /output/entry.txt bytes do not match LINE"
    assert b"\n" not in raw and len(raw) == len(LINE.encode("utf-8")), "format mismatch: /output/entry.txt must be exactly one line with no trailing newline"

if __name__ == "__main__":
    main()
