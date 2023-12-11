import { initializeApp } from "https://www.gstatic.com/firebasejs/10.5.0/firebase-app.js";
import { getDatabase, ref, set, get, child } from "https://www.gstatic.com/firebasejs/10.5.0/firebase-database.js";
const firebaseConfig = {
    apiKey: "AIzaSyDr2FgK1_jWbnvKAxE7o8bQ5GV_k2gplX4",
    authDomain: "formdata-591b2.firebaseapp.com",
    projectId: "formdata-591b2",
    storageBucket: "formdata-591b2.appspot.com",
    messagingSenderId: "986083202538",
    appId: "1:986083202538:web:7f02e06ddc9f2dcb47ce93"
};

  
const app = initializeApp(firebaseConfig);
const db = getDatabase(app);
document.getElementById("submit").addEventListener('click',function(e){
    set(ref(db,'user'+ document.getElementById("ticket-form-name").value),
    {
        username:document.getElementById("ticket-form-name").value,
        email:document.getElementById("ticket-form-email").value,
        Nonumber:document.getElementById("ticket-form-number").value
    });
    alert("Ticket Booked Ticket Will Email To You Soon......");
})
