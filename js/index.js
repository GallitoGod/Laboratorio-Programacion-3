import { landing_page } from "./pages/landing_page.js"
import { recorrido_form } from "./pages/recorrido_form.js"
import { reserva_form } from "./pages/reserva_form.js"

document.addEventListener('DOMContentLoaded', () => {
    const page = document.body.dataset.page

    if (page === 'landing_page') landing_page()
    if (page === 'recorrido_form') recorrido_form()
    if (page === 'reserva_form') reserva_form()
})