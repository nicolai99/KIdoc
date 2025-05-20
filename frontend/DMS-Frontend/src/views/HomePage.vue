<script setup lang="ts">
import AppLayout from "@/layouts/AppLayout.vue";
import uploadPDF from "@/components/uploadPDF.vue";
import PdfViewer from "@/components/PdfViewer.vue";
</script>

<template>
  <AppLayout>
    <template #content>
      <uploadPDF/>
      <p>test</p>
      <PdfViewer></PdfViewer>
    </template>
  </AppLayout>
</template>

<style scoped>

</style>