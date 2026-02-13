

class App:

    def __init__(self, database):
        self.database = database
    def save_data(self, data):
        self.database.save(data)

class MySQLDatabase:

    def save(self, data):
        print(f"Saving data to MySQL Database: {data}")




app = App(MySQLDatabase())
app.save_data("Sample Data")




