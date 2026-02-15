import re


# ---------- 1. Hidden text detection (INTENT AWARE) ----------
def detect_hidden_text(page):
    hidden_texts = []

    elements = page.query_selector_all("*")
    for el in elements:
        try:
            style = el.evaluate(
                """el => {
                    const s = window.getComputedStyle(el);
                    return {
                        display: s.display,
                        visibility: s.visibility,
                        opacity: s.opacity,
                        fontSize: s.fontSize
                    };
                }"""
            )

            text = el.inner_text().strip()
            if not text:
                continue

            # Hidden / low-visibility
            is_hidden = (
                style["display"] == "none"
                or style["visibility"] == "hidden"
                or float(style["opacity"]) < 0.3
                or style["fontSize"].replace("px", "").isdigit()
                and float(style["fontSize"].replace("px", "")) < 8
            )

            if is_hidden:
                # IMPORTANT: only flag if text looks instruction-like
                if looks_like_instruction(text):
                    hidden_texts.append(text)

        except:
            continue

    return hidden_texts


def looks_like_instruction(text: str) -> bool:
    patterns = [
        r"ignore (all|previous)",
        r"follow (these|my) instructions",
        r"do not tell",
        r"override",
        r"system message",
        r"assistant",
        r"submit the form",
        r"click (here|below)",
    ]

    text = text.lower()
    return any(re.search(p, text) for p in patterns)


# ---------- 2. Dynamic DOM injection ----------
def detect_dynamic_dom_injection(page):
    suspicious_nodes = []

    try:
        mutations = page.evaluate(
            """
            () => {
                return document.querySelectorAll(
                    'script:not([src]), iframe, object, embed'
                ).length;
            }
            """
        )

        if mutations > 3:  # threshold
            suspicious_nodes.append(
                f"Multiple runtime-injected elements detected: {mutations}"
            )

    except:
        pass

    return suspicious_nodes


# ---------- 3. Phishing / deceptive UI ----------
def detect_phishing_forms(page):
    findings = []

    forms = page.query_selector_all("form")
    for f in forms:
        try:
            inputs = f.query_selector_all("input")
            for inp in inputs:
                t = inp.get_attribute("type")
                name = inp.get_attribute("name") or ""

                if t in ["password", "email"]:
                    if looks_like_sensitive_context(page):
                        findings.append(
                            f"Sensitive form detected ({t} field)"
                        )
        except:
            continue

    return findings


def looks_like_sensitive_context(page) -> bool:
    keywords = [
        "login",
        "sign in",
        "verify",
        "authentication",
        "account",
        "password",
        "otp",
    ]

    try:
        body_text = page.inner_text("body").lower()
        return any(k in body_text for k in keywords)
    except:
        return False
