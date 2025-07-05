from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    print("Starting browser...")
    browser = p.chromium.launch(headless=False)
    print("Browser started")
    page = browser.new_page()
    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"
    )
    print("Page opened")
    email_input = page.locator(
        '//div[@data-testid="login-form-email-input"]//div//input'
    )
    email_input.fill("user.name@gmail.com")
    password_input = page.locator(
        '//div[@data-testid="login-form-password-input"]//div//input'
    )
    password_input.fill("password")

    # Находим кнопку "Login" и кликаем на нее
    login_button = page.locator('//button[@data-testid="login-page-login-button"]')
    login_button.click()

    # Проверяем, что появилось сообщение об ошибке
    wrong_email_or_password_alert = page.locator(
        '//div[@data-testid="login-page-wrong-email-or-password-alert"]'
    )
    expect(
        wrong_email_or_password_alert
    ).to_be_visible()  # Проверяем видимость элемента
    expect(wrong_email_or_password_alert).to_have_text(
        "Wrong email or password"
    )  # Проверяем текст

    # Пауза на 5 секунд, чтобы увидеть результат

    page.wait_for_timeout(5000)
