import {defineStore} from 'pinia'
import instance from "@/services/axios.ts";
import type {User} from "@/types/user.ts";

export const useUserStore = defineStore('user', {
    state: () => ({
        name: 'John Doe',
        isLoggedIn: false,
        loading: false,
        error: false,
        csrf: '' as string | null,
    }),
    actions: {
        async setCsrfToken() {
            let name: string = "csrftoken"
            if (!this.csrf) {
                await instance.get("auth/csrf-token")
                this.csrf = this.readCsrfFromCookie(name);
            }


        },
        readCsrfFromCookie(name: string) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        ,


        async login(user: User) {
            this.name = user.username
            this.loading = true;
            try {
                await instance.post("/auth/login", user);
                this.csrf = this.readCsrfFromCookie("csrftoken");
                this.isLoggedIn = true;
            } catch (error: any) {
                this.error = error.message;
            } finally {
                this.loading = false;
            }

        },
        async logout() {
            try {
                await instance.post("/auth/logout");
                this.isLoggedIn = false;
            } catch (error: any) {
                this.error = error.message;
            } finally {
                this.loading = false;
            }
        },
    },
    persist: true
})