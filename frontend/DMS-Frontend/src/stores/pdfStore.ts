import {defineStore} from "pinia";
import instance from "@/services/axios.ts";

export const usePdfStore = defineStore('pdfStore', {
    state: () => ({
        pdf: null as File | null,
        id: null as number | null,
        archive_id: null as number | null,
        uploadError: false,
        loading: false,
    }),
    actions: {

        async uploadPdf() {
            const formData = new FormData();
            formData.append('file', this.pdf as Blob);
            formData.append('archive_id', String(this.archive_id));
            this.uploadError = false;
            let response = null;
            this.loading = true;
            try {
                response = await instance.post('/pdfs/upload', formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data',
                    },
                });
                this.id = response.data
                this.loading = false;
            } catch (e) {
                this.uploadError = true;
            } finally {
                this.loading = false;
            }
        },
        async deletePdf(pdfId: number) {
            const response = await instance.delete(`/pdfs/delete/${pdfId}`)

        },
        async getPdfContent(pdfId: number) {
            const response = await instance.get(`/pdfs/${pdfId}`, {
                responseType: 'blob',
            });

            const blob = response.data;
            const file = new File([blob], 'document.pdf', {type: 'application/pdf'});

            this.pdf = file;
        }
    }
})