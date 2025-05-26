<template>
  <div>
    <vue-pdf-embed v-if="pdfSource" :source="pdfSource" />
    <p v-else>Please select a PDF to view or upload one.</p>
  </div>
</template>

<script setup lang="ts">
import VuePdfEmbed from 'vue-pdf-embed';
import { defineProps } from 'vue';

interface Props {
  pdfSource: string;
}

const props = defineProps<Props>();
</script>

<style scoped>
div {
  max-width: 800px;
  margin: 20px auto;
}
p {
  text-align: center;
  color: #888;
  margin-top: 50px;
}
</style>