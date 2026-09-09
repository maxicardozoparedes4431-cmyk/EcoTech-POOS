from dominio.empleado import Empleado
from dominio.departamento import Departamento

empleado1 = Empleado(
    nombre="Benjamin",
    correo="Benjamin@gmail.com",
    telefono="+56 9 6142-0871",
    id=1,
)

empleado2 = Empleado(
    nombre="Antonio",
    correo="Antonio@hotmail.com",
    telefono="+56 9 3321-2871",
    id=2,
)

departamento1 = Departamento(nombre="Recursos Humanos")
departamento2 = Departamento(nombre="Marketing")

print(empleado1.mostrardatos(),"\n", departamento1.mostrardatos())
print(empleado2.mostrardatos(),"\n", departamento2.mostrardatos())