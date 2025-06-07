<script setup lang="ts">
import PdfViewer from './PdfViewer.vue';
import {usePdfStore} from "@/stores/pdfStore.ts";
import {useArchiveStore} from "@/stores/archiveStore.ts";
import AttributesValueInput from "@/components/AttributesValueInput.vue";

const pdfStore = usePdfStore();
const archiveStore = useArchiveStore();

</script>

<template>
  <div class="w-full flex flex-row ">
    <Card>
      <template #header>
        <h1 class="text-2xl font-bold">Attribute</h1>
      </template>
      <template #content>
        <div class="flex flex-col gap-3">
          <AttributesValueInput v-for="(att,index) in archiveStore.archive.attributes" :id="att.id" :label="att.label"
                                :type="att.type.name" :index="index"
                                :value="archiveStore.attributeValues[index]"></AttributesValueInput>
        </div>
      </template>
    </Card>
    <PdfViewer :file="pdfStore.pdf"/>
  </div>
</template>

<style scoped>

</style>