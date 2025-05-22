import {defineStore} from "pinia";
import instance from "@/services/axios.ts";

export const useArchiveStore = defineStore("ArchiveStore", {
    state: () => ({
        archives: null as object[] | null
    }),
    actions: {
        async getArchives() {
            const response = await instance.get("/archives/");
            this.archives = response.data;
        }

    }
})