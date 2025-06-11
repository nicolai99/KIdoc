/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { AttributesSchema } from './AttributesSchema';
import type { PdfSchema } from './PdfSchema';
export type AttributesValueSchema = {
    id?: (number | null);
    createOn?: (string | null);
    attribute: AttributesSchema;
    pdf: PdfSchema;
    value: string;
};

