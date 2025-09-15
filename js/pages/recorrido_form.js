
export function recorrido_form() {
    const date = document.getElementById('fecha')
    date.addEventListener('change', (e) => {
        const obj = new Date()
        const inputDate = new Date(e.target.value)
        if (obj > inputDate) {
            e.target.setCustomValidity('Fecha de vuelo debe ser mayor a la actual')
            e.target.reportValidity()
        } else e.target.setCustomValidity('')
    })

    const origen = document.getElementById('origen')
    const destino = document.getElementById('destino')
    destino.addEventListener('change', (e) => {
        if (destino.value === origen.value 
           && origen.value !== undefined) {
            e.target.setCustomValidity('Ingresar un origen y destino distinto')
            e.target.reportValidity()
        }
    })
}