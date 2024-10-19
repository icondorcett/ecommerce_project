# E-commerce con Roles de Admin y Cliente
E-commerce realizado con Django y Django REST Framework con dos roles principales: Administrador y Cliente. Ambos roles accederán a vistas personalizadas del Django admin,donde el administrador gestionará productos y el cliente tendrá una vista limitada para revisar 
su historial de compras.

## Caracteristicas

### Roles de Usuarios

**Administrador:** Tendrá acceso completo al Django admin,con permisos para agregar,editar y eliminar productos. 

**Cliente:** Tendrá acceso a una vista personalizada dentro del Django admin donde podrá revisar su historial de compras y los detalles de cada una. 

### Proceso de Compra

El cliente agrega productos al carrito utilizando una interfaz que cargue todo dinámicamente.
Al finalizar la compra, se realiza un único POST contodos los productos en elcarrito.
Los datos del carrito deben guardarse y mostrarse en el historial de compras del cliente. 


## Instrucciones de instalación

Para ejecutar este proyecto localmente, siga estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/icondorcett/ecommerce_project.git   
   cd ecommerce_project
   ```
2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Aplicar migraciones de bases de datos:**
   ```bash
   python manage.py migrate
   ```
4. **Cargar datos iniciales (opcional)**
   ```bash
   python manage.py loaddata initial_data.json
   ```
5. **Crear un superusuario**
   ```bash
   python manage.py createsuperuser
   ```
6. **Iniciar el servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```
7. **Abra su navegador web y navegue a:**
   ```bash
   http://127.0.0.1:8000/
   ```
## Uso
-**Panel de administración:** acceda al panel de administración http://127.0.0.1:8000/admin/ con el superuser creado para setear las contraseñas para cada cliente y administrador. 
-**Para administrador:** http://127.0.0.1:8000/admin/
-**Para cliente:** http://127.0.0.1:8000/cliente_admin/
-**API productos:** http://127.0.0.1:8000/tienda/api/productos/
-**API compras:** http://127.0.0.1:8000/tienda/api/compras/
