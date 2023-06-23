function openModal() {
    document.getElementById("modal").style.display = "block";
}

function closeModal() {
    document.getElementById("modal").style.display = "none";
}

// Variables globales
let carrito = [];
let total = 0;
let cantidad = 0;

function agregarAlCarrito(nombre, precio, imagenURL) {
  carrito.push({ nombre, precio, imagenURL });
  total += precio;
  cantidad++;
  actualizarCarrito();
  actualizarCantidad();
}
// Función para vaciar el carrito
function vaciarCarrito() {
  carrito = [];
  total = 0;
  cantidad = 0;
  actualizarCarrito();
  actualizarCantidad();
}

// Función para actualizar el carrito en la página
function actualizarCarrito() {
  const listaCarrito = document.getElementById('lista-carrito');
  const totalCarrito = document.getElementById('total-carrito');

  // Limpiar carrito previo
  listaCarrito.innerHTML = '';

  // Agregar elementos al carrito
  carrito.forEach(producto => {
    const { nombre, precio, imagenURL } = producto;
    const elemento = document.createElement('li');
    elemento.innerHTML = `
      <img src="${imagenURL}" alt="${nombre}">
      <span>${nombre} - $${precio}</span>`;
    listaCarrito.appendChild(elemento);
  });

  // Mostrar total
  totalCarrito.textContent = total;
}