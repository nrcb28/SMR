/* Demostración local: no usa fetch, almacenamiento ni envío a un backend. */
"use strict";

const CATEGORIAS = Object.freeze(["Hardware", "Software", "Red", "Impresión"]);

function validarDatos(entrada) {
  const datos = entrada && typeof entrada === "object" ? entrada : {};
  const valores = {
    codigo: typeof datos.codigo === "string" ? datos.codigo.trim().toUpperCase() : "",
    categoria: typeof datos.categoria === "string" ? datos.categoria.trim() : "",
    descripcion: typeof datos.descripcion === "string" ? datos.descripcion.trim() : ""
  };
  const errores = {};
  if (!/^PC-[0-9]{3}$/.test(valores.codigo)) {
    errores.codigo = "Utiliza PC, guion y tres cifras; por ejemplo, PC-007.";
  }
  if (!CATEGORIAS.includes(valores.categoria)) {
    errores.categoria = "Selecciona Hardware, Software, Red o Impresión.";
  }
  if (valores.descripcion.length < 10 || valores.descripcion.length > 500) {
    errores.descripcion = "Escribe un síntoma ficticio de 10 a 500 caracteres, sin contar espacios en los extremos.";
  }
  return { valores, errores, valido: Object.keys(errores).length === 0 };
}

function iniciarRegistro(documento) {
  const ids = ["interaccion", "registro", "codigo", "categoria", "descripcion",
    "codigo-error", "categoria-error", "descripcion-error", "resumen-errores",
    "lista-errores", "filas-locales", "vaciar", "estado", "estado-script"];
  const elementos = {};
  for (const id of ids) {
    elementos[id] = documento.getElementById(id);
    if (!elementos[id]) return false;
  }
  const campos = ["codigo", "categoria", "descripcion"];
  let siguienteId = 1;

  function limpiarErrores() {
    elementos["lista-errores"].replaceChildren();
    elementos["resumen-errores"].hidden = true;
    for (const campo of campos) {
      elementos[campo].removeAttribute("aria-invalid");
      elementos[campo].setAttribute("aria-describedby", `${campo}-ayuda`);
      elementos[`${campo}-error`].textContent = "";
      elementos[`${campo}-error`].hidden = true;
    }
  }

  elementos.registro.addEventListener("submit", (evento) => {
    evento.preventDefault();
    limpiarErrores();
    const resultado = validarDatos({
      codigo: elementos.codigo.value,
      categoria: elementos.categoria.value,
      descripcion: elementos.descripcion.value
    });
    if (!resultado.valido) {
      for (const [campo, mensaje] of Object.entries(resultado.errores)) {
        const error = elementos[`${campo}-error`];
        error.textContent = mensaje;
        error.hidden = false;
        elementos[campo].setAttribute("aria-invalid", "true");
        elementos[campo].setAttribute("aria-describedby", `${campo}-ayuda ${campo}-error`);
        const item = documento.createElement("li");
        const enlace = documento.createElement("a");
        enlace.href = `#${campo}`;
        enlace.textContent = mensaje;
        enlace.addEventListener("click", (click) => {
          click.preventDefault();
          elementos[campo].focus();
        });
        item.append(enlace);
        elementos["lista-errores"].append(item);
      }
      elementos["resumen-errores"].hidden = false;
      elementos["resumen-errores"].focus();
      elementos.estado.textContent = "No se ha añadido el registro. Corrige los datos del resumen.";
      return;
    }
    const identificador = `LOCAL-${String(siguienteId).padStart(3, "0")}`;
    siguienteId += 1;
    const fila = documento.createElement("tr");
    const columnas = [identificador, resultado.valores.codigo,
      resultado.valores.categoria, resultado.valores.descripcion];
    for (const texto of columnas) {
      const celda = documento.createElement("td");
      celda.textContent = texto;
      fila.append(celda);
    }
    elementos["filas-locales"].append(fila);
    elementos.vaciar.disabled = false;
    elementos.registro.reset();
    elementos.estado.textContent = `${identificador} añadido a esta vista local. Se perderá al recargar la página.`;
    elementos.codigo.focus();
  });

  elementos.registro.addEventListener("reset", () => {
    limpiarErrores();
    elementos.estado.textContent = "Campos restablecidos. Los registros de esta vista no se han borrado.";
  });

  elementos.vaciar.addEventListener("click", () => {
    elementos["filas-locales"].replaceChildren();
    elementos.vaciar.disabled = true;
    elementos.estado.textContent = "Se han vaciado los registros locales; la tabla de referencia permanece intacta.";
    elementos.codigo.focus();
  });

  elementos.registro.noValidate = true;
  elementos.interaccion.hidden = false;
  elementos["estado-script"].textContent = "El simulador local está disponible. No guarda ni envía los datos introducidos.";
  return true;
}

if (typeof document !== "undefined") {
  iniciarRegistro(document);
}
if (typeof module !== "undefined" && module.exports) {
  module.exports = { validarDatos, CATEGORIAS };
}
