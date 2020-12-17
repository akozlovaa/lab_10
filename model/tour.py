class Tour:
    tour_agency_name = "IoT Tours"

    def __init__(self, country=None, num_of_days=None, amt_of_hryvnias=None,
                 num_of_tourists=None,
                 hotel_name=None, transport_type=None):
        self.country = country
        self.num_of_days = num_of_days
        self.amt_of_hryvnias = amt_of_hryvnias
        self.num_of_tourists = num_of_tourists
        self.hotel_name = hotel_name
        self.transport_type = transport_type

    @staticmethod
    def staticmethod():
        return Tour.tour_agency_name

    def __str__(self):
        tour_agency_name = "Tour agency: {0};\n".format(Tour.tour_agency_name)
        country = "Country of destination: {0};\n".format(self.country)
        num_of_days = "Duration in days: {0};\n".format(self.num_of_days)
        amt_of_hryvnias = "Price in Ukrainian Hryvnias: {0};\n".format(self.amt_of_hryvnias)
        num_of_tourists = "How many people are going: {0};\n".format(self.num_of_tourists)
        hotel_name = "Designated hotel: {0};\n".format(self.hotel_name)
        transport_type = "Transportation type: {0}.\n".format(self.transport_type)

        return tour_agency_name + country + num_of_days + amt_of_hryvnias + num_of_tourists + hotel_name + transport_type

    def __del__(self):
        print("Delete " + self.__class__.__name__ + " | Object ID: " + str(id(self)))
        return


"""
1. Дописати ще одну статичну змінну і статичний метод, який повертає значення цієї змінної
2. Дописати приватну змінну і публічний метод, що встановлює її значення
3. Дописати приватну змінну і публічний метод, що повертає її значення
4. Створити масив обєктів і вивести їх в консоль з використанням 
"""
