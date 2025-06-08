<script setup lang="ts">

import AppLayout from "@/layouts/AppLayout.vue";
import UploadPDF from "@/components/uploadPDF.vue";
import AttributesWithPdf from "@/components/AttributesWithPdf.vue";
import {ref} from "vue";
import {useArchiveStore} from "@/stores/archiveStore.ts";
import {usePdfStore} from "@/stores/pdfStore.ts";

const showAttributesWithPdf = ref(false);
const archiveStore = useArchiveStore();
const pdfStore = usePdfStore();
</script>

<template>
  <AppLayout>
    <template #subheader>
      Upload
    </template>
    <template #content>
      <progress-spinner v-if="pdfStore.loading || archiveStore.waitForGemini">

      </progress-spinner>
      <p v-if="pdfStore.loading">Dokument wird hochgeladen...</p>
      <p v-else-if="archiveStore.waitForGemini">Warten auf Gemini-Antwort...</p>
      <uploadPDF @upload-success="showAttributesWithPdf=true"></uploadPDF>
      <Dialog v-model:visible="showAttributesWithPdf" header="Archiv" modal>
        <attributes-with-pdf :show-attributes-with-pdf="true"></attributes-with-pdf>
      </Dialog>
    </template>
  </AppLayout>

</template>

<style scoped>

</style>