import type {AxiosInstance} from 'axios';
import axios from 'axios';
import {useUserStore} from "@/stores/userStore.ts";


const instance: AxiosInstance = axios.create({
    baseURL: import.meta.env.VITE_API_URL,
    timeout: 6000,
    withCredentials: true,
})
instance.interceptors.request.use((config) => {
    const userStore = useUserStore();
    config.headers["X-CSRFToken"] = userStore.csrf;
    return config;
});

export default instance;