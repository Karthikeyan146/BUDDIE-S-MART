window.alert = function (message, timeout=null){
    const alert = document.createElement('div');
    const alertButton = document.createElement('button');
    alertButton.innerText = 'ok'; 
    alert.classList.add('alert');
    alert.setAttribute('style',`
        position:fixed;
        top:80px;
        left:50%;
        padding: 20px;
        border-radius:10px;
        box-shadow:0 10px 5px 0 #00000022;
        display:flex;
        flex-direction:column;
        border:2px solid #5927e5;
        transform: translateX(-50%);
        background-color:white;
        font-weight:600;
        text-align:center;

    `);
    alertButton.setAttribute('style',`
        border:1px solid #333;
        background-color:#5927e5;
        font-weight:700;
        color:white;
        border-radius:5px;
        padding:5px;
    `);
    alert.innerHTML = `<span style="padding:10px">${message}<span>`;
    alert.appendChild(alertButton);
    alertButton.addEventListener('click',(e) =>{
        alert.remove();
    });
    if(timeout != null){
        setTimeout(()=>{
            alert.remove();
        }, Number(timeout))
    }
    document.body.appendChild(alert);
}