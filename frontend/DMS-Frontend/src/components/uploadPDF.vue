<template>
  <div class="card">
    <Toast/>
    <FileUpload
        ref="fileUploadRef"
        name="file"
        @uploader="openArchiveDialog"
        @remove="handleFileRemove"
        @select="alert('Select event')"
        :multiple="false"
        accept="application/pdf"
        :maxFileSize="1000000"
        customUpload
    >
      <template #empty>
        <span>Drag and drop a PDF file here to upload.</span>
      </template>
    </FileUpload>

    <Dialog v-model:visible="displayArchiveDialog" modal header="Archiv auswählen" :style="{ width: '50vw' }">
      <p class="mb-4">Bitte wählen Sie ein Archiv für das PDF-Dokument aus:</p>
      <Listbox v-model="archiveStore.archive" :options="archiveStore.archives" optionLabel="name"
               class="w-full md:w-14rem"/>

      <template #footer>
        <Button label="Abbrechen" icon="pi pi-times" @click="displayArchiveDialog = false" class="p-button-text"/>
        <Button label="Hochladen" icon="pi pi-check" @click="confirmArchiveSelection"
                :disabled="!archiveStore.archive"/>
      </template>
    </Dialog>
  </div>
</template>

<script setup lang="ts">
import {defineEmits, onMounted, ref} from 'vue';
import {useToast} from 'primevue/usetoast';
import Dialog from 'primevue/dialog';
import Listbox from 'primevue/listbox';
import Button from 'primevue/button';
import type {FileUploadUploaderEvent} from 'primevue/fileupload';

import {useArchiveStore} from '@/stores/archiveStore.ts';
import {usePdfStore} from "@/stores/pdfStore.ts";

const toast = useToast();
const fileUploadRef = ref(null);
const archiveStore = useArchiveStore();

const displayArchiveDialog = ref(false);
const pdfStore = usePdfStore();

const emit = defineEmits<{
  (e: 'upload-success'): void;
  (e: 'remove-success', pdfId: number): void;
}>();

onMounted(async () => {
  await archiveStore.getArchives();
  await archiveStore.getTypes();
});

const openArchiveDialog = (event: FileUploadUploaderEvent) => {
  displayArchiveDialog.value = true;
  pdfStore.pdf = event.files[0];

};

const confirmArchiveSelection = async () => {
  pdfStore.archive_id = archiveStore.archive.id!;
  displayArchiveDialog.value = false;
  await pdfStore.uploadPdf();
  if (!pdfStore.uploadError) {
    handleFileRemove();
    await archiveStore.getAttributeValuesFromGeminiByPdf(pdfStore.id!)
    emit("upload-success")
  }
};


const handleFileRemove = () => {
  fileUploadRef.value?.clear();

}


</script>

