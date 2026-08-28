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
GENERIC_ERRORS = {"error", "invalid", "wrong", "incorrect", "review the data", "check the data", "review the field"}
INLINE_CTA_VERBS = r"cancel|retry|confirm|continue|undo|dismiss|accept|decline|delete|try(?:\s+again)?|send|ok"
INLINE_CTA = re.compile(r"\b(?:" + INLINE_CTA_VERBS + r")\b\s+(?:now\s+)?(?:or|and)\s+\b(?:" + INLINE_CTA_VERBS + r")\b", re.IGNORECASE)

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
    if len(label.split()) > 3:
        problems.append("more than 3 words")
    if EMOJI.search(label):
        problems.append("emoji")
    if re.search(r"[.,:;!?]", label):
        problems.append("punctuation (no . , : ; ! ? in a CTA)")
    if re.search(r"\d.*€|€.*\d|\d", label):
        problems.append("contains a number or amount")
    if label.lower() in GENERIC_CTA:
        problems.append("generic label '" + label + "'")
    return (not problems, "; ".join(problems) or "ok")


def no_inline_cta(text, surface=None):
    m = INLINE_CTA.search(text)
    msg = ("inline call to action (\"" + m.group(0).strip() + "\"); put each action in its own button") if m else "ok"
    return (m is None, msg)


def field_error(text, surface=None):
    t = text.strip()
    problems = []
    if not t.endswith("."):
        problems.append("must end with a period")
    if "?" in t or "!" in t:
        problems.append("no ? or ! in a field error")
    core = re.sub(r"(?<=\d)\.(?=\d)", "", t)
    if core.count(".") > 1 or ". " in core:
        problems.append("one sentence only (no two sentences)")
    if t.lower().rstrip(".").strip() in GENERIC_ERRORS:
        problems.append("too generic; give a specific hint")
    return (not problems, "; ".join(problems) or "ok")


def push_title(text, surface=None):
    t = text.strip()
    problems = []
    n = len(EMOJI.findall(t))
    if n > 2:
        problems.append("too many emoji (" + str(n) + "); max 2 in a push title")
    if len(t) > 40:
        problems.append("too long (" + str(len(t)) + " chars); keep the push title to ~40")
    return (not problems, "; ".join(problems) or "ok")


def push_body(text, surface=None):
    t = text.strip()
    if len(t) > 120:
        return (False, "too long (" + str(len(t)) + " chars); keep the push body to ~120 (2 lines)")
    return (True, "ok")


def toast_msg(text, surface=None):
    t = text.strip()
    problems = []
    if t.endswith("."):
        problems.append("no ending period in a toast")
    if "?" in t or "!" in t:
        problems.append("no ? or ! in a toast")
    if len(t) > 50:
        problems.append("too long (" + str(len(t)) + " chars); keep the toast to ~50")
    return (not problems, "; ".join(problems) or "ok")


def option_label(text, surface=None):
    t = text.strip()
    problems = []
    if not t:
        problems.append("empty option")
    if re.search(r"[.,:;!?]$", t):
        problems.append("no ending punctuation in an option")
    if EMOJI.search(t):
        problems.append("no emoji in an option")
    if len(t.split()) > 4:
        problems.append("too many words; keep the option to a few")
    return (not problems, "; ".join(problems) or "ok")


def label_in(text, surface=None):
    t = text.strip()
    problems = []
    if not t:
        problems.append("empty label")
    if re.search(r"[.:!?]$", t):
        problems.append("no ending period, colon, or question mark on a label in")
    if EMOJI.search(t):
        problems.append("no emoji in a label")
    if len(t.split()) > 4:
        problems.append("too long for a label in; use a short noun (aim 1-3 words) and move detail to a label out")
    return (not problems, "; ".join(problems) or "ok")


def label_out(text, surface=None):
    t = text.strip()
    problems = []
    if not t:
        problems.append("empty label")
    if t.endswith("."):
        problems.append("no ending period on a label out")
    if t.endswith(":"):
        problems.append("no colon on a label out")
    if EMOJI.search(t):
        problems.append("no emoji in a label")
    return (not problems, "; ".join(problems) or "ok")


def legend(text, surface=None):
    t = text.strip()
    problems = []
    if not t:
        problems.append("empty legend")
    if t.endswith(".") or t.endswith(":"):
        problems.append("no ending period or colon on a legend")
    if EMOJI.search(t):
        problems.append("no emoji in a legend")
    return (not problems, "; ".join(problems) or "ok")


def helper_text(text, surface=None):
    t = text.strip()
    problems = []
    if "?" in t:
        problems.append("helper text is not a question")
    if EMOJI.search(t):
        problems.append("no emoji in helper text")
    if len(t) > 200:
        problems.append("too long (" + str(len(t)) + " chars); keep helper text to about three lines")
    core = re.sub(r"(?<=\d)\.(?=\d)", "", t)
    if len(re.findall(r"\.\s+\S", core)) >= 2:
        problems.append("avoid several sentences separated by periods; prefer one sentence")
    return (not problems, "; ".join(problems) or "ok")


def checkbox_label(text, surface=None):
    t = text.strip()
    problems = []
    if not t:
        problems.append("empty checkbox label")
    if "?" in t:
        problems.append("a checkbox label is a statement, not a question")
    if EMOJI.search(t):
        problems.append("no emoji in a checkbox label")
    return (not problems, "; ".join(problems) or "ok")


def radio_option(text, surface=None):
    t = text.strip()
    problems = []
    if not t:
        problems.append("empty option")
    if re.search(r"[.:;!?]$", t):
        problems.append("no ending punctuation on a radio option")
    if EMOJI.search(t):
        problems.append("no emoji in an option")
    if len(t) > 60:
        problems.append("too long; keep a radio option to one line")
    return (not problems, "; ".join(problems) or "ok")


REGISTRY = {
    "A-NO-EMOJI": no_emoji,
    "A-EURO-FORMAT": euro_format,
    "A-NO-BANNED": no_banned_terms,
    "A-NO-CLAIMS": no_prohibited_claims,
    "A-ACRONYMS": acronyms_expanded,
    "A-CTA": cta_rules,
    "A-NO-INLINE-CTA": no_inline_cta,
    "A-FIELD-ERROR": field_error,
    "A-PUSH-TITLE": push_title,
    "A-PUSH-BODY": push_body,
    "A-TOAST": toast_msg,
    "A-OPTION": option_label,
    "A-LABEL-IN": label_in,
    "A-LABEL-OUT": label_out,
    "A-LEGEND": legend,
    "A-HELPER": helper_text,
    "A-CHECKBOX": checkbox_label,
    "A-RADIO": radio_option,
}


BODY_CHECKS = ["A-NO-EMOJI", "A-EURO-FORMAT", "A-NO-BANNED", "A-NO-CLAIMS", "A-ACRONYMS", "A-NO-INLINE-CTA"]
CTA_CHECKS = ["A-CTA", "A-NO-EMOJI"]
FIELD_CHECKS = ["A-FIELD-ERROR", "A-NO-EMOJI", "A-EURO-FORMAT", "A-NO-BANNED", "A-NO-CLAIMS", "A-ACRONYMS", "A-NO-INLINE-CTA"]
SURFACE_CHECKS = {
    "cta": CTA_CHECKS, "button": CTA_CHECKS,
    "field-error": FIELD_CHECKS, "validation": FIELD_CHECKS,
    "push-title": ["A-PUSH-TITLE", "A-EURO-FORMAT", "A-NO-BANNED", "A-NO-CLAIMS"],
    "push-body": ["A-PUSH-BODY", "A-NO-EMOJI", "A-EURO-FORMAT", "A-NO-BANNED", "A-NO-CLAIMS", "A-ACRONYMS", "A-NO-INLINE-CTA"],
    "error": BODY_CHECKS, "confirmation": BODY_CHECKS, "empty-state": BODY_CHECKS,
    "notification": BODY_CHECKS, "onboarding-step": BODY_CHECKS, "disclosure": BODY_CHECKS,
    "risk-warning": BODY_CHECKS, "security": BODY_CHECKS, "banner": BODY_CHECKS,
    "toast": ["A-TOAST", "A-NO-EMOJI", "A-EURO-FORMAT", "A-NO-BANNED", "A-NO-CLAIMS"],
    "dropdown-option": ["A-OPTION", "A-NO-BANNED", "A-NO-CLAIMS"], "option": ["A-OPTION", "A-NO-BANNED", "A-NO-CLAIMS"],
    "label-in": ["A-LABEL-IN", "A-NO-EMOJI", "A-NO-BANNED", "A-NO-CLAIMS"],
    "label-out": ["A-LABEL-OUT", "A-NO-EMOJI", "A-NO-BANNED", "A-NO-CLAIMS", "A-ACRONYMS"],
    "legend": ["A-LEGEND", "A-NO-EMOJI", "A-NO-BANNED", "A-NO-CLAIMS"],
    "helper-text": ["A-HELPER", "A-NO-EMOJI", "A-EURO-FORMAT", "A-NO-BANNED", "A-NO-CLAIMS", "A-ACRONYMS", "A-NO-INLINE-CTA"],
    "placeholder": ["A-NO-EMOJI", "A-NO-BANNED", "A-NO-CLAIMS"],
    "checkbox": ["A-CHECKBOX", "A-NO-EMOJI", "A-NO-BANNED", "A-NO-CLAIMS"],
    "radio-option": ["A-RADIO", "A-NO-BANNED", "A-NO-CLAIMS"], "radio": ["A-RADIO", "A-NO-BANNED", "A-NO-CLAIMS"],
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
