document.getElementById("submit-btn").addEventListener("click", function(){
    document.getElementsByClassName("popup")[0].classList.add("active");alert("chal gaya");
    
});

    document.getElementById("dismiss-popup-btn").addEventListener("click", function(){
    document.getElementsByClassName("popup")[0].classList.remove("active");
});