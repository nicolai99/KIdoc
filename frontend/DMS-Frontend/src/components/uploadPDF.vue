<template>
  <div>
    <input type="file" accept="application/pdf" @change="handleFileUpload" />
    <button @click="uploadFile" :disabled="!selectedFile">Upload</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      selectedFile: null
    };
  },
  methods: {
    handleFileUpload(event) {
      const file = event.target.files[0];
      if (file && file.type === "application/pdf") {
        this.selectedFile = file;
      } else {
        alert("Bitte nur PDF-Dateien auswählen.");
        this.selectedFile = null;
      }
    },
    async uploadFile() {
      if (!this.selectedFile) return;

      const formData = new FormData();
      formData.append('file', this.selectedFile);

      try {
        const response = await axios.post(
          'http://localhost:8000/api/upload/upload',
          formData,
          {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          }
        );

        console.log('Upload erfolgreich:', response.data);
      } catch (error) {
        console.error('Fehler beim Upload:', error.response?.data || error.message);
      }
    }
  }
};
</script>
