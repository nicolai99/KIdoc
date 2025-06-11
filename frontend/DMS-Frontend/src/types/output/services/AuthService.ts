/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { AuthSchema } from '../models/AuthSchema';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class AuthService {
    /**
     * Get CSRF token
     * @returns any OK
     * @throws ApiError
     */
    public static dmsApiViewsAuthCsrfToken(): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/auth/csrf-token',
        });
    }
    /**
     * Login
     * @param requestBody
     * @returns any OK
     * @throws ApiError
     */
    public static dmsApiViewsAuthLoginUser(
        requestBody: AuthSchema,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/auth/login',
            body: requestBody,
            mediaType: 'application/json',
        });
    }
    /**
     * Logout
     * @returns any OK
     * @throws ApiError
     */
    public static dmsApiViewsAuthLogout(): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/auth/logout',
        });
    }
    /**
     * Get User
     * @returns any OK
     * @throws ApiError
     */
    public static dmsApiViewsAuthGetUser(): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/auth/user',
        });
    }
}
