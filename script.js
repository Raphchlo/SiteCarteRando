let time = 2 ;
let distance = 3 ;
let donnee = null;
let longUser = null;
let latUser = null;
let listeRando = []
// Fonction d'initialisation de la carte
function initMap(lat, lon,macarte) {
    // Créer l'objet "macarte" et l'insèrer dans l'élément HTML qui a l'ID "map"
    macarte = L.map('map').setView([lat, lon], 11);
    // Leaflet ne récupère pas les cartes (tiles) sur un serveur par défaut. Nous devons lui préciser où nous souhaitons les récupérer. Ici, openstreetmap.fr
    L.tileLayer('https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png', {
        // Il est toujours bien de laisser le lien vers la source des données
        attribution: 'données © <a href="//osm.org/copyright">OpenStreetMap</a>/ODbL - rendu <a href="//openstreetmap.fr">OSM France</a>',
        minZoom: 1,
        maxZoom: 20
    }).addTo(macarte);
    let marker = L.marker([lat, lon]).addTo(macarte);
    marker.bindPopup("votre localisation");
    for (let i = 0; i<listeRando.length;i++){
        const locRando = listeRando[i]["randonnee_localisation"].split(";");
        const longRando = parseFloat(locRando[1]);
        const latRando = parseFloat(locRando[0]);
        let marker1 = L.marker([latRando, longRando]).addTo(macarte).bindPopup(listeRando[i]["randonnee_nom"]);

        
    }

}
// function initMapTrajet(lat, lon,macarte2) {
//     // Créer l'objet "macarte" et l'insèrer dans l'élément HTML qui a l'ID "map"
//     macarte2 = L.map('map-trajet').setView([lat, lon], 11);
//     // Leaflet ne récupère pas les cartes (tiles) sur un serveur par défaut. Nous devons lui préciser où nous souhaitons les récupérer. Ici, openstreetmap.fr
//     L.tileLayer('https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png', {
//         // Il est toujours bien de laisser le lien vers la source des données
//         attribution: 'données © <a href="//osm.org/copyright">OpenStreetMap</a>/ODbL - rendu <a href="//openstreetmap.fr">OSM France</a>',
//         minZoom: 1,
//         maxZoom: 20
//     }).addTo(macarte2);
//     var gpx = data[1]["randonnee_carte"]; // Cela devrait être l'URL de ton fichier GPX
//     new L.GPX(gpx, {async: true}).on('loaded', function(e) {
//         macarte2.fitBounds(e.target.getBounds());
//     }).addTo(macarte2);
//}

async function loadGPXAndDisplay() {
    const gpxUrl = 'https://cors-anywhere.herokuapp.com/https://randogps.net/nb_telecharge.php?dep=38&num=8';  // URL où le GPX est généré

    try {
        
        const response = await fetch(gpxUrl);
        
        if (!response.ok) {
            throw new Error('Erreur lors du téléchargement du fichier GPX');
        }

        // 2. Lire le contenu du fichier GPX
        const gpxData = await response.text();
        
        // 3. Afficher le GPX sur la carte
        const macarte2 = L.map('map-trajet').setView([latUser, longUser], 11);  // Adapte selon ton besoin
        L.tileLayer('https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png', {
            attribution: 'données © <a href="//osm.org/copyright">OpenStreetMap</a>/ODbL - rendu <a href="//openstreetmap.fr">OSM France</a>',
            minZoom: 1,
            maxZoom: 20
        }).addTo(macarte2);

        // 4. Créer un objet GPX avec le fichier récupéré
        new L.GPX(gpxData, { async: true })
            .on('loaded', function(e) {
                macarte2.fitBounds(e.target.getBounds());  // Ajuster la carte aux limites du GPX
            })
            .addTo(macarte2);
    } catch (error) {
        console.error("Erreur lors du chargement du fichier GPX:", error);
    }
}
// window.onload = function(){
//     const succes = (position) =>{
//         const {latitude, longitude}=position.coords;
//         let lat = latitude;
//         latUser = lat
//         let lon = longitude;
//         let macarte = null;
//         let macarte2 = null;
//         initMap(lat,lon,macarte); 
//         initMapTrajet(lat,lon,macarte2);
//     };
    
//     const error = (error) =>{
//         console.warn(error.message);
//     };
    
//     // Fonction d'initialisation qui s'exécute lorsque le DOM est chargé
//     navigator.geolocation.getCurrentPosition(succes,error);
//     fetch('../api.php')
//         .then(response => response.json())
//         .then(data => {
//     console.log(data); // Tu peux afficher ça ou l'injecter dans le HTML
//     donnee = data
//   })
//   .catch(error => console.error('Erreur :', error));
//   getproxi()
// };


function getPosition(){
    return new Promise((resolve,reject)=>{
        navigator.geolocation.getCurrentPosition(resolve,reject);
    });
}

async function init(){
    try{
        const position = await getPosition();
        const {latitude, longitude} = position.coords;
        latUser = latitude;
        longUser = longitude;
        console.log(latUser)
        const response = await fetch('api.php');
        data = await response.json();
        console.log(data);
        

        getproxi();
        let macarte = null;
        let macarte2 = null;
        initMap(latUser,longUser,macarte); 
        loadGPXAndDisplay();
        // initMapTrajet(latUser,longUser,macarte2);

    }catch (error) {
        console.error('Erreur attrapée dans init() :', error);
    }
}


window.onload = init();
// localisation

const latToKm = (lat) =>{  // calcul de la lat en kilometre
    return lat*111
}
const longToKm = (long,lat) =>{
    return long*111*Math.cos(lat*(Math.PI/180)) //calcul de la long en kilometre
}



function getproxi(){  // renvoie une liste avec les rando à moins de 10km de la position de l'user
    for (let i =0; i<data.length; i++){
        const locRando = data[i]["randonnee_localisation"].split(";");
        const longRando = locRando[1];
        const latRando = locRando[0];
        const distMax = 10;
        let time2 = data[i]["randonnee_duree"].split(" ");
            time2 = time2[0].split(":").join(".");
        let distance_rando = data[i]["randonnee_distance"].split(" ");
            distance_rando = distance_rando[0]
        
        if ((longToKm(longRando,latRando)-longToKm(longUser,latUser))**2 + (latToKm(latRando)-latToKm(latUser))**2 <= distMax**2 &&  time2<=time && distance_rando<=distance){ // calcul de distance : n  = dist max
            listeRando.push(data[i])
        }
    }
    console.log(listeRando)



}


