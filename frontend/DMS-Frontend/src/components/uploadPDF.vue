<template>
  <div class="card">
    <Toast/>
    <FileUpload
        name="file"
        @uploader="handleFileUpload"
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
import instance from '@/services/axios.ts';
import {FileUploadUploaderEvent} from 'primevue/fileupload';

const handleFileUpload = async (event: FileUploadUploaderEvent) => {
  const selectedFile = event.files?.[0];

  if (!(selectedFile instanceof File)) {
    console.error('❌ Keine Datei ausgewählt.');
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

    console.log('✅ Upload erfolgreich:', response.data);
  } catch (error) {
    console.error('❌ Fehler beim Upload:', error);
  }
};
</script>
