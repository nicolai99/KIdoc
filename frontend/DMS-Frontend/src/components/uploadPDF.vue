<template>
  <div class="card">
    <Toast />
    <FileUpload
      name="file"
      @uploader="openArchiveDialog"
      @remove="handleFileRemove"
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
      <Listbox v-model="selectedArchive" :options="archiveStore.archives" optionLabel="name" class="w-full md:w-14rem" />

      <template #footer>
        <Button label="Abbrechen" icon="pi pi-times" @click="displayArchiveDialog = false" class="p-button-text" />
        <Button label="Hochladen" icon="pi pi-check" @click="confirmArchiveSelection" :disabled="!selectedArchive" />
      </template>
    </Dialog>
  </div>
</template>

<script setup lang="ts">
import { ref, defineEmits, onMounted } from 'vue';
import { useToast } from 'primevue/usetoast';
import Dialog from 'primevue/dialog';
import Listbox from 'primevue/listbox';
import Button from 'primevue/button';
import instance from '@/services/axios.ts';
import type { FileUploadUploaderEvent, FileUploadRemoveEvent } from 'primevue/fileupload';

import { useArchiveStore } from '@/stores/archiveStore.ts';
import type { ArchiveSchema } from '@/types/output';

const toast = useToast();
const uploadedFiles = ref<{ file: File, id: number, url: string }[]>([]);

const archiveStore = useArchiveStore();

const displayArchiveDialog = ref(false);
const selectedArchive = ref<ArchiveSchema | null>(null);
const pendingFile = ref<File | null>(null);

const emit = defineEmits<{
  (e: 'upload-success', data: { id: number; name: string; url: string }): void;
  (e: 'remove-success', pdfId: number): void;
}>();

onMounted(async () => {
  await archiveStore.getArchives();
  await archiveStore.getTypes();
});

const openArchiveDialog = (event: FileUploadUploaderEvent) => {
  const files = event.files;
  const fileToUpload = Array.isArray(files) ? files[0] : files;

  if (!(fileToUpload instanceof File)) {
    toast.add({severity:'error', summary:'Fehler', detail:'Keine Datei ausgewählt', life: 3000});
    return;
  }

  if (fileToUpload.type !== 'application/pdf') {
    toast.add({severity:'warn', summary:'Falscher Dateityp', detail:'Bitte nur PDF-Dateien hochladen.', life: 3000});
    return;
  }

  pendingFile.value = fileToUpload;
  displayArchiveDialog.value = true;
};

const confirmArchiveSelection = async () => {
  if (!selectedArchive.value) {
    toast.add({severity:'warn', summary:'Auswahl fehlt', detail:'Bitte wählen Sie ein Archiv aus.', life: 3000});
    return;
  }

  if (!pendingFile.value) {
    toast.add({severity:'error', summary:'Fehler', detail:'Keine Datei zum Hochladen vorhanden.', life: 3000});
    return;
  }

  displayArchiveDialog.value = false;
  await uploadFileWithArchive(pendingFile.value, selectedArchive.value.id!);

  pendingFile.value = null;
  selectedArchive.value = null;
};

const uploadFileWithArchive = async (file: File, archiveId: number) => {
  const formData = new FormData();
  formData.append('file', file);
  formData.append('archive_id', String(archiveId));

  try {
    const response = await instance.post('/upload/upload', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });

    const pdfId = response.data.id;
    const pdfUrl = response.data.content_url;
    const pdfName = response.data.name;

    uploadedFiles.value.push({ file: file, id: pdfId, url: pdfUrl });

    toast.add({severity:'success', summary:'Erfolg', detail:'Datei wurde erfolgreich hochgeladen', life: 3000});
    console.log('✅ Upload erfolgreich:', response.data);

    emit('upload-success', { id: pdfId, name: pdfName, url: pdfUrl });

  } catch (error) {
    toast.add({severity:'error', summary:'Upload Fehler', detail:'Fehler beim Hochladen der Datei', life: 3000});
    console.error('❌ Fehler beim Upload:', error);
  }
};

const handleFileRemove = async (event: FileUploadRemoveEvent) => {
  const removedFile = event.file as File;
  const fileEntry = uploadedFiles.value.find(f => f.file.name === removedFile.name);

  if (!fileEntry) {
    toast.add({severity:'warn', summary:'Datei nicht gefunden', detail:'Diese Datei wurde nicht hochgeladen (lokal).', life: 3000});
    return;
  }

  const pdfId = fileEntry.id;

  try {
    await instance.delete(`/upload/pdfs/${pdfId}/`);
    toast.add({severity:'success', summary:'Erfolg', detail:'Datei wurde gelöscht', life: 3000});

    uploadedFiles.value = uploadedFiles.value.filter(f => f.id !== pdfId);
    emit('remove-success', pdfId);

  } catch (error) {
    toast.add({severity:'error', summary:'Lösch Fehler', detail:'Fehler beim Löschen der Datei', life: 3000});
    console.error('❌ Fehler beim Löschen:', error);
  }
};
</script>

<style scoped>
.card {
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  background-color: #ffffff;
}

.p-dialog .p-listbox {
  min-width: 15rem;
}
</style>
