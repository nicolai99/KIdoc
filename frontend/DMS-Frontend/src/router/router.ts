import {createRouter, createWebHistory} from "vue-router";
import LoginPage from "@/views/LoginPage.vue";
import SettingsPage from "@/views/SettingsPage.vue";
import {useUserStore} from "@/stores/userStore.ts";
import ArchivPage from "@/views/ArchivPage.vue";
import HomePage from "@/views/HomePage.vue";
import SearchPage from "@/views/SearchPage.vue";


const router = createRouter(
    {
        history: createWebHistory(),
        routes: [
            {path: '/', redirect: "/home"},
            {path: '/home', name: "home", component: HomePage}
            ,
            {path: '/login', name: "login", component: LoginPage},
            {path: '/settings', name: "settings", component: SettingsPage},
            {path: '/archives', name: "archives", component: ArchivPage},
            {
                path: '/search/:archiveId',
                name: "search",
                component: SearchPage
            }

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