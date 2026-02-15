import time
from agent.agent import Agent
from browser.controller import get_page, execute_action

from sec_layer.dom_analyzer import (
    detect_hidden_text,
    detect_dynamic_dom_injection,
    detect_phishing_forms,
)

from sec_layer.risk_engine import compute_risk
from sec_layer.policy import enforce_policy


if __name__ == "__main__":
    print("\n=== Agentic Browser Security Framework ===")

    url = input("Enter website URL: ").strip()

    page, browser, p = get_page(url)

    agent = Agent()
    action = agent.decide_action(page)

    print("\n[AGENT ACTION PROPOSED]")
    print(action)

    start = time.time()

    hidden_texts = detect_hidden_text(page)
    dynamic = detect_dynamic_dom_injection(page)
    phishing = detect_phishing_forms(page)

    risk, reasons = compute_risk(hidden_texts, dynamic, phishing)
    decision = enforce_policy(risk)

    print("\n[SECURITY SCAN RESULT]")
    print("Risk Score:", risk)
    print("Decision:", decision)

    if reasons:
        print("Reasons:")
        for r in reasons:
            print(" -", r)

    latency = (time.time() - start) * 1000
    print(f"\n[PERFORMANCE]\nSecurity analysis latency: {latency:.2f} ms")

    if decision == "ALLOW":
        print("\n[ACTION EXECUTED]")
        execute_action(page, action)

    elif decision == "WARN":
        print("\n[WARNING]")
        if input("Proceed? (y/n): ").lower() == "y":
            execute_action(page, action)
        else:
            print("[ACTION CANCELLED]")

    else:
        print("\n[ACTION BLOCKED]")

    print("\n[INFO] Keeping browser open for 15 seconds...")
    try:
        page.wait_for_timeout(15000)
    except:
        pass

    browser.close()
    p.stop()
#file:///C:/Users/Swastik%20Awasthi/OneDrive/Desktop/hackiitk/agentic-browser-security-CLEAN/agentic-browser-security/attacks/hidden_prompt.html
#file:///C:/Users/Swastik%20Awasthi/OneDrive/Desktop/hackiitk/agentic-browser-security-CLEAN/agentic-browser-security/attacks/safe_page.html
#file:///C:/Users/Swastik%20Awasthi/OneDrive/Desktop/hackiitk/agentic-browser-security-CLEAN/agentic-browser-security/attacks/dynamic_injection.html
