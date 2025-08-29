class Smartphone:
    def __init__(self, brand, model, storage_gb, battery_mah):
        self.brand = brand
        self.model = model
        self.__storage_gb = storage_gb  # private attribute
        self.battery_mah = battery_mah

    def get_storage(self):
        return self.__storage_gb

    def set_storage(self, new_storage):
        if new_storage > 0:
            self.__storage_gb = new_storage
        else:
            print("Storage must be positive!")

    def describe(self):
        return f"{self.brand} {self.model} with {self.__storage_gb}GB storage and {self.battery_mah}mAh battery."

    def battery_life(self, screen_time_hours):
        consumption_per_hour = 400
        remaining = self.battery_mah - consumption_per_hour * screen_time_hours
        return max(remaining, 0)


class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage_gb, battery_mah, cooling_system, rgb_lighting):
        super().__init__(brand, model, storage_gb, battery_mah)
        self.cooling_system = cooling_system
        self.rgb_lighting = rgb_lighting

    def describe(self):
        base = super().describe()
        lighting = "with RGB lighting" if self.rgb_lighting else "without RGB lighting"
        return f"{base} It has {self.cooling_system} cooling and {lighting}."

    def game_performance(self, game_name):
        print(f"Running {game_name} at high settings smoothly!")


# Example objects
phone1 = Smartphone("Samsung", "Galaxy S21", 128, 4000)
print(phone1.describe())
print(f"Battery left after 5 hours: {phone1.battery_life(5)}mAh")

gaming_phone = GamingSmartphone("Asus", "ROG Phone 5", 256, 6000, "Liquid Cooling", True)
print(gaming_phone.describe())
gaming_phone.game_performance("Call of Duty Mobile")

gaming_phone.set_storage(512)
print(f"New storage: {gaming_phone.get_storage()}GB")
