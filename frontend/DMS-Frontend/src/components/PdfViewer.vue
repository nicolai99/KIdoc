<template>
  <div>
    <iframe class="w-300 h-[70vh]" v-if="file" :src="pdfUrl "/>
    <p v-else>Please select a PDF to view or upload one.</p>
  </div>
</template>

<script setup lang="ts">
import {computed, defineProps} from 'vue';

interface Props {
  file: File | null;
}

const props = defineProps<Props>();
const pdfUrl = computed(() => {
  return props.file ? URL.createObjectURL(props.file) : null
})
</script>

<style scoped>

</style>