# -*- coding: utf-8 -*-

import sys
sys.path.append('/Users/Maritza/Downloads/')
from hoteles_reservas_py import Hotel, Cliente, Reserva, GestorHoteles

import unittest
from unittest.mock import patch
from io import StringIO
import json

class TestHotel(unittest.TestCase):

    def setUp(self):
        self.hotel_data = {
            "id_hotel": 2,
            "nombre": "Hotel Dos",
            "ubicacion": "Ciudad Dos",
            "capacidad": 70,
            "estrellas": 3
        }
    
    def crear_hotel_prueba(self, id_hotel, nombre, ubicacion, capacidad, estrellas):
        return {
            "id_hotel": id_hotel,
            "nombre": nombre,
            "ubicacion": ubicacion,
            "capacidad": capacidad,
            "estrellas": estrellas
        }

    def tearDown(self):
        """Limpieza después de cada prueba, si es necesario"""
        pass

    @patch('hoteles_reservas_py.GestorHoteles.leer_archivo', return_value=[{"id_hotel": 2, "nombre": "Hotel Antiguo", "ubicacion": "Ciudad X"}])
    @patch('hoteles_reservas_py.GestorHoteles.escribir_archivo')

    @patch('builtins.print')
    def test_modificar_hotel(self, mock_print, mock_escribir_archivo, mock_leer_archivo):
        Hotel.modificar_hotel(2, {"nombre": "Hotel Modificado", "ubicacion": "Ciudad Nueva"})

        # Imprimir las llamadas reales a print para depurar
        print(f"Se llamó a print con: {mock_print.call_args_list}")
        mock_print.assert_any_call("Hotel actualizado exitosamente.")
    
    @patch('hoteles_reservas_py.GestorHoteles.leer_archivo', return_value=[])

    @patch('builtins.print')
    def test_eliminar_hotel(self, mock_print, mock_leer_archivo):
        Hotel.eliminar_hotel(2)

        # Verificar la llamada a print
        print(f"Se llamó a print con: {mock_print.call_args_list}")
        mock_print.assert_any_call("Hotel con ID 2 eliminado.")

    @patch('builtins.print')
    def test_mostrar_info_hotel(self, mock_print):
        hotel_data = self.crear_hotel_prueba(2, "Hotel Dos", "Ciudad Dos", 70, 3)
        Hotel.mostrar_info(2)

        # Verificar que se imprimió el JSON correctamente
        print(f"Se llamó a print con: {mock_print.call_args_list}")
        mock_print.assert_any_call(json.dumps(hotel_data, indent=4, ensure_ascii=False))

class TestCliente(unittest.TestCase):

    def setUp(self):
        self.cliente_data = {
            "id_cliente": 5,
            "nombre": "Oscar Rodriguez H",
            "email": "oscarRH@gmail.com"
        }

    def crear_cliente_prueba(self, id_cliente, nombre, email):
        return {
            "id_cliente": id_cliente,
            "nombre": nombre,
            "email": email
        }

    def tearDown(self):
        pass

    @patch('hoteles_reservas_py.GestorHoteles.leer_archivo', return_value=[{"id_cliente": 5, "nombre": "Antiguo Nombre", "email": "antiguo@example.com"}])
    @patch('hoteles_reservas_py.GestorHoteles.escribir_archivo')

    @patch('builtins.print')
    def test_modificar_cliente(self, mock_print, mock_escribir_archivo, mock_leer_archivo):
        Cliente.modificar_cliente(5, {"nombre": "Ana María González", "email": "ana_maria@example.com"})

        # Verificar la llamada a print
        print(f"Se llamó a print con: {mock_print.call_args_list}")
        mock_print.assert_any_call("Cliente actualizado exitosamente.")

    @patch('hoteles_reservas_py.GestorHoteles.leer_archivo', return_value=[])

    @patch('builtins.print')
    def test_eliminar_cliente(self, mock_print, mock_leer_archivo):
        Cliente.eliminar_cliente(5)

        # Verificar la llamada a print
        print(f"Se llamó a print con: {mock_print.call_args_list}")
        mock_print.assert_any_call("Cliente con ID 5 eliminado.")

    @patch('builtins.print')
    def test_mostrar_info_cliente(self, mock_print):
        cliente_data = self.crear_cliente_prueba(4, "Carlos Méndez", "carlos.mendez@example.com")
        Cliente.mostrar_info(4)

        # Verificar que se imprimió el JSON correctamente
        print(f"Se llamó a print con: {mock_print.call_args_list}")
        mock_print.assert_any_call(json.dumps(cliente_data, indent=4, ensure_ascii=False))


class TestReserva(unittest.TestCase):

    def setUp(self):
        self.reserva_data = {
            "id_reserva": 1,
            "id_cliente": 1,
            "id_hotel": 1
        }
    
    def crear_reserva_prueba(self, id_reserva, id_cliente, id_hotel):
        return {
            "id_reserva": id_reserva,
            "id_cliente": id_cliente,
            "id_hotel": id_hotel
        }

    def tearDown(self):
        pass

    @patch('hoteles_reservas_py.GestorHoteles.leer_archivo', return_value=[{"id_reserva": 1, "id_cliente": 1, "id_hotel": 1}])
    @patch('hoteles_reservas_py.GestorHoteles.escribir_archivo')

    @patch('builtins.print')
    def test_cancelar_reserva(self, mock_print, mock_escribir_archivo, mock_leer_archivo):
        Reserva.cancelar_reserva(1)

        # Verificar la llamada a print
        print(f"Se llamó a print con: {mock_print.call_args_list}")
        mock_print.assert_any_call("Reserva con ID 1 cancelada.")

    @patch('builtins.print')
    def test_mostrar_info_reserva(self, mock_print):
        reserva_data = self.crear_reserva_prueba(1, 1, 1)
        Reserva.mostrar_info(1)

        # Verificar que se imprimió el JSON correctamente
        print(f"Se llamó a print con: {mock_print.call_args_list}")
        mock_print.assert_any_call(json.dumps(reserva_data, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    unittest.main()
