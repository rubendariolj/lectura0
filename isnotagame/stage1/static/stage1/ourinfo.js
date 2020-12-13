
function showSection(section) {
                

    fetch(`/whoweare/${section}`)
    .then(response => response.text())
    .then(text => {
        console.log(text);
        document.querySelector('#content').style.display = 'block';
        document.querySelector('#content').innerHTML = text;
    });
}

// Shows one page and hides the other two
function showPage(page) {

    // Hide all of the divs:
    document.querySelectorAll('div').forEach(div => {
        div.style.display = 'none';
    });

    // Show the div provided in the argument
    document.querySelector(`#${page}`).style.display = 'block';
}


function ChangeColor(a)  
               {  
                var title = a;
                console.log(a);
                document.getElementById(`${a}`).style.backgroundColor='lightgreen';
                document.getElementById(`${a}`).style.height='35px';
                document.getElementById(`${a}`).style.width='162px';
               } 

function ChangeColor2(a)
                {
                var title = a;
                console.log(a);
                document.getElementById(`${a}`).style.backgroundColor='lightgray';
                document.getElementById(`${a}`).style.height='30px';
                document.getElementById(`${a}`).style.width='160px';
                }

               

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('button').forEach(button => {
        button.onclick = function() {
            const info = this.dataset.section;
            console.log(info);
            showSection(this.dataset.section);
            showPage(this.dataset.page);
            document.getElementById(`${info}`).style.backgroundColor = button.dataset.color;
            document.querySelector(`#tittle${info}`).style.backgroundColor = button.dataset.color;
        };
    });
});
