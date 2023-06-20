# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста
# Импортируем необходимые модули
import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
page = webdriver.Chrome(options=options)
page.get('https://sbis.ru/')

# Находим ссылку Контакты по CSS-селектору и кликаем в него
element_contacts = page.find_element(By.CSS_SELECTOR, 'a[href="/contacts"]')
element_contacts.click()

# Находим ссылку на сайт tensor.ru по CSS-селектору и кликаем в него
time.sleep(1)
element_tensor = page.find_element(By.CSS_SELECTOR, 'img[alt="Разработчик системы СБИС — компания «Тензор»"]')
element_tensor.click()

# Получаем список всех открытых вкладок браузера
windows = page.window_handles

# Переключаемся на вторую вкладку
page.switch_to.window(windows[1])

# Прокрутить страницу до искомого элемента
target_element_locator = By.XPATH, '//a[@class="tensor_ru-link tensor_ru-Index__link" and text()="Подробнее"]'
target_element = WebDriverWait(page, 10).until(EC.presence_of_element_located(target_element_locator))
page.execute_script("arguments[0].scrollIntoView();", target_element)

# Проверяем наличие блока Сила в людях
try:
    element = page.find_element(By.XPATH, '//p[text()="Сила в людях"]')
except selenium.common.exceptions.NoSuchElementException:
    print('На странице нет блока "Сила в людях"')

# Кликаем в ссылку Подробнее
element_link_more = page.find_element(By.CSS_SELECTOR, 'a[href="/about"].tensor_ru-link.tensor_ru-Index__link')
element_link_more.click()

try:
    assert page.current_url == 'https://tensor.ru/about'
except AssertionError:
    print(f'Вместо сайта https://tensor.ru/about перешли на {page.current_url}')

# Закрытие браузера
page.quit()
