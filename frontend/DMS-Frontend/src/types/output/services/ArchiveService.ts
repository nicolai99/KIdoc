/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { ArchiveSchema } from '../models/ArchiveSchema';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class ArchiveService {
    /**
     * Get all archives
     * @returns ArchiveSchema OK
     * @throws ApiError
     */
    public static dmsApiViewsArchiveGetArchives(): CancelablePromise<Array<ArchiveSchema>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/archives/',
        });
    }
    /**
     * Create a new archive
     * @param requestBody
     * @returns any Created
     * @throws ApiError
     */
    public static dmsApiViewsArchiveCreateArchive(
        requestBody: ArchiveSchema,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/archives/',
            body: requestBody,
            mediaType: 'application/json',
        });
    }
    /**
     * Edit archive name
     * @param id
     * @param requestBody
     * @returns any OK
     * @throws ApiError
     */
    public static dmsApiViewsArchiveEditArchiveName(
        id: number,
        requestBody: ArchiveSchema,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/archives/edit/{id}',
            path: {
                'id': id,
            },
            body: requestBody,
            mediaType: 'application/json',
        });
    }
    /**
     * Get archive by ID
     * @param archiveId
     * @returns ArchiveSchema OK
     * @throws ApiError
     */
    public static dmsApiViewsArchiveGetArchiveById(
        archiveId: number,
    ): CancelablePromise<ArchiveSchema> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/archives/{archive_id}',
            path: {
                'archive_id': archiveId,
            },
        });
    }
}
