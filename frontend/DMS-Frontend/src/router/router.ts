import {createRouter, createWebHistory} from "vue-router";
import HomePage from "@/views/HomePage.vue";
import LoginPage from "@/views/LoginPage.vue";
import SettingsPage from "@/views/SettingsPage.vue";


const router = createRouter(
    {
        history: createWebHistory(),
        routes: [
            {path: '/', redirect: "/home"},
            {path: '/home', name: "home", component: HomePage}
            ,
            {path: '/login', name: "login", component: LoginPage},
            {path: '/settings', name: "settings", component: SettingsPage}

        ]
    }
);

export default router;