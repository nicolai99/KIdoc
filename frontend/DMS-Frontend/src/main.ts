import './assets/main.css'

import {createApp} from 'vue'
import App from './App.vue'
import PrimeVue from 'primevue/config'
import ToastService from 'primevue/toastservice'
import Aura from '@primeuix/themes/aura';
import router from "@/router/router.ts"
import {createPinia} from "pinia";
import piniaPersist from 'pinia-plugin-persistedstate'
import {useUserStore} from "@/stores/userStore.ts";

const app = createApp(App);

const pinia = createPinia();
pinia.use(piniaPersist);
app.use(pinia);

const userStore = useUserStore();
userStore.setCsrfToken();

app.use(router);
app.use(PrimeVue, {
    theme: {
        preset: Aura,
        options: {
            darkModeSelector: false,
            cssLayer: {
                name: 'primevue',
                order: 'theme, base, primevue'
            }
        }
    }
});
app.use(ToastService);

app.mount('#app');
