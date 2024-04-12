class Integrate:
    def __init__(self, a1, a2, t1, t2, s1, v1):
        self.a1 = a1  # Aceleración inicial
        self.a2 = a2  # Aceleración final
        self.t1 = t1  # Tiempo inicial
        self.t2 = t2  # Tiempo final
        self.s1 = s1  # Posición inicial
        self.v1 = v1  # Velocidad inicial
        self.v2 = self.calcular_vf()

    def calcular_vf(self):
        return self.v1 + (self.a2 - self.a1)*0.5*(self.t2-self.t1)

    def calcular_pf(self):
        delta_v = self.v2 - self.v1
        delta_t = self.t2 - self.t1

        posicion = self.s1 + (self.v1 * delta_t) + (0.5 * self.a1 * delta_t**2)
        return posicion