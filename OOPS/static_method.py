class ChaiUtils:

    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]
    
raw=" mil, cofee    , sugar, tea   "

print(ChaiUtils.clean_ingredients(raw))