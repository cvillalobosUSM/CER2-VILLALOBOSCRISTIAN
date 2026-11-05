const filtro = document.getElementById("filtroMascota");
const tabla = document.getElementById("tablaMascotas");

filtro.addEventListener('input', function () {
  const busqueda = filtro.value.toLowerCase();
  const filas = tabla.querySelectorAll('tbody tr');

  filas.forEach(function (fila) {
    const nombre = fila.cells[2].textContent.toLowerCase();
    if (nombre.includes(busqueda)) {
      fila.style.display = '';
    } else {
      fila.style.display = 'none';
    }
  })
})
