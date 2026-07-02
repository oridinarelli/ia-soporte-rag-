class MemoriaConversacional:
    def __init__(self):
        self.historial = []

    def agregar(self, mensaje):
        self.historial.append(mensaje)

    def obtener_historial(self):
        return self.historial

    def limpiar(self):
        self.historial = []