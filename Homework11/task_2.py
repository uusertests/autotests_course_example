# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста
import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
page = webdriver.Chrome(options=options)
page.get('https://fix-online.sbis.ru/')

# Указываем логин
time.sleep(2)
element_login = page.find_element(By.CSS_SELECTOR, 'input[name="Login"]')
element_login.send_keys('Демо')
element_login.send_keys(Keys.ENTER)
time.sleep(2)

# Указываем пароль и заходим в акк
element_password = page.find_element(By.CSS_SELECTOR, 'input[name="Password"]')
element_password.send_keys('Демо123')
element_password.send_keys(Keys.ENTER)
time.sleep(5)

# Открываем панель выбора адресата
page.find_element(By.CSS_SELECTOR, 'span[title="Написать сообщение"]').click()
time.sleep(5)

# Ищем адресата (самого себя)
element_search = page.find_element(By.XPATH, '//div[text()="Найти"]')
actions = ActionChains(page)
actions.move_to_element(element_search).click().send_keys('Демо_тензор').perform()
time.sleep(2)

# Выбираем адресата из списка
page.find_element(By.CSS_SELECTOR, '.person-BaseInfo').click()
time.sleep(2)

# Вводим текст сообщения
element_text_message = page.find_element(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph')
actions = ActionChains(page)
actions.move_to_element(element_text_message).click().send_keys('HW11').perform()
time.sleep(2)

# Отправляем сообщение
page.find_element(By.CSS_SELECTOR, 'span[data-qa="msg-send-editor__send-button"]').click()
time.sleep(3)

# Закрываем панель отправки сообщений
page.find_element(By.CSS_SELECTOR, 'span[data-qa="controls-stack-Button__close"]').click()
time.sleep(3)

# Открываем реестр сообщений
page.find_element(By.CSS_SELECTOR, 'a[data-qa="Контакты"]').click()
time.sleep(2)
page.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle').click()
time.sleep(5)

# Ищем сообщение в реестре
try:
    element_author = page.find_element(By.XPATH, '//div[text()="Демо_тензор Демо_тензор"]')
except selenium.common.exceptions.NoSuchElementException:
    print('В реестре нет сообщения от меня')

try:
    element_text = page.find_element(By.XPATH, '//p[text()="HW11"]')
except selenium.common.exceptions.NoSuchElementException:
    print('В реестре есть сообщение от меня, но нет с текстом из текущего теста')

# Удаляем сообщение
element_author = page.find_element(By.XPATH, '//p[text()="HW11"]')
actions = ActionChains(page)
actions.move_to_element(element_author).perform()
time.sleep(3)
page.find_element(By.CSS_SELECTOR, 'div[title="Перенести в удаленные"]').click()

# Ищем сообщение в реестре
try:
    element_author = page.find_element(By.XPATH, '//p[text()="HW11"]')
except selenium.common.exceptions.NoSuchElementException:
    print('Сообщение удалено!')

# Для красивого финала
time.sleep(3)
