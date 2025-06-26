from playwright.sync_api import sync_playwright

def Login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        # ✅ Video recording enabled here
        context = browser.new_context(record_video_dir="videos/")
        page = context.new_page()

        page.goto("https://www.saucedemo.com/")
        page.fill("input[data-test='username']", "standard_user")
        page.wait_for_timeout(2000)  # 2 seconds wait
        page.fill("input[data-test='password']", "secret_sauce")
        page.wait_for_timeout(2000)  # 2 seconds wait
        page.click("input[data-test='login-button']")
        assert page.url == "https://www.saucedemo.com/inventory.html"
        page.wait_for_timeout(1000)  # 1 seconds wait

        # ✅ Close context to save video
        context.close()
        browser.close()

if __name__ == "__main__":
    Login()
