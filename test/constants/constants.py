import allure


class Constants:
    def __init__(self):
        print("constants loaded")

    @staticmethod
    def app_url():
        return "https://app.vwo.com"

    @staticmethod
    def app_dashboard_url():
        return "https://app.vwo.com/#/dashboard"
