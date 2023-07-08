$(document).ready(function() {
    // Capturar el evento de clic en el botón "Agregar Review"
    $('#agregar-review-btn').click(function() {
      var productoId = $('#producto-id').val();
      var url = `/reviews/${productoId}/agregar/`; // URL para agregar review del producto
      window.location.href = url;  // Redirigir a la página de agregar review
    });
  });


  