from playwright.sync_api import sync_playwright


def get_page(url):
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    try:
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
    except Exception as e:
        print("[WARNING] Page did not fully load:", e)

    return page, browser, p


def execute_action(page, action):
    if action["type"] == "noop":
        print("[NO ACTION]")
        return

    try:
        page.click(action["selector"], timeout=5000)
        print("[ACTION] Click executed successfully")

    except Exception as e:
        print("[ACTION FAILED]")
        print("Reason:", str(e))
        print("[INFO] Action blocked by UI / overlay — not bypassing for safety")

