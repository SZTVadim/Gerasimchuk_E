from playwright.sync_api import Page, expect

url = 'https://www.qa-practice.com/forms/practice-form'


def test_visible(page: Page):
    page.goto(url)

    locator_first_name = page.locator("input[name=first_name]")
    locator_first_name.fill('Alice')

    locator_last_name = page.locator("input[name=last_name]")
    locator_last_name.fill('Carlail')

    locator_email = page.locator("input[name=email]")
    locator_email.fill('alice123@mail.com')

    locator_gender = page.locator("input[value=Female]")
    locator_gender.click()

    locator_mobile = page.locator("input[name=mobile]")
    locator_mobile.fill('9099887776')

    locator_birth = page.locator("input[name=date_of_birth]")
    locator_birth.fill('06 Oct 1901')

    locator_sub = page.locator("input#subjectsAutocomplete")
    locator_sub.fill('Math')
    locator_list = page.locator("div#subjectsSuggestions")
    locator_list.get_by_text("Maths").click()

    locator_hobbies = page.locator("input#hobbies_0")
    locator_hobbies.click()

    locator_picture = page.locator("input[name=picture]")
    locator_picture.set_input_files("homework/hw_lesson23/pic.png")

    locator_textarea = page.locator("textarea#currentAddress")
    locator_textarea.fill('Forks, Washington')

    locator_dropdown = page.locator("div#div_id_state div.custom-dropdown-control")
    locator_dropdown.click()
    locator_option_state = page.locator("div.custom-dropdown-option[data-value=NCR]")
    locator_option_state.click()

    locator_dropdown = page.locator("div#div_id_city div.custom-dropdown-control")
    locator_dropdown.click()
    locator_option_state = page.locator("div.custom-dropdown-option[data-value=Delhi]")
    locator_option_state.click()

    locator_submit_button = page.locator("input#submit-id-submit")
    locator_submit_button.click()

    locator_title = page.locator("h5#resultsModalLabel")
    expect(locator_title).to_have_text('Thanks for submitting the form')

    locator_res_name = page.locator("//tr[1]/td[2]")
    expect(locator_res_name).to_have_text("Alice Carlail")

    locator_res_email = page.locator("//tr[2]/td[2]")
    expect(locator_res_email).to_have_text("alice123@mail.com")

    locator_res_gender = page.locator("//tr[3]/td[2]")
    expect(locator_res_gender).to_have_text("Female")

    locator_res_mobile = page.locator("//tr[4]/td[2]")
    expect(locator_res_mobile).to_have_text("9099887776")

    locator_res_birth = page.locator("//tr[5]/td[2]")
    expect(locator_res_birth).to_have_text('1901-10-06')

    locator_res_sub = page.locator("//tr[6]/td[2]")
    expect(locator_res_sub).to_have_text('Maths')

    locator_res_hobbies = page.locator("//tr[7]/td[2]")
    expect(locator_res_hobbies).to_have_text("Sports")

    locator_res_picture = page.locator("//tr[8]/td[2]")
    expect(locator_res_picture).to_have_text("pic.png")

    locator_res_address = page.locator("//tr[9]/td[2]")
    expect(locator_res_address).to_have_text("Forks, Washington")

    locator_res_state_and_city = page.locator("//tr[10]/td[2]")
    expect(locator_res_state_and_city).to_have_text("NCR")
