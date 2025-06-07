<script setup lang="ts">

import AppLayout from "@/layouts/AppLayout.vue";
import UploadPDF from "@/components/uploadPDF.vue";
import AttributesWithPdf from "@/components/AttributesWithPdf.vue";
import {ref} from "vue";

const showAttributesWithPdf = ref(false);
</script>

<template>
  <AppLayout>
    <template #subheader>
      Upload
    </template>
    <template #content>
      <uploadPDF @upload-success="showAttributesWithPdf=true"></uploadPDF>
      <Dialog v-model:visible="showAttributesWithPdf" header="Archiv" modal>
        <attributes-with-pdf :show-attributes-with-pdf="true"></attributes-with-pdf>
      </Dialog>
    </template>
  </AppLayout>

</template>

<style scoped>

</style>