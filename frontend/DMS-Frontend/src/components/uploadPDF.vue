<template>
  <div class="card">
    <Toast />
    <FileUpload
      name="file"
      @uploader="handleFileUpload"
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
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useToast } from 'primevue/usetoast';
import instance from '@/services/axios.ts';
import type { FileUploadUploaderEvent, FileUploadRemoveEvent } from 'primevue/fileupload';

const toast = useToast();
const uploadedFiles = ref<{file: File, id: number}[]>([]);

const handleFileUpload = async (event: FileUploadUploaderEvent) => {
  const files = event.files;
  const selectedFile = Array.isArray(files) ? files[0] : files;

  if (!(selectedFile instanceof File)) {
    toast.add({severity:'error', summary:'Fehler', detail:'Keine Datei ausgewählt', life: 3000});
    return;
  }

  if (selectedFile.type !== 'application/pdf') {
    toast.add({severity:'warn', summary:'Falscher Dateityp', detail:'Bitte nur PDF-Dateien hochladen.', life: 3000});
    return;
  }

  const formData = new FormData();
  formData.append('file', selectedFile);

  try {
    const response = await instance.post('/upload/upload', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });

    const pdfId = response.data.id;
    uploadedFiles.value.push({file: selectedFile, id: pdfId});

    toast.add({severity:'success', summary:'Erfolg', detail:'Datei wurde erfolgreich hochgeladen', life: 3000});
    console.log('✅ Upload erfolgreich:', response.data);
  } catch (error) {
    toast.add({severity:'error', summary:'Upload Fehler', detail:'Fehler beim Hochladen der Datei', life: 3000});
    console.error('❌ Fehler beim Upload:', error);
  }
};

const handleFileRemove = async (event: FileUploadRemoveEvent) => {
  const removedFile = event.file as File;
  const fileIndex = uploadedFiles.value.findIndex(f => f.file.name === removedFile.name);
  if (fileIndex === -1) {
    toast.add({severity:'warn', summary:'Datei nicht gefunden', detail:'Diese Datei wurde nicht hochgeladen.', life: 3000});
    return;
  }

  const pdfId = uploadedFiles.value[fileIndex].id;

  try {
    await instance.delete(`/upload/delete/${pdfId}`);
    toast.add({severity:'success', summary:'Erfolg', detail:'Datei wurde gelöscht', life: 3000});
    uploadedFiles.value.splice(fileIndex, 1);
  } catch (error) {
    toast.add({severity:'error', summary:'Lösch Fehler', detail:'Fehler beim Löschen der Datei', life: 3000});
    console.error('❌ Fehler beim Löschen:', error);
  }
};
</script>
