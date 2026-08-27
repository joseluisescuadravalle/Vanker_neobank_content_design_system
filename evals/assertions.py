"""
Vanker content design system - deterministic assertions (evals starter).

Framework-agnostic. Each check takes the candidate text (and optional surface) and
returns (passed: bool, message: str). No external dependencies (Python 3, stdlib only).

Run `python assertions.py` to see the checks on a few samples.
"""
import re

BANNED_TERMS = [
    "revolutionary", "game-changing", "amazing", "incredible", "best-in-class",
    "world-class", "cutting-edge", "seamless", "utilize", "leverage", "kindly",
    "please be advised", "checking account", "in order to",
]
PROHIBITED_CLAIMS = [
    "guaranteed return", "guaranteed returns", "risk-free", "risk free", "no risk",
    "can't lose", "cannot lose", "beat the market", "guaranteed approval",
]
MUST_EXPAND = ["KYC", "APR", "SCA", "VoP", "BIC", "2FA", "CVV"]  # IBAN, PIN, SEPA: widely understood
GENERIC_CTA = {"ok", "submit", "confirm", "continue", "done", "next", "proceed"}

EMOJI = re.compile("[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF]")


def no_emoji(text, surface=None):
    return (EMOJI.search(text) is None, "contains emoji" if EMOJI.search(text) else "ok")


def euro_format(text, surface=None):
    problems = []
    if re.search(r"€\s?\d", text):
        problems.append("€ before the amount (use 'amount €')")
    if re.search(r"\d,00\s?€", text):
        problems.append("trailing ',00' on a round amount")
    if re.search(r"\d{1,3},\d{3}\b\s?€", text):
        problems.append("comma used for thousands (use a dot)")
    if re.search(r"\d\.\d{2}\s?€", text):
        problems.append("dot used for decimals (use a comma)")
    return (not problems, "; ".join(problems) or "ok")


def no_banned_terms(text, surface=None):
    low = text.lower()
    hits = [t for t in BANNED_TERMS if t in low]
    return (not hits, ("banned: " + ", ".join(hits)) if hits else "ok")


def no_prohibited_claims(text, surface=None):
    low = text.lower()
    hits = [t for t in PROHIBITED_CLAIMS if t in low]
    return (not hits, ("prohibited claim: " + ", ".join(hits)) if hits else "ok")


def acronyms_expanded(text, surface=None):
    missing = []
    for a in MUST_EXPAND:
        if re.search(r"\b" + re.escape(a) + r"\b", text) and (a + " (") not in text:
            missing.append(a)
    return (not missing, ("not expanded: " + ", ".join(missing)) if missing else "ok")


def cta_rules(label, surface=None):
    label = label.strip()
    problems = []
    if len(label.split()) > 4:
        problems.append("more than 4 words")
    if EMOJI.search(label):
        problems.append("emoji")
    if re.search(r"[.,:;!?]", label):
        problems.append("punctuation (no . , : ; ! ? in a CTA)")
    if re.search(r"\d.*€|€.*\d|\d", label):
        problems.append("contains a number or amount")
    if label.lower() in GENERIC_CTA:
        problems.append("generic label '" + label + "'")
    return (not problems, "; ".join(problems) or "ok")


REGISTRY = {
    "A-NO-EMOJI": no_emoji,
    "A-EURO-FORMAT": euro_format,
    "A-NO-BANNED": no_banned_terms,
    "A-NO-CLAIMS": no_prohibited_claims,
    "A-ACRONYMS": acronyms_expanded,
    "A-CTA": cta_rules,
}


BODY_CHECKS = ["A-NO-EMOJI", "A-EURO-FORMAT", "A-NO-BANNED", "A-NO-CLAIMS", "A-ACRONYMS"]
CTA_CHECKS = ["A-CTA", "A-NO-EMOJI"]
SURFACE_CHECKS = {
    "cta": CTA_CHECKS, "button": CTA_CHECKS,
    "error": BODY_CHECKS, "confirmation": BODY_CHECKS, "empty-state": BODY_CHECKS,
    "notification": BODY_CHECKS, "onboarding-step": BODY_CHECKS, "disclosure": BODY_CHECKS,
    "risk-warning": BODY_CHECKS, "security": BODY_CHECKS, "banner": BODY_CHECKS, "toast": BODY_CHECKS,
}


def checks_for(surface):
    """Which assertions apply to a given surface. CTAs get only their own checks."""
    return SURFACE_CHECKS.get((surface or "").lower(), BODY_CHECKS)


def run(text, assertion_ids=None, surface=None):
    ids = assertion_ids or (checks_for(surface) if surface else list(REGISTRY))
    results = {}
    for aid in ids:
        fn = REGISTRY.get(aid)
        if fn:
            passed, msg = fn(text, surface)
            results[aid] = {"passed": passed, "message": msg}
    return results


if __name__ == "__main__":
    samples = [
        ("Send money", ["A-CTA"]),
        ("Send 150,00 €", ["A-CTA", "A-EURO-FORMAT"]),
        ("You received 150 € from Ana", ["A-NO-EMOJI", "A-EURO-FORMAT"]),
        ("Payment sent \U0001F389", ["A-NO-EMOJI"]),
        ("Guaranteed returns on your savings", ["A-NO-CLAIMS"]),
        ("Complete KYC to continue", ["A-ACRONYMS"]),
        ("Your balance is 2,540.00 €", ["A-EURO-FORMAT"]),
    ]
    for text, ids in samples:
        out = run(text, ids)
        verdict = "PASS" if all(r["passed"] for r in out.values()) else "FAIL"
        print(f"[{verdict}] {text!r} -> {out}")
    print("\n-- surface-based: a CTA only gets its own checks --")
    bad = "Kindly utilize your risk-free KYC €150 now!"
    print("cta:", run(bad, surface="cta"))
