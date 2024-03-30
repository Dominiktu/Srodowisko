let kal = document.getElementById("Kalendarz")

function Stworz() {
    let dzis = new Date();
    let miesiac = dzis.getMonth();
    let rok = dzis.getFullYear();
    let dni = new Date(rok, miesiac + 1, 0).getDate();
    let p_dni = new Date(rok, miesiac + 1).getDate();

    let table = document.createElement("table");

    let thead = document.createElement("thead");
    let tr = document.createElement("tr");
    let dni_tygodnia = ['Pon', 'Wt', 'Sr', 'Czw', 'Pt', 'Sob', 'Niedz'];

    for(i = 0; i < dni_tygodnia.length; i++)
    {
        let th = document.createElement("th");
        th.textContent = dni_tygodnia[i];
        tr.appendChild(th);

    }

    thead.appendChild(tr);
    table.appendChild(thead);

    let tbody = document.createElement("tbody");
    let date = 1;
    for(i = 0; i < 6; i++)
    {
        let row = document.createElement("tr");
        for(j = 0; j < 7; j++)
        {
            if(i === 0 && j <p_dni)
            {
                let cell = document.createElement("td");
                row.appendChild(cell)
            }
            else if(date > dni)
            {
                break;
            }
            else
            {
                let cell = document.createElement("td");
                cell.textContent = date;
                
                row.appendChild(cell);
                date++
            }
        }
        tbody.appendChild(row);
    }
    table.appendChild(tbody)

    let kontener = document.getElementById('Kalendarz');
    kontener.innerHTML='';
    kontener.appendChild(table);
}

window.onload = function()
{
    Stworz()
}