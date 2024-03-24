from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from app.core.config import settings
from app.core.logger import logger


class WebDriverCurrent:
    AVITO_BASE: str = "https://www.avito.ru/"

    def __init__(self):
        self.options = self._get_default_options()

    def _get_default_options(self):
        try:
            options = webdriver.ChromeOptions()
            prefs = {"profile.managed_default_content_settings.images": 2}
            options.add_argument("--headless")
            options.add_argument("--disable-extensions")
            options.add_argument("--blink-settings=imagesEnabled=false")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-background-networking")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--log-level=3")  # fatal
            options.add_argument("--ignore-certificate-errors-spki-list")
            options.add_experimental_option("prefs", prefs)
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            options.add_argument("window-size=1920,1080")
            options.add_argument("--disable-extensions")
            options.add_argument("--proxy-server='direct://'")
            options.add_argument("--proxy-bypass-list=*")
            options.add_argument("--start-maximized")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-browser-side-navigation")
            options.add_argument("--disable-infobars")
            options.add_argument("--disable-features=site-per-process")
            options.add_argument("--enable-features=NetworkServiceInProcess")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-default-apps")
            options.add_argument("--disable-translate")
            logger.info(f"web_driver_current: Установка опций браузера...")
            return options
        except Exception as e:
            logger.info(f"web_driver_current: Ошибка настроек браузера: {e}")


    def _get_driver(self):
        """
        Получение драйвера веб браузера


            from selenium.webdriver.chrome.service import Service as ChromeService
            from webdriver_manager.chrome import ChromeDriverManager

            if settings.ENVIRONMENT == 'local':
                 # для локальной разработки
                 chrome = ChromeDriverManager().install()
                 driver = webdriver.Chrome(
                      service=ChromeService(chrome), options=self.options
                  )
            else:
                # для продакшн
                 executor = f'http://{settings.SELENIUM_HUB_HOST}:4444/wd/hub'
                driver = webdriver.Remote(command_executor=executor, options=self.options)
                return driver

        Returns: driver

        """
        try:
            logger.info("web_driver_current: Начался процесс получения драйвера")
            executor = f'http://{settings.SELENIUM_HUB_HOST}:4444/wd/hub'
            driver = webdriver.Remote(command_executor=executor, options=self.options)
            logger.info("web_driver_current: Драйвер браузера успешно получен")
            return driver
        except Exception as e:
            logger.warning(f"web_driver_current: Ошибка при получении драйвера браузера: `{e}`")

    def _add_cookie(self, driver, cookie=None):
        """Куки для сеанса"""
        logger.info("web_driver_current: Начался процесс установки COOKIE")
        try:
            if cookie is None:
                cookie = {"name": "view", "value": "gallery"}
            driver.get(self.AVITO_BASE)
            driver.add_cookie(cookie)
            logger.info("web_driver_current: Процесс получения COOKIE успешно закончен")
            return driver
        except Exception as e:
            logger.warning(f"web_driver_current: Ошибка в процесс получения COOKIE: {e} ")

    def get_source_page(self, url, num_page: int):
        driver = None
        logger.info("web_driver_current: Процесс получения содержимого HTML страницы")
        try:
            driver = self._add_cookie(self._get_driver())
            driver.get(f"{url}&p={num_page or 1}")
            source = driver.page_source
            logger.info("web_driver_current: Содержимое HTML страницы успешно получено")
            return self._get_html(source)
        except Exception as e:
            logger.warning(f"web_driver_current: Ошибка в процессе получения HTML страницы: {e}")
        finally:
            if driver is not None:
                driver.quit()
                logger.info("web_driver_current: Драйвер отключен")

    def get_video_element(self, url):
        driver = None
        try:
            logger.info("web_driver_current: Получение HTML кода с видео плеером")
            driver = self._get_driver()
            driver.get(f"{url}")
            # Найти первый элемент, чей class начинается с "images-preview-previewImageWrapper_video-"
            element = driver.find_element(
                by=By.CSS_SELECTOR,
                value="[class*='images-preview-previewImageWrapper_video']",
            )

            element.click()
            button = driver.find_element(
                by=By.CSS_SELECTOR, value="[class*='videoPlayer-button']"
            )
            button.click()

            source = driver.page_source
            return self._get_html(source)
        except Exception as e:
            print(f"{e}")
        finally:
            if driver is not None:
                driver.quit()

    def get_source_full_page(self, url):
        driver = None

        try:
            driver = self._get_driver()
            driver.get(f"{url}")
            source = driver.page_source
            return self._get_html(source)
        except Exception as e:
            print(f"{e}")
        finally:
            if driver is not None:
                driver.quit()

    def _get_html(self, source: str) -> BeautifulSoup:
        """Получить содержимого в формате BS4"""
        return BeautifulSoup(source, "html.parser")
