from decimal import Decimal

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Categoria, Marca, Producto


class CategoriaModelTest(TestCase):
    def test_crear_categoria(self):
        cat = Categoria.objects.create(nombre="Frenos")
        self.assertEqual(str(cat), "Frenos")
        self.assertTrue(cat.activa)


class MarcaModelTest(TestCase):
    def test_crear_marca(self):
        marca = Marca.objects.create(nombre="Bosch", descripcion="Repuestos")
        self.assertEqual(str(marca), "Bosch")


class ProductoModelTest(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nombre="Filtros")
        self.marca = Marca.objects.create(nombre="Mann", descripcion="Filtros")

    def test_crear_producto(self):
        p = Producto.objects.create(
            nombre="Filtro de aceite", precio=5990, precio_mayorista=4500,
            descripcion="Filtro", stock=10, categoria=self.categoria,
            peso=Decimal("0.50"), largo=10, ancho=10, alto=10,
        )
        p.marca.add(self.marca)
        self.assertEqual(str(p), "Filtro de aceite")
        self.assertEqual(p.marca.count(), 1)
        self.assertEqual(self.categoria.productos.count(), 1)


class UsuarioTest(TestCase):
    def test_crear_usuario(self):
        u = User.objects.create_user(username="carla", email="carla@carla.carla", password="Carla1!")
        self.assertTrue(u.check_password("Carla1!"))


class PaginasTest(TestCase):
    def test_login_page_responde(self):
        r = self.client.get(reverse("login"))
        self.assertEqual(r.status_code, 200)
