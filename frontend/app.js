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

            const boton = document.createElement("button");
            boton.textContent = "Ver detalle";
            boton.addEventListener("click", () => verDetallePlan(plan.id));

            tarjeta.append(nombre, precio, duracion, boton);
            planesContenedor.appendChild(tarjeta);
        });
    } catch (error) {
        planesContenedor.innerHTML = "<p>No se pudieron cargar los planes.</p>";
        mensaje.textContent = error.message;
    }
}

async function cargarMiembros() {
    try {
        const [respuestaMiembros, respuestaPlanes] = await Promise.all([
            fetch(`${API_URL}/miembros/`),
            fetch(`${API_URL}/planes/`)
        ]);

        if (!respuestaMiembros.ok || !respuestaPlanes.ok) {
            throw new Error("No se pudieron cargar los miembros o los planes.");
        }

        const miembros = await respuestaMiembros.json();
        const planes = await respuestaPlanes.json();

        const nombresPlanes = new Map(
            planes.map((plan) => [plan.id, plan.nombre])
        );

        miembrosContenedor.innerHTML = "";

        if (miembros.length === 0) {
            miembrosContenedor.innerHTML =
                '<tr><td colspan="5">No hay miembros registrados.</td></tr>';
            return;
        }

        miembros.forEach((miembro) => {
            const fila = document.createElement("tr");

            const valores = [
                miembro.nombre,
                miembro.edad,
                miembro.telefono,
                nombresPlanes.get(miembro.plan_id) || "Sin plan"
            ];

            valores.forEach((valor) => {
                const celda = document.createElement("td");
                celda.textContent = valor ?? "";
                fila.appendChild(celda);
            });

            const celdaAccion = document.createElement("td");
            const boton = document.createElement("button");
            boton.textContent = "Ver detalle";
            boton.addEventListener("click", () => verDetalleMiembro(miembro.id));

            celdaAccion.appendChild(boton);
            fila.appendChild(celdaAccion);
            miembrosContenedor.appendChild(fila);
        });
    } catch (error) {
        miembrosContenedor.innerHTML =
            '<tr><td colspan="5">No se pudieron cargar los miembros.</td></tr>';
        mensaje.textContent = error.message;
    }
}

async function verDetallePlan(id) {
    try {
        const respuesta = await fetch(`${API_URL}/planes/${id}`);

        if (!respuesta.ok) {
            throw new Error("No se pudo encontrar el plan.");
        }

        const plan = await respuesta.json();

        mostrarDetalle(
            "Detalle del plan",
            [
                ["Nombre", plan.nombre],
                ["Precio", `$${Number(plan.precio).toLocaleString("es-CO")}`],
                ["Duración", `${plan.duracion_dias} días`]
            ]
        );
    } catch (error) {
        mensaje.textContent = error.message;
    }
}

async function verDetalleMiembro(id) {
    try {
        const respuesta = await fetch(`${API_URL}/miembros/${id}`);

        if (!respuesta.ok) {
            throw new Error("No se pudo encontrar el miembro.");
        }

        const miembro = await respuesta.json();
        const respuestaPlanes = await fetch(`${API_URL}/planes/`);

        if (!respuestaPlanes.ok) {
            throw new Error("No se pudo consultar el plan del miembro.");
        }

        const planes = await respuestaPlanes.json();
        const plan = planes.find((item) => item.id === miembro.plan_id);

        mostrarDetalle(
            "Detalle del miembro",
            [
                ["Nombre", miembro.nombre],
                ["Edad", miembro.edad],
                ["Teléfono", miembro.telefono],
                ["Plan", plan ? plan.nombre : "Sin plan"]
            ]
        );
    } catch (error) {
        mensaje.textContent = error.message;
    }
}

function mostrarDetalle(titulo, campos) {
    mensaje.innerHTML = "";

    const detalle = document.createElement("section");
    detalle.className = "detalle";

    const encabezado = document.createElement("h2");
    encabezado.textContent = titulo;
    detalle.appendChild(encabezado);

    campos.forEach(([etiqueta, valor]) => {
        const parrafo = document.createElement("p");
        const textoEtiqueta = document.createElement("strong");

        textoEtiqueta.textContent = `${etiqueta}: `;
        parrafo.append(textoEtiqueta, document.createTextNode(valor ?? "No disponible"));
        detalle.appendChild(parrafo);
    });

    const botonCerrar = document.createElement("button");
    botonCerrar.textContent = "Cerrar detalle";
    botonCerrar.addEventListener("click", () => {
        mensaje.innerHTML = "";
    });

    detalle.appendChild(botonCerrar);
    mensaje.appendChild(detalle);
    mensaje.scrollIntoView({ behavior: "smooth", block: "nearest" });
}

async function iniciar() {
    await Promise.all([cargarPlanes(), cargarMiembros()]);
}

iniciar();