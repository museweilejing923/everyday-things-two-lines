"""Write the entry text to /output/entry.txt. Deterministic: no network, no randomness, no clock."""
import os
import sys
# The entry text: two lines explaining a toaster to a 10-year-old, then why the analogy works.
ENTRY_TEXT = "A toaster is like a little sunbed for bread: your slice lies under glowing hot wires until it turns golden brown.\nThe analogy works because both use heat and time to change colour, but it leaves out that bread cannot get up when it wants — the toaster decides when it is done."
MAX_ENTRY_CHARS = 400


def _fail(msg):
    print("error: " + msg, file=sys.stderr)
    raise SystemExit(1)


def validate(t):
    if not t.strip():
        _fail("entry text must not be blank")
    if not any(c.isalpha() for c in t):
        _fail("entry text must contain at least one letter")
    if t.strip().isdigit():
        _fail("entry text must not be only digits")
    if len(t) > MAX_ENTRY_CHARS:
        _fail(f"entry text is {len(t)} characters, over the {MAX_ENTRY_CHARS} character limit")
    try:
        t.encode("utf-8")
    except UnicodeEncodeError as e:
        _fail(f"entry text is not valid UTF-8: {e}")


def main():
    validate(ENTRY_TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
