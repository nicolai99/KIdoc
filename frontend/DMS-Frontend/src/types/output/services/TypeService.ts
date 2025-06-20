/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { TypeSchema } from '../models/TypeSchema';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class TypeService {
    /**
     * Get all types
     * @returns TypeSchema OK
     * @throws ApiError
     */
    public static dmsApiViewsTypeGetTypes(): CancelablePromise<Array<TypeSchema>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/types/',
        });
    }
    /**
     * Create a new type
     * @param requestBody
     * @returns any Created
     * @throws ApiError
     */
    public static dmsApiViewsTypeCreateType(
        requestBody: TypeSchema,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/types/',
            body: requestBody,
            mediaType: 'application/json',
        });
    }
}
