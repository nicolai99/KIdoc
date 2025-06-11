/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { AttributesSchema } from '../models/AttributesSchema';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class AttributeService {
    /**
     * Add Attribute
     * @param requestBody
     * @returns any OK
     * @throws ApiError
     */
    public static dmsApiViewsAttributeAddAttribute(
        requestBody: AttributesSchema,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/attributes/',
            body: requestBody,
            mediaType: 'application/json',
        });
    }
    /**
     * Delete Attribute
     * @param id
     * @returns any OK
     * @throws ApiError
     */
    public static dmsApiViewsAttributeDeleteAttribute(
        id: number,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/attributes/{id}',
            path: {
                'id': id,
            },
        });
    }
}
