import {createRouter, createWebHistory} from "vue-router";
import LoginPage from "@/views/LoginPage.vue";
import SettingsPage from "@/views/SettingsPage.vue";
import {useUserStore} from "@/stores/userStore.ts";
import ArchivPage from "@/views/ArchivPage.vue";
import HomePage2 from "@/views/HomePage2.vue";


const router = createRouter(
    {
        history: createWebHistory(),
        routes: [
            {path: '/', redirect: "/home"},
            {path: '/home', name: "home", component: HomePage2}
            ,
            {path: '/login', name: "login", component: LoginPage},
            {path: '/settings', name: "settings", component: SettingsPage},
            {path: '/archive', name: "archive", component: ArchivPage}

        ]
    }
);
const getLoginStatus = () => {
    const userStore = useUserStore();
    return userStore.isLoggedIn;
}
router.beforeEach(async (to, from, next) => {
    if (!getLoginStatus() && to.name !== "login") {
        // Redirect zum Login, ohne zusätzlich next() aufzurufen
        next({name: "login"});
    } else {
        // Erlaubter Zugriff
        next();
    }
});

export default router;