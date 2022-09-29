function waterMeter(){
    var waterSwitch = document.getElementById('water-switch');
    var waterMeter = document.getElementById('inner-water-meter')

    if (waterSwitch.checked){
        waterMeter.style.height = "700px";       
    }
    else if (waterSwitch.checked == false) {
        waterMeter.style.height = "0px";   
    }
}

function lightMeter(){
    var lightSwitch = document.getElementById('light-switch');
    var lightMeter = document.getElementById('light-meter')

    if (lightSwitch.checked){
        lightMeter.style.background = "yellow";       
    }
    else if (lightSwitch.checked == false) {
        lightMeter.style.background = "grey";   
    }
}