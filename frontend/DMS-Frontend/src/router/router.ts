import {createRouter, createWebHistory} from "vue-router";
import Login from "@/components/Login.vue";
import AppLayout from "@/layouts/AppLayout.vue";
import uploadPDF from "@/components/uploadPDF.vue";
import EmptyLayout from "@/layouts/EmptyLayout.vue";

const router = createRouter(
    {
        history: createWebHistory(),
        routes: [
            {
                path: "/", component: AppLayout, children: [{path: '', name: "home", component: uploadPDF}

                ]
            }
            ,
            {
                path: "/login", component: EmptyLayout, children: [{path: '', name: "login", component: Login}

                ]
            }
        ]
    }
);

export default router;