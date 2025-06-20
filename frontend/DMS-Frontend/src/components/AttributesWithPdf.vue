<script setup lang="ts">
import PdfViewer from './PdfViewer.vue';
import {usePdfStore} from "@/stores/pdfStore.ts";
import {useArchiveStore} from "@/stores/archiveStore.ts";
import AttributesValueInput from "@/components/AttributesValueInput.vue";
import {useToast} from "primevue/usetoast";

const emit = defineEmits(['afterSuccess']);
const pdfStore = usePdfStore();
const archiveStore = useArchiveStore();
const toastService = useToast();
const saveAttributeValues = async () => {
  await archiveStore.upsertAttributeValues(pdfStore.id);
  if (archiveStore.attributeValuesError)
    toastService.add({severity: 'error', summary: 'Fehler', detail: archiveStore.attributeValuesError, life: 3000});
  else {
    emit('afterSuccess');
  }
}

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
          ></AttributesValueInput>
        </div>
      </template>
      <template #footer>
        <Button @click="saveAttributeValues">Attribute speichern</Button>
      </template>
    </Card>
    <PdfViewer :file="pdfStore.pdf"/>
  </div>
  <Toast></Toast>
</template>

<style scoped>

</style>