import {defineStore} from "pinia";
import instance from "@/services/axios.ts";

export const usePdfStore = defineStore('pdfStore', {
    state: () => ({
        pdf: null as File | null,
        id: null as number | null,
        archive_id: null as number | null,
        uploadError: false
    }),
    actions: {

        async uploadPdf() {
            const formData = new FormData();
            formData.append('file', this.pdf as Blob);
            formData.append('archive_id', String(this.archive_id));
            this.uploadError = false;
            try {
                const response = await instance.post('/upload/upload', formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data',
                    },
                });
            } catch (e) {
                this.uploadError = true;
            }
        }
    }
})