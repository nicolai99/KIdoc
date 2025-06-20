import {defineStore} from "pinia";
import instance from "@/services/axios.ts";
import type {ArchiveSchema, AttributesSchema, PdfWithValuesSchema, TypeSchema} from "@/types/output";

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
        attributeValues: [] as any,
        waitForGemini: false,
        archiveNotFound: false,
        pdfsWithAttributeValues: [] as PdfWithValuesSchema[] | null,
        attributeValuesError: null as string | null,
    }),
    actions: {
        initAttributeValues(length: number) {
            this.attributeValues = new Array(length).fill(null);
        },
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
        async getArchiveById(id: number) {
            let response = null;
            try {
                response = await instance.get(`/archives/${id}`)
                this.archive = response.data
            } catch (e: any) {
                this.archiveNotFound = true;
            }
        },
        async addAtribute(attribute: AttributesSchema) {
            const response = await instance.post("/attributes/", attribute)

        },
        async getTypes() {
            const response = await instance.get("/types/")
            this.types = response.data
        },
        async getAttributeValuesFromGeminiByPdf(pdfId: number) {
            this.waitForGemini = true;
            const response = await instance.get(`/attributeValues/geminiValues/${pdfId}`)
            this.attributeValues = response.data
            this.waitForGemini = false;
        },
        async upsertAttributeValues(pdfId: number) {
            let response = null
            this.attributeValuesError = null
            let values: Array<string | number> = [];
            this.attributeValues.forEach((val: any) => {
                const indexValue = val instanceof Date ? this.formatDateToDDMMYYYY(val) : val;
                values.push(indexValue);
            });
            try {
                response = await instance.post(`/attributeValues/${pdfId}`, values)
            } catch (e: any) {
                this.attributeValuesError = e.response.data.message;
            }
        },
        async getAttributeValuesValue(pdfId: number) {
            const response = await instance.get(`/attributeValues/listValues/${pdfId}`)
            this.attributeValues = response.data;
        },
        async listPdfsWithAttributeValues() {

            let values: Array<string | number> = [];
            this.attributeValues.forEach((val: any) => {
                const indexValue = val instanceof Date ? this.formatDateToDDMMYYYY(val) : val;
                values.push(indexValue);
            });
            const response = await instance.post(`/pdfs/pdfSearch/${this.archive.id}`, values)
            this.pdfsWithAttributeValues = response.data;
        },
        formatDateToDDMMYYYY(date: Date | null): string | null {
            if (!date) return null;
            const day = String(date.getDate()).padStart(2, '0');
            const month = String(date.getMonth() + 1).padStart(2, '0');
            const year = date.getFullYear();
            return `${day}.${month}.${year}`;
        }

    }
})