<script setup lang="ts">
import AppLayout from "@/layouts/AppLayout.vue";
import uploadPDF from "@/components/uploadPDF.vue";
</script>

<template>
  <AppLayout>
    <template #content>
      <uploadPDF/>
    </template>
  </AppLayout>
</template>

<style scoped>

</style>