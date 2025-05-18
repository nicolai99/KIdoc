<script setup lang="ts">
import AppLayout from "@/layouts/AppLayout.vue";
import uploadPDF from "@/components/uploadPDF.vue";
</script>

<template>
  <AppLayout>
    <template #content>
      <uploadPDF/>
      <p>test</p>
    </template>
  </AppLayout>
</template>

<style scoped>

</style>