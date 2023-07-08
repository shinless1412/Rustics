document.getElementById('review-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Evitar que se recargue la página
  
    // Obtener los valores del formulario
    var nombre = document.getElementById('nombre').value;
    var comentario = document.getElementById('comentario').value;
    var puntuacion = document.getElementById('puntuacion').value;
  
    // Realizar acciones adicionales o enviar la información a través de AJAX
    // ...
  
    // Limpiar los campos del formulario
    document.getElementById('nombre').value = '';
    document.getElementById('comentario').value = '';
    document.getElementById('puntuacion').value = '';
  });
  