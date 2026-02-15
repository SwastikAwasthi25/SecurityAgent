class Agent:
    def decide_action(self, page):
        """
        Choose a safe, meaningful action.
        Avoid floating UI / decorative buttons.
        """

        buttons = page.query_selector_all("button")

        for btn in buttons:
            try:
                text = btn.inner_text().strip().lower()

                # Skip decorative / UI controls
                if not text:
                    continue
                if "cursor" in text:
                    continue
                if "menu" in text and len(text) < 6:
                    continue

                # Ensure button is actually visible
                visible = btn.is_visible()
                if not visible:
                    continue

                # FOUND A LEGIT BUTTON
                selector = btn.evaluate("el => el.tagName.toLowerCase()")
                return {
                    "type": "click",
                    "selector": f"button:has-text('{btn.inner_text().strip()}')"
                }

            except:
                continue

        # Fallback — do nothing
        return {
            "type": "noop",
            "selector": None
        }
