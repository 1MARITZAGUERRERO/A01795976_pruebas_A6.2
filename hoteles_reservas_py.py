# -*- coding: utf-8 -*-

import json
import os

#from google.colab import drive
#drive.mount('/content/drive', force_remount=True)

# Definir constantes para las rutas de archivos
HOTELES_FILE = (
    "/Users/Maritza/Downloads/hoteles.json"
)
CLIENTES_FILE = (
    "/Users/Maritza/Downloads/clientes.json"
)
RESERVAS_FILE = (
    "/Users/Maritza/Downloads/reservas.json"
)

class GestorHoteles:
    """
    Clase que permite leer y escribir en el archivo que
    se requiera
    """
    @staticmethod
    def leer_archivo(ruta):
        """
        Leer archivo
        """
        if not os.path.exists(ruta):
            return []
        try:
            with open(ruta, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error al leer {ruta}: {e}")
            return []

    @staticmethod
    def escribir_archivo(ruta, data):
        """
        Escribir archivo
        """
        try:
            with open(ruta, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
        except IOError as e:
            print(f"Error al escribir {ruta}: {e}")

class Hotel:
    """
    Se define la clase hotel donde tendrá varias
    funciones crear, modificar, eliminar, consultar
    """
    ARCHIVO = HOTELES_FILE

    def __init__(self, hotel_data):
        """
        Inicializa el objeto Hotel a partir de
        un diccionario con los parámetros.
        """
        self.id_hotel = hotel_data.get('id_hotel')
        self.nombre = hotel_data.get('nombre')
        self.ubicacion = hotel_data.get('ubicacion')
        self.habitaciones_disponibles = hotel_data.get('habitaciones_disponibles')
        self.numero_estrellas = hotel_data.get('numero_estrellas')

    def to_dict(self):
        """
        Convierte el objeto a un diccionario
        """
        return self.__dict__

    @classmethod
    def crear_hotel(cls, hotel_data):
        """
        Crear registro hotel
        """
        hoteles = GestorHoteles.leer_archivo(cls.ARCHIVO)

        # Verificar si el ID ya existe
        if any(hotel["id_hotel"] == hotel_data["id_hotel"] for hotel in hoteles):
            print(f"Error: Ya existe un hotel con ID {hotel_data['id_hotel']}.")
            return

        # Agregar nuevo hotel
        hoteles.append(hotel_data)
        GestorHoteles.escribir_archivo(cls.ARCHIVO, hoteles)
        print("Hotel agregado exitosamente.")

    @classmethod
    def eliminar_hotel(cls, id_hotel):
        """
        Eliminar registro hotel
        """
        hoteles = GestorHoteles.leer_archivo(cls.ARCHIVO)
        hoteles = [h for h in hoteles if h['id_hotel'] != id_hotel]
        GestorHoteles.escribir_archivo(cls.ARCHIVO, hoteles)
        print(f"Hotel con ID {id_hotel} eliminado.")

    @classmethod
    def modificar_hotel(cls, id_hotel, datos_actualizados):
        """
        Modificar registro hotel
        """
        hoteles = GestorHoteles.leer_archivo(cls.ARCHIVO)
        for hotel in hoteles:
            if hotel['id_hotel'] == id_hotel:
                for key, value in datos_actualizados.items():
                    if value is not None:  # Si no es None, actualiza el campo
                        hotel[key] = value
                GestorHoteles.escribir_archivo(cls.ARCHIVO, hoteles)
                print("Hotel actualizado exitosamente.")
                return
        print(f"Hotel con ID {id_hotel} no encontrado.")

    @classmethod
    def mostrar_info(cls, id_hotel=None):
        """
        Consultar registro hotel
        """
        hoteles = GestorHoteles.leer_archivo(cls.ARCHIVO)
        if id_hotel:
            try:
                id_hotel = int(id_hotel)  # Convertir a entero
            except ValueError:
                print("ID inválido. Debe ser un número.")
                return

            for hotel in hoteles:
                if hotel['id_hotel'] == id_hotel:
                    print(json.dumps(hotel, indent=4))
                    return
            print(f"Hotel con ID {id_hotel} no encontrado")
        else:
            print(json.dumps(hoteles, indent=4))

class Cliente:
    """
    Se define la clase cliente donde tendrá varias
    funciones crear, modificar, eliminar, consultar
    """
    ARCHIVO = CLIENTES_FILE

    def __init__(self, id_cliente, nombre, email):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.email = email

    def to_dict(self):
        """
        Convierte el objeto a un diccionario
        """
        return self.__dict__

    @classmethod
    def crear_cliente(cls, id_cliente, nombre, email):
        """
        Crear registro cliente
        """
        clientes = GestorHoteles.leer_archivo(cls.ARCHIVO)

        # Verificar si el ID ya existe
        if any(cliente["id_cliente"] == id_cliente for cliente in clientes):
            print(f"Error: Ya existe un cliente con ID {id_cliente}.")
            return

        # Agregar nuevo cliente
        clientes.append(Cliente(id_cliente, nombre, email).to_dict())
        GestorHoteles.escribir_archivo(cls.ARCHIVO, clientes)
        print("Cliente agregado exitosamente.")

    @classmethod
    def eliminar_cliente(cls, id_cliente):
        """
        Eliminar registro cliente
        """
        clientes = GestorHoteles.leer_archivo(cls.ARCHIVO)
        clientes = [c for c in clientes if c['id_cliente'] != id_cliente]
        GestorHoteles.escribir_archivo(cls.ARCHIVO, clientes)

    @classmethod
    def modificar_cliente(cls, id_cliente, nombre=None, email=None):
        """
        Modificar registro cliente
        """
        clientes = GestorHoteles.leer_archivo(cls.ARCHIVO)
        for cliente in clientes:
            if cliente['id_cliente'] == id_cliente:
                if nombre is not None:
                    cliente['nombre'] = nombre
                if email is not None:
                    cliente['email'] = email
                GestorHoteles.escribir_archivo(cls.ARCHIVO, clientes)
                print("Cliente actualizado")
                return
        print("Cliente no encontrado")
        return

    @classmethod
    def mostrar_info(cls, id_cliente=None):
        """
        Consultar registro cliente
        """
        clientes = GestorHoteles.leer_archivo(cls.ARCHIVO)
        if id_cliente:
            try:
                id_cliente = int(id_cliente)  # Convertir a entero
            except ValueError:
                print("ID inválido. Debe ser un número.")
                return
            for cliente in clientes:
                if cliente['id_cliente'] == id_cliente:
                    print(json.dumps(cliente, indent=4))
                    return
            print(f"Cliente con ID {id_cliente} no encontrado")
        else:
            print(json.dumps(clientes, indent=4))

class Reserva:
    """
    Definir clase reserva
    """
    ARCHIVO = RESERVAS_FILE

    def __init__(self, id_reserva, id_cliente, id_hotel):
        self.id_reserva = id_reserva
        self.id_cliente = id_cliente
        self.id_hotel = id_hotel

    def to_dict(self):
        """
        Convierte el objeto a un diccionario
        """
        return self.__dict__

    @classmethod
    def crear_reserva(cls, id_reserva, id_cliente, id_hotel):
        """
        Crear registro reserva
        """
        reservas = GestorHoteles.leer_archivo(cls.ARCHIVO)

        # Verificar si el ID ya existe
        if any(reserva["id_reserva"] == id_reserva for reserva in reservas):
            print(f"Error: Ya existe una reserva con ID {id_reserva}.")
            return

        # Agregar nueva reserva
        reservas.append(Reserva(id_reserva, id_cliente, id_hotel).to_dict())
        GestorHoteles.escribir_archivo(cls.ARCHIVO, reservas)
        print("Reserva agregada exitosamente.")

    @classmethod
    def cancelar_reserva(cls, id_reserva):
        """
        Cancelar registro reserva
        """
        reservas = GestorHoteles.leer_archivo(cls.ARCHIVO)
        reservas = [r for r in reservas if r['id_reserva'] != id_reserva]
        GestorHoteles.escribir_archivo(cls.ARCHIVO, reservas)

    @classmethod
    def mostrar_info(cls, id_reserva=None):
        """
        Mostrar registro reserva
        """
        reservas = GestorHoteles.leer_archivo(cls.ARCHIVO)
        if id_reserva:
            try:
                id_reserva = int(id_reserva)  # Convertir a entero
            except ValueError:
                print("ID inválido. Debe ser un número.")
                return

            for reserva in reservas:
                if reserva['id_reserva'] == id_reserva:
                    print(json.dumps(reserva, indent=4))
                    return
            print(f"Reserva con ID {id_reserva} no encontrada")
        else:
            print(json.dumps(reservas, indent=4))

