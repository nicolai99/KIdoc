/// <reference types="vite/client" />
interface ImportMetaEnv {
    readonly VITE_API_URL: string;
    readonly VITE_FEATURE_FLAG?: 'on' | 'off';
    // Weitere eigene Variablen hier typisieren
}

interface ImportMeta {
    readonly env: ImportMetaEnv;
}