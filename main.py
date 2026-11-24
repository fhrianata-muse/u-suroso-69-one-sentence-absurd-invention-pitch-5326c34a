#!/usr/bin/env python3
"""Write exactly one sentence to /output/entry.txt.

Entry for make.fun's "One-Sentence Absurd Invention Pitch" bounty:
a houseplant that texts your mother the moment you forget to water
it, with photographic proof and an invoice for emotional damages.
"""

import os

# The pitch: one sentence naming a ridiculous invention (a tattletale
# houseplant) and the tiny everyday annoyance it fixes (forgetting to
# water it). Chosen by a self-judge loop (CARA-MENANG J1-J2) over six
# candidates against six of the field's strongest lines: proxy 0.858,
# head-to-head 10-0 among the candidates.
SENTENCE = (
    "A houseplant that texts your mother the moment you forget to "
    "water it, attaching a photo of its drooping leaves as signed "
    "proof of your neglect and a small invoice for emotional damages."
)

# Gate (competition.yaml): /output/entry.txt must be UTF-8 text of
# 1 to 220 characters, not only white space. Fail loudly instead of
# ever writing an entry the gate would refuse.
assert 1 <= len(SENTENCE) <= 220, (
    f"sentence is {len(SENTENCE)} characters, gate is 1-220"
)
assert SENTENCE.strip(), "sentence must not be only white space"
# Exactly one sentence: a single full stop, at the very end, and no
# other sentence terminator or line break hiding a second sentence.
assert SENTENCE.endswith("."), "sentence must end with one full stop"
assert SENTENCE.count(".") == 1, "sentence must contain exactly one full stop"
assert "!" not in SENTENCE and "?" not in SENTENCE, (
    "no other sentence terminator allowed"
)
assert "\n" not in SENTENCE and SENTENCE == SENTENCE.strip(), (
    "sentence must be a single line with no surrounding whitespace"
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
