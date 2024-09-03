import { createApp } from "vue";
import App from "./App.vue";
import router from "./router"; // Ajout du router
import FontAwesomeIcon from "./plugins/font-awesome";

const app = createApp(App);

app.component("font-awesome-icon", FontAwesomeIcon);
app.use(router); // Utilisation de Vue Router dans l'application Vue
app.mount("#app");
