function confirmarAccion(event) {
    event.preventDefault();  // Evitar que el formulario se envíe de inmediato
    
    // Mostrar ventana emergente de confirmación
    if (confirm("¿Estás seguro de agregar esta reseña?")) {
      // Continuar con el envío del formulario si el usuario confirma
      event.target.closest('form').submit();
    }
  }
  