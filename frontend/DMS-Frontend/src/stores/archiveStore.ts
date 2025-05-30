import {defineStore} from "pinia";
import instance from "@/services/axios.ts";
import type {ArchiveSchema, AttributesSchema, TypeSchema} from "@/types/output";

export const useArchiveStore = defineStore("ArchiveStore", {
    state: () => ({
        archives: null as ArchiveSchema[] | null,
        archive: {
            name: "",
            attributes: [],
            id: null,
            createOn: null,
        } as ArchiveSchema,
        attribute: {
            name: "",
            archive: null,
            label: "",
            type: {
                id: null,
                name: "",
            },
        } as AttributesSchema,
        types: null as TypeSchema[] | null,
        archiveSaveError: false as boolean,
        archiveSaveErrorMessage: "" as string,
    }),
    actions: {
        async getArchives() {
            const response = await instance.get("/archives/");
            this.archives = response.data;
        },
        async saveArchive() {
            try {
                const response = await instance.post("/archives/", this.archive)
            } catch (e: any) {
                this.archiveSaveError = true;
                this.archiveSaveErrorMessage = e.response.data.message;

            }
        },
        async addAtribute(attribute: AttributesSchema) {
            const response = await instance.post("/attributes/", attribute)
        },
        async getTypes() {
            const response = await instance.get("/types/")
            this.types = response.data
        }

    }
})