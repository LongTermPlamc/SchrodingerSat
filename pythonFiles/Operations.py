class Operations:
    def __init__(self,variable,tipo):
        self.variable=variable
        self.tipo=tipo
    def operar(self):
        operaciones = {
            '1': lambda x: x / 100,  # aceleraciones
            '2': lambda x: x / 10,   # temperatura
            '3': lambda x: 101325 - x,  # presion
            '4': lambda x: x / 100,  # altura
            '5': lambda x: (x * 1000) / 8.75,  # gyro
        }

        if self.tipo in operaciones:
            self.variable = operaciones[self.tipo](self.variable)
        else:
            print("Tipo no reconocido")