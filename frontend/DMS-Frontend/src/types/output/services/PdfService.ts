/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { PdfSchema } from '../models/PdfSchema';
import type { PdfWithValuesSchema } from '../models/PdfWithValuesSchema';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class PdfService {
    /**
     * Upload a PDF file
     * @param formData
     * @returns number OK
     * @throws ApiError
     */
    public static dmsApiViewsPdfUploadPdf(
        formData: {
            file: Blob;
            archive_id: number;
        },
    ): CancelablePromise<number> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/upload/upload',
            formData: formData,
            mediaType: 'multipart/form-data',
        });
    }
    /**
     * List all PDFs
     * @returns PdfSchema OK
     * @throws ApiError
     */
    public static dmsApiViewsPdfListPdfs(): CancelablePromise<Array<PdfSchema>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/upload/files',
        });
    }
    /**
     * Get PDF content
     * @param pdfId
     * @returns any OK
     * @throws ApiError
     */
    public static dmsApiViewsPdfGetPdfContent(
        pdfId: number,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/upload/pdfs/{pdf_id}/',
            path: {
                'pdf_id': pdfId,
            },
        });
    }
    /**
     * Delete PDF
     * @param pdfId
     * @returns void
     * @throws ApiError
     */
    public static dmsApiViewsPdfDeletePdf(
        pdfId: number,
    ): CancelablePromise<void> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/upload/pdfs/{pdf_id}/',
            path: {
                'pdf_id': pdfId,
            },
        });
    }
    /**
     * List all Pdf by Seachparameter
     * @param archiveId
     * @param requestBody
     * @returns PdfWithValuesSchema OK
     * @throws ApiError
     */
    public static dmsApiViewsPdfPdfSearch(
        archiveId: number,
        requestBody: Array<(string | number | null)>,
    ): CancelablePromise<Array<PdfWithValuesSchema>> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/upload/pdfSearch/{archiveId}',
            path: {
                'archiveId': archiveId,
            },
            body: requestBody,
            mediaType: 'application/json',
        });
    }
}
