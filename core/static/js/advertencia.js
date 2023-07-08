function mostrarPantallaEmergente() {
    var pantallaEmergente = document.getElementById('pantalla-emergente');
    pantallaEmergente.style.display = 'flex';
  }
  
  function confirmarAccion() {
    var pantallaEmergente = document.getElementById('pantalla-emergente');
    pantallaEmergente.style.display = 'none';
    // Aquí puedes realizar la acción deseada una vez que el usuario haya confirmado
    // Por ejemplo, desbloquear el contenido, enviar datos, redirigir, etc.
  }
  
  // Llamar a la función para mostrar la pantalla emergente
  mostrarPantallaEmergente();
  