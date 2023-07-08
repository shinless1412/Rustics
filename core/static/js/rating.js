// Obtener todas las estrellas
const stars = document.querySelectorAll('.star');

// Agregar evento de clic a cada estrella
stars.forEach(star => {
  star.addEventListener('click', function() {
    const value = this.dataset.value; // Obtener el valor de la estrella
    document.getElementById('id_puntuacion').value = value; // Asignar el valor al campo oculto
    // Actualizar la apariencia de las estrellas
    stars.forEach(s => {
      const starValue = s.dataset.value;
      s.classList.toggle('selected', starValue <= value);
    });
  });
});
