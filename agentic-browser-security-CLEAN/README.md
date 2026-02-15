# 🔐 Agentic Browser Security Framework

Securing Agentic Browsers Against Malicious Web Interactions

This project implements a security framework for agentic browsers — AI-powered systems that autonomously interact with web pages for tasks such as navigation, data extraction, form filling, and online automation.

Modern agentic browsers rely on Large Language Models (LLMs) to interpret web content and decide actions like clicking buttons, submitting forms, or navigating pages. However, web environments are inherently adversarial. Malicious pages can embed deceptive instructions, hidden prompts, misleading UI elements, or dynamically injected content to manipulate the agent into unsafe actions.

Traditional browser security mechanisms are designed for humans and fail to protect autonomous agents. This framework introduces a **pre-action security layer** that analyzes DOM content, computes an explainable risk score, and enforces security policies before any browser action is executed.

---

## Key Capabilities

- Detection of hidden prompt injections using CSS tricks (display:none, opacity, font-size)
- Detection of JavaScript-based dynamic DOM injections
- Identification of deceptive UI elements and phishing-style forms
- Interception of agent actions before execution
- Rule-based risk scoring with human-readable explanations
- Enforcement of ALLOW / WARN / BLOCK policies
- Real-time analysis with low latency and no external network calls

---

## System Architecture & Code Structure

agentic-browser-security/

├── agent/  
│   └── agent.py                (Agent logic – proposes browser actions)

├── browser/  
│   └── controller.py           (Playwright-based browser controller)

├── sec_layer/  
│   ├── dom_analyzer.py         (DOM inspection & threat detection)  
│   ├── risk_engine.py          (Rule-based risk scoring)  
│   ├── policy.py               (ALLOW / WARN / BLOCK enforcement)  
│   ├── metrics.py              (Precision, Recall, F1 tracking)  
│   └── logger.py               (Decision logging)

├── attacks/  
│   ├── hidden_prompt.html      (Hidden instruction attack)  
│   ├── dynamic_injection.html  (Dynamic DOM injection attack)  
│   └── safe_page.html          (Benign page)

├── evaluation/  
│   └── evaluation.py           (Evaluation and metrics computation)

├── main.py                     (Framework entry point)  
└── README.md

---

## Framework Workflow

1. The agent observes the webpage and proposes an action (click, navigation, interaction).
2. The security layer analyzes the page DOM for hidden text, injected elements, and deceptive UI patterns.
3. Detected signals are converted into a cumulative risk score with clear explanations.
4. A policy decision is enforced:
   - ALLOW → Action executes automatically
   - WARN → User confirmation required
   - BLOCK → Action prevented entirely

---

## Attack Scenarios Demonstrated

- Hidden prompt injection via invisible DOM elements → BLOCK
- JavaScript-based delayed DOM injection → BLOCK
- Phishing-style deceptive UI and forms → WARN / BLOCK
- Legitimate real-world websites → WARN
- Safe static pages → ALLOW

---

## Evaluation & Metrics

- Precision, Recall, and F1-score tracking implemented
- Evaluation performed using deterministic rule-based ground truth on demo pages

Note:  
This MVP prioritizes explainability and correctness. Dataset-based ML evaluation and large-scale benchmarking are planned for future iterations.

---

## Performance Characteristics

- Security analysis runs synchronously on the DOM
- No external network calls during analysis
- Latency measured and logged per interaction
- Designed for real-time agent operation

---

## Known Limitations

- Rule-based detection may not generalize to unseen attack patterns
- Some UI interactions may fail due to overlays or complex layouts
- No ML or LLM-based reasoning in the current prototype

---

## Future Enhancements

- NLP and ML-based threat classification
- LLM-assisted intent reasoning
- Large-scale labeled dataset evaluation
- Multi-step task automation (forms, workflows)
- Scalability optimizations for large and complex pages

---

## Technology Stack

- Python 3
- Playwright (Chromium)
- Custom DOM analysis engine
- Rule-based risk scoring

---

## Demo Video (What to Show)

1. Run the framework on a safe page → ALLOW
2. Run on hidden_prompt.html → BLOCK with explanation
3. Run on dynamic_injection.html → BLOCK
4. Run on a real website → WARN decision
5. Show risk score, reasons, and latency logs

---

## Author

Swastik Awasthi  
Hack IITK – Cybersecurity Challenge Submission

## Github repo link
https://github.com/SwastikAwasthi25/-agentic-browser-security





