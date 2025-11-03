import { landing_page } from "./pages/landing_page.js"
import { recorrido_form } from "./pages/recorrido_form.js"
import { reserva_form } from "./pages/reserva_form.js"

document.addEventListener('DOMContentLoaded', () => {

    if (document.getElementById('landing_page')) landing_page()
    if (document.getElementById('recorrido_form')) recorrido_form()
    if (document.getElementById('reserva_form')) reserva_form()
})