from selene import browser, have


def test_todos():
    browser.open('https://todomvc.com/examples/preact/dist')
    # Поиск одного элемента
    new_todo = browser.element('.new-todo')
    #
    new_todo.type('First task').press_enter()
    new_todo.type('Second task').press_enter()
    new_todo.type('Third task').press_enter()

    # Поиск всех элементов с определённым локатором
    todo_items = browser.all('.todo-list li')

    # Проверка коллекции элементов
    todo_items.should(
        have.exact_texts('First task', 'Second task', 'Third task'))
    # или, например, проверим, что в каждом элементе списка есть слово `task`
    todo_items.should(have.text('task').each)