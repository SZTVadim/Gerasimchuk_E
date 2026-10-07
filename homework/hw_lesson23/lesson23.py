from playwright.sync_api import Page, expect

url = 'https://www.qa-practice.com/forms/practice-form'


def test_visible(page: Page):
    page.goto(url)

    locator_first_name = page.locator("input[name=first_name]")
    locator_first_name.fill('Alice')
    expect(locator_first_name, 'Имя не ввелось').to_have_value('Alice')

    locator_last_name = page.locator("input[name=last_name]")
    locator_last_name.fill('Carlail')
    expect(locator_last_name, 'Фамилия не ввелась').to_have_value('Carlail')

    locator_email = page.locator("input[name=email]")
    locator_email.fill('alice123@mail.com')
    expect(locator_email, 'Мэйл не ввелся').to_have_value('alice123@mail.com')

    locator_gender = page.locator("input[value=Female]")
    locator_gender.click()
    expect(locator_gender).to_be_checked()

    locator_mobile = page.locator("input[name=mobile]")
    locator_mobile.fill('9099887776')
    expect(locator_mobile, 'Телефон не ввелся').to_have_value('9099887776')

    locator_birth = page.locator("input[name=date_of_birth]")
    locator_birth.fill('06 Oct 1901')
    expect(locator_birth, 'Дата рождения не ввелась').to_have_value('06 Oct 1901')

    locator_sub = page.locator("input#subjectsAutocomplete")
    locator_sub.fill('Math')
    locator_list = page.locator("div#subjectsSuggestions")
    locator_list.get_by_text("Maths").click()
    locator_span = page.locator("span[class=subject-tag]")
    expect(locator_span, 'Предмет не ввелся').to_have_text('Maths ×')

    locator_hobbies = page.locator("input#hobbies_0")
    locator_hobbies.click()
    expect(locator_hobbies).to_be_checked()

    locator_picture = page.locator("input[name=picture]")
    locator_picture.set_input_files("homework/hw_lesson23/pic.png")
    expect(locator_picture).to_have_value(r"C:\fakepath\pic.png")

    locator_textarea = page.locator("textarea#currentAddress")
    locator_textarea.fill('Forks, Washington')
    expect(locator_textarea).to_have_value("Forks, Washington")

    locator_dropdown = page.locator("div#div_id_state div.custom-dropdown-control")
    locator_dropdown.click()
    locator_option_state = page.locator("div.custom-dropdown-option[data-value=NCR]")
    locator_option_state.click()
    locator_select_value = page.locator("div#div_id_state span.selected-value")
    expect(locator_select_value).to_have_text("NCR")

    locator_dropdown = page.locator("div#div_id_city div.custom-dropdown-control")
    locator_dropdown.click()
    locator_option_state = page.locator("div.custom-dropdown-option[data-value=Delhi]")
    locator_option_state.click()
    locator_select_value = page.locator("div#div_id_city span.selected-value")
    expect(locator_select_value).to_have_text("Delhi")

    locator_submit_button = page.locator("input#submit-id-submit")
    locator_submit_button.click()
    locator_title = page.locator("h5#resultsModalLabel")
    expect(locator_title).to_have_text('Thanks for submitting the form')
