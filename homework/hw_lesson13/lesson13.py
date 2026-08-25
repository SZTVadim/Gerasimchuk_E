class TestCase:
    def __init__(self, name, status="new", duration=None):
        self.name = name
        self.status = status
        self.duration = duration

    def can_run(self):
        if self.status == "new":
            return True
        return False

    def finish(self, result, duration):
        if not self.can_run():
            return False
        if result not in ["passed", "failed"]:
            return False
        self.status = result
        self.duration = duration
        return True

    def is_slow(self):
        if self.duration is None:
            return None
        if self.duration >= 5:
            return True
        return False


test1 = TestCase("test1")
test2 = TestCase("test2", duration=2)
test2.finish('ok', 4)
test3 = TestCase("test3", duration=5)
test3.finish('passed', 10)

print(test1.name, test1.can_run(), test1.status, test1.is_slow(), test1.status)
print(test2.name, test2.can_run(), test2.status, test2.is_slow(), test2.status)
print(test3.name, test3.can_run(), test3.status, test3.is_slow(), test3.status)
