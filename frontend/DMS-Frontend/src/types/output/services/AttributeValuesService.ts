/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { AttributesValueSchema } from '../models/AttributesValueSchema';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class AttributeValuesService {
    /**
     * Get Attribute Values By Pdf
     * @param id
     * @returns AttributesValueSchema OK
     * @throws ApiError
     */
    public static dmsApiViewsAttributeValuesGetAttributeValuesByPdf(
        id: number,
    ): CancelablePromise<Array<AttributesValueSchema>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/attributeValues/{id}',
            path: {
                'id': id,
            },
        });
    }
    /**
     * Get Attribute Values By Pdf from Gemini
     * @param id
     * @returns string OK
     * @throws ApiError
     */
    public static dmsApiViewsAttributeValuesGetGeminiAttributeValuesByPdf(
        id: string,
    ): CancelablePromise<Array<string>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/attributeValues/geminiValues/{id}',
            path: {
                'id': id,
            },
        });
    }
}
