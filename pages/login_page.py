from playwright.sync_api import Page

from components.authentication import LoginFormComponent
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Класс, представляющий страницу входа в систему.

    Атрибуты:
        form (LoginFormComponent): Форма для ввода логина и пароля.
        login_btn: Локатор кнопки "Войти".
        registration_link: Локатор ссылки на страницу регистрации.
        title_page: Локатор заголовка страницы.
        wrong_email_or_password_alert: Локатор уведомления об ошибке при вводе неправильной почты или пароля.

    Методы:
        click_login_btn: Кликает по кнопке "Войти".
        click_registration_link: Кликает по ссылке "Зарегистрироваться".
        check_visible_login_page_title: Проверяет видимость заголовка страницы.
        check_visible_wrong_email_or_password_alert: Проверяет видимость сообщения об ошибке.
    """

    def __init__(self, page: Page):
        """
        Инициализирует объект LoginPage и связанные с ним элементы.

        Аргументы:
            page (Page): Экземпляр страницы браузера.
        """
        super().__init__(page)

        self.form = LoginFormComponent(page)

        self.login_btn = page.get_by_test_id("login-page-login-button")
        self.registration_link = page.get_by_test_id("login-page-registration-link")
        self.title_page = page.get_by_test_id("authentication-ui-course-title-text")
        self.wrong_email_or_password_alert = page.get_by_test_id(
            "login-page-wrong-email-or-password-alert"
        )

    def click_login_btn(self):
        """
        Кликает по кнопке "Войти" после проверки её видимости.
        """
        self.check_locator(self.login_btn)
        self.login_btn.click()

    def click_registration_link(self):
        """
        Кликает по ссылке "Зарегистрироваться" после проверки её видимости.
        """
        self.check_locator(self.registration_link)
        self.registration_link.click()

    def check_visible_login_page_title(self):
        """
        Проверяет, что заголовок страницы отображается корректно.
        """
        self.check_locator(self.title_page, "UI Course")

    def check_visible_wrong_email_or_password_alert(self):
        """
        Проверяет, что отображается уведомление о неверной электронной почте или пароле.
        """
        self.check_locator(
            self.wrong_email_or_password_alert, "Wrong email or password"
        )
