from playwright.sync_api import sync_playwright

def Add_To_Cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        # ✅ Add video recording line here
        context = browser.new_context(record_video_dir="videos/")
        page = context.new_page()

        page.goto("https://www.saucedemo.com/")
        page.fill("input[data-test='username']", "standard_user")
        page.wait_for_timeout(2000)  # 2 seconds wait
        page.fill("input[data-test='password']", "secret_sauce")
        page.wait_for_timeout(2000)  # 2 seconds wait
        page.click("input[data-test='login-button']")
        page.wait_for_timeout(2000)  
        page.click("button[data-test='add-to-cart-sauce-labs-backpack']")
        page.wait_for_timeout(1000)  # 1 seconds wait
        assert page.locator("span.shopping_cart_badge").inner_text() == "1"
        page.wait_for_timeout(1000)  # 1 seconds wait

        # ✅ Close context to save the video
        context.close()
        browser.close()

if __name__ == "__main__":
    Add_To_Cart()
