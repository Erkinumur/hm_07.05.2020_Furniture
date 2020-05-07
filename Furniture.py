class House:
    def __init__(self, household_type, total_area):
        self.household_type = household_type
        self.total_area = total_area
        self.remaining_area = total_area
        self.furniture_list = []
    
    def __str__(self):
        return f'Household type: {self.household_type}, total area: {self.total_area}, remaining area: {self.remaining_area}, furniture name list: {self.furniture_list}'

    def add_furniture(self, *args):
        furniture_area = {'Bed': 4, 'Wardrobe': 2, 'Table': 1.5}
        furniture_list = list(args)
        for i in args:
            if self.remaining_area - furniture_area[i] >= 0:
                self.furniture_list.append(i)
                self.remaining_area -= furniture_area[i]
                furniture_list.remove(i)
            else:
                print('Оставшиеся вещи не поместятся: ', furniture_list)
                break

house = House('simple_house', 50)
house.add_furniture('Bed', 'Wardrobe', 'Table', 'Bed', 'Table', 'Table', 'Wardrobe', 'Table')
print(house)
