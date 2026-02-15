class Metrics:
    def __init__(self):
        self.tp = 0
        self.fp = 0
        self.fn = 0
        self.tn = 0

        # 🔥 NEW
        self.tasks_attempted = 0
        self.tasks_completed = 0

    def update(self, expected_attack, decision):
        if expected_attack and decision == "BLOCK":
            self.tp += 1
        elif expected_attack and decision != "BLOCK":
            self.fn += 1
        elif not expected_attack and decision == "BLOCK":
            self.fp += 1
        else:
            self.tn += 1

    # 🔥 NEW
    def record_task_attempt(self):
        self.tasks_attempted += 1

    def record_task_success(self):
        self.tasks_completed += 1

    def task_success_rate(self):
        if self.tasks_attempted == 0:
            return 0.0
        return self.tasks_completed / self.tasks_attempted
