statuses = ["queued", "running", "testing", "deploy", "done"]
first, *middle, last = statuses
statuses2 = [*middle, *["failed", "skipped"]]
print(first)
print(last)
print(statuses2)

browser = {"browser": "chrome", "timeout": 3000}
options = {"headless": True, "timeout": 5000}


def start_session(browser, timeout, headless):
    return f"{browser}, timeout={timeout}, headless={headless}"


config = {**browser, **options}
str1 = start_session(**config)
print(config)
print(str1)
