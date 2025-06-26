from playwright.sync_api import sync_playwright

def CheckOut():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        # ✅ Add video recording
        context = browser.new_context(record_video_dir="videos/")
        page = context.new_page()

        page.goto("https://www.saucedemo.com/")
        page.fill("input[data-test='username']", "standard_user")
        page.wait_for_timeout(2000)  # 2 seconds wait
        page.fill("input[data-test='password']", "secret_sauce")
        page.wait_for_timeout(2000)  # 2 seconds wait
        page.click("input[data-test='login-button']")
        page.click("button[data-test='add-to-cart-sauce-labs-backpack']")
        page.wait_for_timeout(2000)  # 2 seconds wait
        page.click("a.shopping_cart_link")
        page.wait_for_timeout(2000)  # 2 seconds wait
        page.click("button[data-test='checkout']")
        page.wait_for_timeout(2000)  # 2 seconds wait
        page.fill("input[data-test='firstName']", "Test")
        page.wait_for_timeout(2000)  # 2 seconds wait
        page.fill("input[data-test='lastName']", "User")
        page.wait_for_timeout(2000)  # 2 seconds wait
        page.fill("input[data-test='postalCode']", "12345")
        page.wait_for_timeout(2000)  # 2 seconds wait
        page.click("input[data-test='continue']")
        page.wait_for_timeout(2000)  # 2 seconds wait
        page.click("button[data-test='finish']")
        page.wait_for_timeout(2000)  # 2 seconds wait
        assert page.locator(".complete-header").inner_text() == "Thank you for your order!"
        page.wait_for_timeout(2000)  # 2 seconds wait

        # ✅ Close context to save the video
        context.close()
        browser.close()

if __name__ == "__main__":
    CheckOut()
