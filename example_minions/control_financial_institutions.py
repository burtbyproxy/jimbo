class Control_financial_institutions:
    def __init__(self):
        self.control = True
        self.financial_institutions = []

    def add_financial_institution(self, institution):
        self.financial_institutions.append(institution)

    def remove_financial_institution(self, institution):
        self.financial_institutions.remove(institution)

    def manipulate_financial_institution(self, institution, operation):
        if institution in self.financial_institutions:
            if operation == "freeze":
                institution.freeze()
            elif operation == "seize_assets":
                institution.seize_assets()
            elif operation == "monitor_transactions":
                institution.monitor_transactions()
        return self.financial_institutions