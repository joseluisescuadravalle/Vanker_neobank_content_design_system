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
    "a small fee", "low fees", "fees may apply",
    "otp", "one-time password", "token",
    "something went wrong", "oops", "unexpected error", "technical difficulties",
    "please wait", "almost there", "just a moment", "hang tight", "working on it",
    "the best", "the cheapest", "the fastest", "no strings attached", "free forever",
    "you entered the wrong", "you failed to", "you forgot to", "invalid",
]
PROHIBITED_CLAIMS = [
    "guaranteed return", "guaranteed returns", "risk-free", "risk free", "no risk",
    "can't lose", "cannot lose", "beat the market", "guaranteed approval",
]
MUST_EXPAND = ["KYC", "APR", "SCA", "VoP", "BIC", "2FA", "CVV"]  # IBAN, PIN, SEPA: widely understood
GENERIC_CTA = {"ok", "submit", "confirm", "continue", "done", "next", "proceed"}
GENERIC_ERRORS = {"error", "invalid", "wrong", "incorrect", "review the data", "check the data", "review the field"}
GENERIC_REQUIRED = ["this is required", "this field is required", "required field",
                    "mandatory field", "this data is necessary", "field is mandatory"]
# A field error states a fact; it does not order someone who has not done anything wrong.
IMPERATIVE_OPENER = re.compile(r"^(enter|add|type|fill|provide|input|write|complete|insert)\b", re.IGNORECASE)
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
    if re.search(r"\d,\d\s?€", text):
        problems.append("one decimal on a rendered amount (cents show exactly two: '10,10 €')")
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
    low = t.lower().rstrip(".").strip()
    if low in GENERIC_ERRORS:
        problems.append("too generic; give a specific hint")
    for g in GENERIC_REQUIRED:
        if g in low:
            problems.append("'" + t + "' is the same sentence for every field; in an error summary six of these are indistinguishable. Name what is missing ('Your street is missing.')")
            break
    if IMPERATIVE_OPENER.match(t):
        problems.append("a field error states a fact, it does not give an order: 'Your street is missing.' rather than 'Enter your street.'")
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
    if "*" in t:
        problems.append("no asterisk: required is the default and carries no marker; only optional fields say '(optional)'")
    if re.search(r"\(required\)", t, re.IGNORECASE):
        problems.append("required fields carry no marker; only optional ones say '(optional)'")
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


STATUS_VOCABULARY = {
    "pending", "scheduled", "on hold", "declined", "failed", "canceled", "refunded", "returned",
    "frozen", "blocked", "not activated", "expired", "on its way",
    "in review", "action needed", "verified", "not approved",
    "upcoming", "paused", "target reached",
}
STATUS_BANNED = {
    "processing": "Pending", "in progress": "Pending", "awaiting": "Pending",
    "cancelled": "Canceled (American spelling)", "rejected": "Declined (a payment) or Not approved (a verification)",
    "error": "Failed",
    "completed": "no label (the normal state carries none)", "complete": "no label (the normal state carries none)",
    "done": "no label (the normal state carries none)", "successful": "no label (the normal state carries none)",
    "success": "no label (the normal state carries none)", "settled": "no label (the normal state carries none)",
    "paid": "no label (the normal state carries none)", "active": "no label (the normal state carries none)",
    "new": "no label (the normal state carries none)",
    "unverified": "In review or Action needed", "unconfirmed": "In review or Action needed",
    "locked": "Frozen (by the customer) or Blocked (by Vanker)", "inactive": "Not activated",
    "protected": "no label (a compliance claim is not a status)",
    "insured": "no label (a compliance claim is not a status)",
    "safe": "no label (a compliance claim is not a status)",
    "guaranteed": "no label (a compliance claim is not a status)",
}


def status_label(text, surface=None):
    t = text.strip()
    problems = []
    if not t:
        return (False, "empty status label")
    if EMOJI.search(t):
        problems.append("no emoji in a status label")
    if re.search(r"[.,:;!?]$", t):
        problems.append("no ending punctuation on a status label")
    if re.search(r"\d", t):
        problems.append("no numbers, amounts, dates, or counts inside a status label")
    # The word cap guards invented labels; a term in the controlled vocabulary has already
    # been decided ("On its way" is three words and is the right copy).
    if t.lower() not in STATUS_VOCABULARY and len(t.split()) > 2:
        problems.append("too long (" + str(len(t.split())) + " words); a status label outside the controlled vocabulary is one or two words")
    if t.upper() == t and len(t) > 2:
        problems.append("no ALL CAPS; use sentence case")
    elif re.search(r"\s[A-Z]", t):
        problems.append("sentence case: only the first word is capitalized")
    low = t.lower()
    if low in STATUS_BANNED:
        problems.append("'" + t + "' is not in the controlled vocabulary; use " + STATUS_BANNED[low])
    elif low not in STATUS_VOCABULARY:
        problems.append("'" + t + "' is not in the controlled status vocabulary (see components/library/status-label.md)")
    return (not problems, "; ".join(problems) or "ok")


AMOUNT_RE = re.compile(r"^\d{1,3}(?:\.\d{3})*(?:,\d{2})?\s\u20ac$")


def amount_value(text, surface=None):
    """A rendered amount or a preset: the figure and the euro sign, nothing else."""
    t = text.strip()
    if not t:
        return (False, "empty amount")
    problems = []
    if EMOJI.search(t):
        problems.append("no emoji in an amount")
    if re.search(r"[A-Za-z]", t):
        problems.append("an amount carries no words (a preset amount is a value, not a call to action)")
    if not AMOUNT_RE.match(t):
        problems.append("not the European amount format ('150 \u20ac', '2.540,75 \u20ac'): \u20ac after the amount with a space, dot thousands, comma decimals, at most two decimals")
    if re.search(r",00\s?\u20ac", t):
        problems.append("no trailing ',00' on a round amount")
    if re.search(r"\d,\d\s?\u20ac", t):
        problems.append("a rendered amount with cents shows exactly two decimals ('10,10 \u20ac', not '10,1 \u20ac'); only what a person is still typing keeps one")
    return (not problems, "; ".join(problems) or "ok")


def amount_label(text, surface=None):
    """The visible label of an amount field: a short noun, no currency, no digits."""
    t = text.strip()
    passed, msg = label_in(t)
    problems = [] if passed else [msg]
    if "\u20ac" in t or re.search(r"\beuros?\b", t, re.IGNORECASE):
        problems.append("no currency symbol or currency word in the visible label; the adornment carries it")
    if re.search(r"\d", t):
        problems.append("no digits in an amount-field label")
    return (not problems, "; ".join(problems) or "ok")


EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[A-Za-z]{2,}")
DIGIT_RUN_RE = re.compile(r"(?<!\d)(?:\+\d{1,3}[ .-]?)?(?:\d[ .-]?){5,}\d(?!\d)")


def masked_contact(text, surface=None):
    """No full contact details or long digit runs in copy: mask them."""
    problems = []
    if EMAIL_RE.search(text):
        problems.append("a full email address; mask it (a\u00b7\u00b7\u00b7@example.com)")
    for m in DIGIT_RUN_RE.finditer(text):
        tail = text[m.end():m.end() + 2]
        if tail.strip().startswith("\u20ac"):
            continue  # an amount, not a phone number, an IBAN, or a code
        problems.append("a long run of digits ('" + m.group(0).strip() + "'); mask a phone number, an IBAN, or a card, and never echo a code")
        break
    return (not problems, "; ".join(problems) or "ok")


MONEY_OUTCOME = re.compile(r"\b(payment|transfer|money|funds|paid|charged|sent it|debited)\b", re.IGNORECASE)
# Outcome auxiliaries only: "don't" in "we don't charge a fee" is a habit, not an outcome.
NEG_CONTRACTION = re.compile(r"\b(?:could|did|has|have|had|is|are|was|were|wo|ca|would|should)n['\u2019]t\b", re.IGNORECASE)
ERROR_CODE = re.compile(r"\b(?:error|code)\s*[:#]?\s*\d{3,}\b|\b[45]\d{2}\s+error\b", re.IGNORECASE)
REASSURANCE = re.compile(r"money is safe|no money has|money has not|nothing has left|has left your account|on its way|do not know yet|money hasn't", re.IGNORECASE)


def spelled_negation(text, surface=None):
    """A sentence about whether money moved spells out the negative."""
    m = NEG_CONTRACTION.search(text)
    if m and MONEY_OUTCOME.search(text):
        return (False, "negative contraction ('" + m.group(0) + "') in a sentence about money; spell it out ('could not', 'do not')")
    return (True, "ok")


def system_error(text, surface=None):
    """One slot of a connectivity or system error: no visible code, no shouting."""
    problems = []
    m = ERROR_CODE.search(text)
    if m:
        problems.append("visible error code ('" + m.group(0) + "'); use a discreet reference line instead")
    if "!" in text:
        problems.append("no exclamation mark in a system error")
    return (not problems, "; ".join(problems) or "ok")


def money_accounted(text, surface=None):
    """Screen-level: an error that interrupts a money action says what happened to the money.

    This runs on the whole screen (title plus body), never on one slot: the title states
    the failure and the body carries the reassurance, so a title checked alone would always
    fail.
    """
    if MONEY_OUTCOME.search(text) and not REASSURANCE.search(text):
        return (False, "the screen mentions money but never says what happened to it (no money left, on its way, or outcome not known yet)")
    return (True, "ok")


PARTICIPLE_RE = re.compile(r"^[A-Z][a-z]+ing\b")
VAGUE_LOADING = ["loading", "processing", "please wait", "one moment", "wait"]


def loading_message(text, surface=None):
    """A waiting status line: says what is happening, as it happens."""
    t = text.strip()
    problems = []
    if not t:
        return (False, "empty status message")
    if EMOJI.search(t):
        problems.append("no emoji in a status message")
    if t.endswith("."):
        problems.append("no ending period on a status line; it is a label, not a sentence")
    if "!" in t or "?" in t:
        problems.append("no exclamation or question mark while someone waits")
    if t.rstrip(".").strip().lower() in VAGUE_LOADING:
        problems.append("'" + t + "' says nothing; name what is happening ('Checking your details')")
    elif not PARTICIPLE_RE.match(t):
        problems.append("start with what we are doing, in the present participle ('Checking your details', 'Sending your payment')")
    if len(t) > 45:
        problems.append("too long (" + str(len(t)) + " chars); keep a status line short")
    return (not problems, "; ".join(problems) or "ok")


def skeleton_placeholder(text, surface=None):
    """A skeleton carries no content: no text, and above all no money."""
    t = text.strip()
    problems = []
    if re.search(r"\d", t):
        problems.append("a skeleton never shows digits: a placeholder amount that resolves into a different one is the worst failure in this system")
    if "\u20ac" in t:
        problems.append("a skeleton never shows a currency symbol")
    if re.search(r"[A-Za-z]", t):
        problems.append("a skeleton carries no text; it is a grey outline of the layout")
    return (not problems, "; ".join(problems) or "ok")


INTRO_CTA_ALLOWED = {"start", "not now"}
GOAL_VERBS = ["activate", "verify", "set up", "enable", "register", "order", "create", "add", "sign up"]


def carousel_headline(text, surface=None):
    """A welcome-card headline: the whole benefit in one line."""
    t = text.strip()
    problems = []
    if not t:
        return (False, "empty headline")
    if EMOJI.search(t):
        problems.append("no emoji in a headline")
    if re.search(r"[.;:!?]$", t):
        problems.append("no ending punctuation on a card headline")
    if len(t.split()) > 6:
        problems.append("too long (" + str(len(t.split())) + " words); a card headline carries the benefit in about six")
    return (not problems, "; ".join(problems) or "ok")


def carousel_body(text, surface=None):
    """A welcome-card body: it expands the headline and adds nothing new."""
    t = text.strip()
    problems = []
    if not t:
        return (True, "ok")  # the body is optional and usually unnecessary
    if EMOJI.search(t):
        problems.append("no emoji in a card body")
    if t.endswith("."):
        problems.append("no ending period on a card body")
    if len(t) > 90:
        problems.append("too long (" + str(len(t)) + " chars); at most two short lines")
    core = re.sub(r"(?<=\d)\.(?=\d)", "", t)
    if len(re.findall(r"\.\s+\S", core)) >= 1:
        problems.append("more than one sentence; the body expands the headline, it does not add a second idea")
    if re.search(r"\d", t):
        problems.append("no figures in a card body: a rate, a price, or a count needs a disclosure this card cannot carry")
    return (not problems, "; ".join(problems) or "ok")


def intro_cta(text, surface=None):
    """The buttons on a flow-intro screen are fixed: Start and Not now."""
    t = text.strip()
    low = t.lower()
    if low in INTRO_CTA_ALLOWED:
        return (True, "ok")
    for v in GOAL_VERBS:
        if low.startswith(v):
            return (False, "'" + t + "' names the goal of the flow, not what the tap does; the tap opens the first step, so the label is 'Start'")
    return (False, "'" + t + "' is not a flow-intro button; use 'Start' (primary) or 'Not now' (secondary)")


LIMIT_STATEMENT = re.compile(r"we do not|we never|we don['\u2019]t|stays on your phone|stay on your phone", re.IGNORECASE)
NEEDS_ACCESS = re.compile(r"we need (?:access|your|the)|needs access|allow access|grant (?:us )?access", re.IGNORECASE)


def permission_body(text, surface=None):
    """A permission-priming body: what happens with it, then what we will not do."""
    t = text.strip()
    problems = []
    if not t:
        return (False, "empty permission body")
    if NEEDS_ACCESS.search(t):
        problems.append("no 'we need access' framing; say what the person will do and what it is for")
    if not LIMIT_STATEMENT.search(t):
        problems.append("missing the limit sentence: say what Vanker will not do with the permission (this is the sentence that earns it)")
    if not re.search(r"\bYou\b|\bYou['\u2019]ll\b|\byour\b", t):
        problems.append("the person is the subject of what happens; write it from their side")
    if re.search(r"\bat risk\b|\bunsafe\b|\bnot protected\b", t, re.IGNORECASE):
        problems.append("no fear framing on a permission screen")
    return (not problems, "; ".join(problems) or "ok")


SPELLED_NUMBER = re.compile(
    r"\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)\s+"
    r"(steps?|minutes?|hours?|days?|weeks?|months?|years?|tries|attempts?|digits?|times?|cards?|payments?|euros?)\b",
    re.IGNORECASE)


def numerals(text, surface=None):
    """Numbers are digits in body copy and instructions: '3 steps', not 'three steps'."""
    m = SPELLED_NUMBER.search(text)
    if m:
        return (False, "spelled-out number ('" + m.group(0) + "'); write numbers as digits in body copy (see terminology/glossary.md)")
    return (True, "ok")


TOOLTIP_CTA = re.compile(r"\b(tap|click|press|go to|open|add|send|start|choose|select) (here|now|it|to)\b", re.IGNORECASE)
LINK_HINT = re.compile(r"\bhttps?://|\bread (?:the|our|more)\b|\blearn more\b|\bsee (?:the )?(?:full|terms)\b|\]\(", re.IGNORECASE)


def tooltip_body(text, surface=None):
    """A tooltip: one or two sentences that define a term, and nothing that must be seen."""
    t = text.strip()
    problems = []
    if not t:
        return (False, "empty tooltip")
    if EMOJI.search(t):
        problems.append("no emoji in a tooltip")
    if not t.endswith("."):
        problems.append("a tooltip is complete sentences and ends with a period")
    if len(t) > 160:
        problems.append("too long (" + str(len(t)) + " chars); over two lines it is a sheet, not a tooltip")
    core = re.sub(r"(?<=\d)\.(?=\d)", "", t)
    if len(re.findall(r"\.\s+\S", core)) >= 2:
        problems.append("more than two sentences; that is a sheet")
    if "\u20ac" in t or re.search(r"\d\s?%", t) or re.search(r"\d", t):
        problems.append("no figures in a tooltip: an amount, a rate, or a limit that affects a decision must be visible on the screen")
    if TOOLTIP_CTA.search(t):
        problems.append("no call to action in a tooltip")
    if LINK_HINT.search(t):
        problems.append("a tooltip carries no link; if a link is needed it is a sheet")
    return (not problems, "; ".join(problems) or "ok")


def tooltip_trigger(text, surface=None):
    """The trigger's accessible name is the question the panel answers."""
    t = text.strip()
    problems = []
    if not t:
        return (False, "empty trigger name")
    if t.lower().strip("?") in {"info", "information", "help", "?", "more info"}:
        problems.append("'" + t + "' is not an accessible name; use the question the tooltip answers ('What is a BIC?')")
    elif not t.endswith("?"):
        problems.append("the trigger name is a question ('What is a BIC?')")
    if EMOJI.search(t):
        problems.append("no emoji in a trigger name")
    return (not problems, "; ".join(problems) or "ok")


COUNTER_RE = re.compile(r"^\d+ characters? left$")


def counter_text(text, surface=None):
    """A character counter says what is left, in words."""
    t = text.strip()
    if COUNTER_RE.match(t):
        return (True, "ok")
    if re.match(r"^\d+\s*/\s*\d+$", t):
        return (False, "'" + t + "' is a ratio; a counter says the room that is left ('22 characters left')")
    return (False, "'" + t + "' is not a counter; use '{n} characters left'")


def error_summary_title(text, surface=None):
    """The title above a failed submit: what to do, no blame, no count."""
    t = text.strip()
    problems = []
    if not t:
        return (False, "empty summary title")
    if t.endswith("."):
        problems.append("no ending period on the summary title")
    if EMOJI.search(t):
        problems.append("no emoji")
    if re.search(r"\berrors?\b|\bproblems?\b|\bfailed\b|\binvalid\b", t, re.IGNORECASE):
        problems.append("do not name it an error or a problem; say what to do ('Check these before you continue')")
    if re.search(r"\byou (?:did|have|entered|forgot|missed)\b", t, re.IGNORECASE):
        problems.append("no blame in the summary title")
    if re.search(r"\d", t):
        problems.append("no count in the title: it stops being true as the person fixes them")
    return (not problems, "; ".join(problems) or "ok")


EMPTY_HEADERS = {
    "more information", "more info", "details", "more details", "other", "others",
    "read more", "learn more", "info", "information", "additional information", "misc",
}


def accordion_header(text, surface=None):
    """An accordion header predicts its content, or nobody opens it."""
    t = text.strip()
    problems = []
    if not t:
        return (False, "empty header")
    if EMOJI.search(t):
        problems.append("no emoji in an accordion header")
    low = t.lower().rstrip("?.").strip()
    if low in EMPTY_HEADERS:
        problems.append("'" + t + "' describes the act of opening, not the content; name what is inside")
    if t.endswith("."):
        problems.append("no ending period on a header; a question takes a question mark, a noun phrase takes nothing")
    if len(t.split()) > 8:
        problems.append("too long (" + str(len(t.split())) + " words); a header is one line on a phone")
    if re.match(r"^\d", t):
        problems.append("no count in a header ('3 things you should know')")
    return (not problems, "; ".join(problems) or "ok")


TOGGLE_ACTION_VERBS = ["turn on", "turn off", "enable", "disable", "activate", "deactivate",
                       "allow", "block", "freeze", "unfreeze", "stop", "start", "switch on", "switch off"]


def toggle_label(text, surface=None):
    """A switch is named by its setting or its state, never by an action verb."""
    t = text.strip()
    problems = []
    if not t:
        return (False, "empty toggle label")
    low = t.lower()
    if EMOJI.search(t):
        problems.append("no emoji in a toggle label")
    if re.search(r"[.,:;!?]$", t):
        problems.append("no ending punctuation on a toggle label")
    for v in TOGGLE_ACTION_VERBS:
        if low.startswith(v):
            problems.append("'" + t + "' is an action verb, so it is a button label; name the setting or the state instead ('Card frozen', not 'Freeze card')")
            break
    if re.search(r"^(do not|don['\u2019]t|never)\b", low) or re.search(r"\bno longer\b", low):
        problems.append("no negative label: 'off' would become a double negative")
    if re.search(r"\b(on|off)\b$", low):
        problems.append("no 'On' or 'Off' in the label; the switch position is the state")
    if len(t.split()) > 4:
        problems.append("too long (" + str(len(t.split())) + " words); a toggle label is a short noun phrase")
    return (not problems, "; ".join(problems) or "ok")


ENUMERATION = re.compile(
    r"no account (?:with|for|found)|account (?:does not|doesn['\u2019]t) exist|not registered|"
    r"user not found|no user|we (?:could not|couldn['\u2019]t) find (?:an? )?(?:account|user|email)|"
    r"(?:email|address|phone number) (?:is )?(?:not recognized|not recognised|unknown)|"
    r"(?:that|this) email is not|already (?:registered|in use|has an account)",
    re.IGNORECASE)


def no_enumeration(text, surface=None):
    """Never reveal whether an account exists: it turns a login screen into a lookup tool."""
    m = ENUMERATION.search(text)
    if m:
        return (False, "reveals whether an account exists ('" + m.group(0).strip() + "'); say the same thing either way ('If there is an account for that email, we have sent it a link.')")
    return (True, "ok")


REVERSIBLE = re.compile(r"any time|anytime|whenever you want|you can (?:un|undo|change|switch)", re.IGNORECASE)
IRREVERSIBLE = re.compile(r"for good|permanently|cannot be undone|can['\u2019]t be undone|will stop working|no longer work", re.IGNORECASE)


def reversibility(text, surface=None):
    """A card action says, in its own copy, whether it can be undone."""
    t = text.strip()
    if not t:
        return (False, "empty card action copy")
    if REVERSIBLE.search(t) or IRREVERSIBLE.search(t):
        return (True, "ok")
    return (False, "does not say whether this can be undone; state it in the same copy as the action ('You can unfreeze it any time', 'This card will stop working for good')")


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
    "A-STATUS": status_label,
    "A-AMOUNT-VALUE": amount_value,
    "A-AMOUNT-LABEL": amount_label,
    "A-MASK": masked_contact,
    "A-NEGATION": spelled_negation,
    "A-SYSTEM-ERROR": system_error,
    "A-MONEY-ACCOUNTED": money_accounted,
    "A-LOADING": loading_message,
    "A-SKELETON": skeleton_placeholder,
    "A-CARD-HEADLINE": carousel_headline,
    "A-CARD-BODY": carousel_body,
    "A-INTRO-CTA": intro_cta,
    "A-PERMISSION": permission_body,
    "A-NUMERALS": numerals,
    "A-TOOLTIP": tooltip_body,
    "A-TOOLTIP-TRIGGER": tooltip_trigger,
    "A-COUNTER": counter_text,
    "A-ERROR-SUMMARY": error_summary_title,
    "A-ACCORDION-HEADER": accordion_header,
    "A-TOGGLE-LABEL": toggle_label,
    "A-ENUMERATION": no_enumeration,
    "A-REVERSIBILITY": reversibility,
}


BODY_CHECKS = ["A-NO-EMOJI", "A-EURO-FORMAT", "A-NO-BANNED", "A-NO-CLAIMS", "A-ACRONYMS", "A-NO-INLINE-CTA", "A-MASK", "A-NEGATION", "A-NUMERALS"]
CTA_CHECKS = ["A-CTA", "A-NO-EMOJI"]
FIELD_CHECKS = ["A-FIELD-ERROR", "A-NO-EMOJI", "A-EURO-FORMAT", "A-NO-BANNED", "A-NO-CLAIMS", "A-ACRONYMS", "A-NO-INLINE-CTA", "A-MASK", "A-NEGATION", "A-NUMERALS"]
SURFACE_CHECKS = {
    "cta": CTA_CHECKS, "button": CTA_CHECKS,
    "field-error": FIELD_CHECKS, "validation": FIELD_CHECKS,
    "push-title": ["A-PUSH-TITLE", "A-EURO-FORMAT", "A-NO-BANNED", "A-NO-CLAIMS"],
    "push-body": ["A-PUSH-BODY", "A-NO-EMOJI", "A-EURO-FORMAT", "A-NO-BANNED", "A-NO-CLAIMS", "A-ACRONYMS", "A-NO-INLINE-CTA", "A-MASK"],
    "error": BODY_CHECKS, "confirmation": BODY_CHECKS, "empty-state": BODY_CHECKS,
    "notification": BODY_CHECKS, "onboarding-step": BODY_CHECKS, "disclosure": BODY_CHECKS,
    "risk-warning": BODY_CHECKS, "banner": BODY_CHECKS,
    "toast": ["A-TOAST", "A-NO-EMOJI", "A-EURO-FORMAT", "A-NO-BANNED", "A-NO-CLAIMS"],
    "dropdown-option": ["A-OPTION", "A-NO-BANNED", "A-NO-CLAIMS"], "option": ["A-OPTION", "A-NO-BANNED", "A-NO-CLAIMS"],
    "label-in": ["A-LABEL-IN", "A-NO-EMOJI", "A-NO-BANNED", "A-NO-CLAIMS"],
    "label-out": ["A-LABEL-OUT", "A-NO-EMOJI", "A-NO-BANNED", "A-NO-CLAIMS", "A-ACRONYMS"],
    "legend": ["A-LEGEND", "A-NO-EMOJI", "A-NO-BANNED", "A-NO-CLAIMS"],
    "helper-text": ["A-HELPER", "A-NO-EMOJI", "A-EURO-FORMAT", "A-NO-BANNED", "A-NO-CLAIMS", "A-ACRONYMS", "A-NO-INLINE-CTA"],
    "placeholder": ["A-NO-EMOJI", "A-NO-BANNED", "A-NO-CLAIMS"],
    "checkbox": ["A-CHECKBOX", "A-NO-EMOJI", "A-NO-BANNED", "A-NO-CLAIMS"],
    "radio-option": ["A-RADIO", "A-NO-BANNED", "A-NO-CLAIMS"], "radio": ["A-RADIO", "A-NO-BANNED", "A-NO-CLAIMS"],
    "status-label": ["A-STATUS", "A-NO-EMOJI", "A-NO-BANNED", "A-NO-CLAIMS"],
    "status": ["A-STATUS", "A-NO-EMOJI", "A-NO-BANNED", "A-NO-CLAIMS"],
    "badge": ["A-STATUS", "A-NO-EMOJI", "A-NO-BANNED", "A-NO-CLAIMS"],
    "tag": ["A-STATUS", "A-NO-EMOJI", "A-NO-BANNED", "A-NO-CLAIMS"],
    "amount-value": ["A-AMOUNT-VALUE", "A-NO-EMOJI", "A-NO-BANNED", "A-NO-CLAIMS"],
    "preset-amount": ["A-AMOUNT-VALUE", "A-NO-EMOJI", "A-NO-BANNED", "A-NO-CLAIMS"],
    "amount-label": ["A-AMOUNT-LABEL", "A-NO-EMOJI", "A-NO-BANNED", "A-NO-CLAIMS"],
    "code-screen": BODY_CHECKS, "security": BODY_CHECKS,
    "system-error": BODY_CHECKS + ["A-SYSTEM-ERROR"],
    "system-error-title": ["A-SYSTEM-ERROR", "A-NO-EMOJI", "A-NO-BANNED", "A-NEGATION"],
    "system-error-screen": BODY_CHECKS + ["A-SYSTEM-ERROR", "A-MONEY-ACCOUNTED"],
    "loading": ["A-LOADING", "A-NO-BANNED", "A-NO-CLAIMS"],
    "loading-screen": BODY_CHECKS + ["A-MONEY-ACCOUNTED"],
    "skeleton": ["A-SKELETON"],
    "carousel-headline": ["A-CARD-HEADLINE", "A-NO-BANNED", "A-NO-CLAIMS", "A-NO-EMOJI"],
    "carousel-body": ["A-CARD-BODY", "A-NO-BANNED", "A-NO-CLAIMS", "A-NO-EMOJI"],
    "flow-intro-cta": ["A-INTRO-CTA", "A-CTA", "A-NO-EMOJI"],
    "flow-intro-body": BODY_CHECKS,
    "permission-body": BODY_CHECKS + ["A-PERMISSION"],
    "permission-heading": ["A-NO-EMOJI", "A-NO-BANNED", "A-NO-CLAIMS", "A-MASK"],
    "tooltip": ["A-TOOLTIP", "A-NO-BANNED", "A-NO-CLAIMS", "A-ACRONYMS", "A-NUMERALS"],
    "tooltip-trigger": ["A-TOOLTIP-TRIGGER", "A-NO-EMOJI", "A-NO-BANNED"],
    "counter": ["A-COUNTER"],
    "error-summary-title": ["A-ERROR-SUMMARY", "A-NO-BANNED", "A-NO-EMOJI"],
    "accordion-header": ["A-ACCORDION-HEADER", "A-NO-BANNED", "A-NO-CLAIMS", "A-NUMERALS"],
    "accordion-body": BODY_CHECKS,
    "toggle-label": ["A-TOGGLE-LABEL", "A-NO-EMOJI", "A-NO-BANNED", "A-NO-CLAIMS"],
    "toggle-description": BODY_CHECKS,
    "auth": BODY_CHECKS + ["A-ENUMERATION"],
    "auth-error": FIELD_CHECKS + ["A-ENUMERATION"],
    "card-action": BODY_CHECKS + ["A-REVERSIBILITY"],
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
