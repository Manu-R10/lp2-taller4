const API_URL = "/api";

const planesContenedor = document.getElementById("planes");
const miembrosContenedor = document.getElementById("miembros");
const mensaje = document.getElementById("mensaje");

async function cargarPlanes() {
    try {
        const respuesta = await fetch(`${API_URL}/planes/`);

        if (!respuesta.ok) {
            throw new Error("No se pudieron cargar los planes.");
        }

        const planes = await respuesta.json();

        planesContenedor.innerHTML = "";

        if (planes.length === 0) {
            planesContenedor.innerHTML = "<p>No hay planes registrados.</p>";
            return;
        }

        planes.forEach((plan) => {
            const tarjeta = document.createElement("article");
            tarjeta.className = "tarjeta";

            const nombre = document.createElement("h3");
            nombre.textContent = plan.nombre;

            const precio = document.createElement("p");
            precio.className = "precio";
            precio.textContent = `$${Number(plan.precio).toLocaleString("es-CO")}`;

            const duracion = document.createElement("p");
            duracion.textContent = `Duración: ${plan.duracion_dias} días`;

            tarjeta.append(nombre, precio, duracion);
            planesContenedor.appendChild(tarjeta);
        });
    } catch (error) {
        planesContenedor.innerHTML = "<p>No se pudieron cargar los planes.</p>";
        mensaje.textContent = error.message;
    }
}

async function cargarMiembros() {
    try {
        const respuesta = await fetch(`${API_URL}/miembros/`);

        if (!respuesta.ok) {
            throw new Error("No se pudieron cargar los miembros.");
        }

        const miembros = await respuesta.json();
        miembrosContenedor.innerHTML = "";

        if (miembros.length === 0) {
            miembrosContenedor.innerHTML =
                '<tr><td colspan="4">No hay miembros registrados.</td></tr>';
            return;
        }

        miembros.forEach((miembro) => {
            const fila = document.createElement("tr");

            [
                miembro.nombre,
                miembro.edad,
                miembro.telefono,
                miembro.plan_id
            ].forEach((valor) => {
                const celda = document.createElement("td");
                celda.textContent = valor;
                fila.appendChild(celda);
            });

            miembrosContenedor.appendChild(fila);
        });
    } catch (error) {
        miembrosContenedor.innerHTML =
            '<tr><td colspan="4">No se pudieron cargar los miembros.</td></tr>';
        mensaje.textContent = error.message;
    }
}

async function iniciar() {
    await Promise.all([cargarPlanes(), cargarMiembros()]);
}

iniciar();