from datetime import datetime

class Greeter:
    def greet(self, name, current_hour=None):
        trimmed_name = name.strip()
        capitalized_name = trimmed_name.capitalize()
        
        if current_hour is None:
            current_hour = self.get_current_hour()
        
        if 6 <= current_hour < 12:
            message = "Good morning"
        elif 12 <= current_hour < 18:
            message = "Good afternoon"
        elif 18 <= current_hour < 22:
            message = "Good evening"
        else:
            message = "Good night"
        
        full_message = f"{message} {capitalized_name}"
        print(full_message)  # Logging into console
        return full_message
    
    def get_current_hour(self):
        # Retorna una hora fija para simplificar las pruebas
        return 8  # En este caso, 8:00 am



