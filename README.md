# E-commerce con Roles de Admin y Cliente
E-commerce utilizando Django y Django REST Framework con dos roles principales: Administrador y Cliente. Ambos roles accederán a vistas personalizadas del Django admin,donde el administrador gestionará productos y el cliente tendrá una vista limitada para revisar 
su historial de compras.

## Caracteristicas
###Roles de Usuarios
Administrador:Tendrá acceso completo al Django admin,con permisos para agregar,editar y eliminar productos. 
Cliente:Tendrá acceso a una vista personalizada dentro del Django admin donde podrá revisar su historial de compras y los detalles de cada una. 
###Proceso de Compra
El cliente agrega productos al carrito utilizando una interfaz que cargue todo dinámicamente.
Al finalizar la compra, se realiza un único POST contodos los productos en elcarrito.
Los datos del carrito deben guardarse y mostrarse en el historial de compras del cliente. 
