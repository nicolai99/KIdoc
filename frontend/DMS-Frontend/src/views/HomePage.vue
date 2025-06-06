<script setup lang="ts">
import { ref, onMounted } from 'vue';
import AppLayout from "@/layouts/AppLayout.vue";
import uploadPDF from "@/components/uploadPDF.vue";
import PdfViewer from "@/components/PdfViewer.vue";
import instance from '@/services/axios.ts';
import { useUserStore } from '@/stores/userStore.ts';
import axios from 'axios';

import Button from 'primevue/button';
import ProgressSpinner from 'primevue/progressspinner';
import Message from 'primevue/message';
import Dialog from 'primevue/dialog';
import InputText from 'primevue/inputtext';
import { useConfirm } from "primevue/useconfirm";
import ConfirmDialog from 'primevue/confirmdialog';

import type { ArchiveSchema, AttributesSchema } from '@/types/output';


interface PdfEntry {
  id: number;
  name: string;
  content_url: string | null;
  archive_id: number;
}

const currentPdfSource = ref<string>('');
const pdfList = ref<PdfEntry[]>([]);
const isLoadingPdfs = ref<boolean>(false);
const errorLoadingPdfs = ref<string | null>(null);

const displayPdfDialog = ref<boolean>(false);
const dialogPdfTitle = ref<string>('');


const selectedArchiveDetails = ref<ArchiveSchema | null>(null);

const userStore = useUserStore();
const confirm = useConfirm();

const fetchPdfs = async () => {
  isLoadingPdfs.value = true;
  errorLoadingPdfs.value = null;
  try {
    const response = await instance.get('/upload/files', {
        headers: {
            'X-CSRFToken': userStore.csrfToken || '',
        }
    });
    pdfList.value = response.data as PdfEntry[];

  } catch (error) {
    console.error('Error fetching PDFs:', error);
    errorLoadingPdfs.value = 'Fehler beim Laden der PDFs.';

    if (axios.isAxiosError(error)) {
        if (error.response?.status === 401) {
            errorLoadingPdfs.value = 'Fehler beim Laden der PDFs: Nicht autorisiert. Bitte loggen Sie sich ein.';
        } else if (error.code === 'ERR_NETWORK') {
            errorLoadingPdfs.value = 'Netzwerkfehler: Backend-Server ist möglicherweise nicht erreichbar oder hat einen Fehler.';
        } else if (error.message) {
            errorLoadingPdfs.value += `: ${error.message}`;
        }
    }
  } finally {
    isLoadingPdfs.value = false;
  }
};

const handleUploadSuccess = async () => {
  await fetchPdfs();
  console.log('PDF uploaded successfully, re-fetching list.');
};

const handleRemoveSuccess = async (pdfId: number) => {
  await fetchPdfs();
  console.log(`PDF with ID ${pdfId} removed successfully (via uploadPDF component), re-fetching list.`);
};

const selectPdfToView = async (pdfEntry: PdfEntry) => {
  if (pdfEntry.content_url) {
    currentPdfSource.value = pdfEntry.content_url;
    dialogPdfTitle.value = pdfEntry.name || `PDF ${pdfEntry.id}`;

    try {
      const response = await instance.get(`/archives/${pdfEntry.archive_id}/`);
      selectedArchiveDetails.value = response.data as ArchiveSchema;
      console.log('Fetched Archive Details:', selectedArchiveDetails.value);
    } catch (error) {
      console.error(`Error fetching archive details for archive ID ${pdfEntry.archive_id}:`, error);
      selectedArchiveDetails.value = null;
    }

    displayPdfDialog.value = true;
  } else {
    console.warn('Selected PDF has no content URL. Cannot display.');
  }
};

const deletePdf = async (event: Event, pdfId: number, pdfName: string) => {
    confirm.require({
        target: event.currentTarget as HTMLElement,
        message: `Möchten Sie "${pdfName}" wirklich löschen?`,
        icon: 'pi pi-exclamation-triangle',
        acceptLabel: 'Ja',
        rejectLabel: 'Nein',
        accept: async () => {
            try {
                isLoadingPdfs.value = true;
                errorLoadingPdfs.value = null;

                await instance.delete(`/upload/pdfs/${pdfId}/`, {
                });
                console.log(`PDF with ID ${pdfId} deleted from backend.`);
                await fetchPdfs();
            } catch (error) {
                console.error(`Error deleting PDF with ID ${pdfId}:`, error);
                errorLoadingPdfs.value = `Fehler beim Löschen der PDF (ID: ${pdfId}).`;

                if (axios.isAxiosError(error)) {
                    if (error.response?.status === 401) {
                        errorLoadingPdfs.value = 'Fehler beim Löschen: Nicht autorisiert. Bitte loggen Sie sich ein.';
                    } else if (error.code === 'ERR_NETWORK') {
                        errorLoadingPdfs.value = 'Netzwerkfehler beim Löschen: Backend-Server ist möglicherweise nicht erreichbar.';
                    } else if (error.message) {
                        errorLoadingPdfs.value += `: ${error.message}`;
                    }
                }
            } finally {
                isLoadingPdfs.value = false;
            }
        },
        reject: () => {
            console.log('Deletion cancelled.');
        }
    });
};

onMounted(() => {
  fetchPdfs();
});
</script>

<template>
  <AppLayout>
    <template #content>
      <h1>PDF Management</h1>

      <uploadPDF
        @upload-success="handleUploadSuccess"
        @remove-success="handleRemoveSuccess"
      />

      <hr />

      <h2>Alle hochgeladenen PDFs</h2>
      <div v-if="isLoadingPdfs" class="loading-spinner-container">
        <ProgressSpinner />
      </div>
      <div v-else-if="errorLoadingPdfs">
        <Message severity="error">{{ errorLoadingPdfs }}</Message>
      </div>
      <div v-else-if="pdfList.length > 0">
        <ul class="pdf-list">
          <li v-for="pdf in pdfList" :key="pdf.id">
            <a href="#" @click.prevent="selectPdfToView(pdf)">
              {{ pdf.name || `PDF ${pdf.id}` }}
            </a>
            <Button
                icon="pi pi-trash"
                severity="danger"
                label="Löschen"
                @click="deletePdf($event, pdf.id, pdf.name || `PDF ${pdf.id}`)"
                class="p-button-sm"
            />
          </li>
        </ul>
      </div>
      <div v-else>
        <p>Noch keine PDFs hochgeladen. Laden Sie oben eine hoch, um sie hier dauerhaft anzuzeigen.</p>
      </div>

      <hr />

      <Dialog
        v-model:visible="displayPdfDialog"
        :header="dialogPdfTitle"
        :modal="true"
        :draggable="false"
        :resizable="false"
        :style="{width: '90vw', height: '90vh'}" contentClass="p-dialog-content-scrollable" >

        <div class="pdf-details-layout"> <div class="attribute-panel">
                <h3>Archiv &lt;{{ selectedArchiveDetails?.name || 'N/A' }}&gt;</h3>
                <div v-if="selectedArchiveDetails?.attributes?.length">
                    <h4>Attribute</h4>
                    <div v-for="attr in selectedArchiveDetails.attributes" :key="attr.id" class="attribute-item">
                        <label>{{ attr.label || attr.name }} ({{ attr.type?.name }})</label>
                        <InputText :placeholder="`Wert für ${attr.label || attr.name}`" disabled class="w-full" />
                    </div>
                </div>
                <div v-else>
                    <p>Keine Attribute für dieses Archiv konfiguriert.</p>
                </div>
            </div>
            <div class="pdf-panel">
                <PdfViewer :pdfSource="currentPdfSource" />
            </div>
        </div>
      </Dialog>
    </template>
  </AppLayout>
  <ConfirmDialog></ConfirmDialog>
</template>

<style scoped>
h1, h2 {
  text-align: center;
  margin-top: 20px;
}
hr {
  margin: 40px 0;
  border: 0;
}

.pdf-list {
  list-style: none;
  padding: 0;
  max-width: 800px;
  margin: 20px auto;
}

.pdf-list li {
  padding: 10px 15px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.pdf-list li:last-child {
  border-bottom: none;
}

.pdf-list a {
  text-decoration: none;
  color: var(--primary-color);
  font-weight: bold;
  flex-grow: 1;
  margin-right: 15px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.pdf-list a:hover {
  text-decoration: underline;
}

p {
  text-align: center;
  margin: 20px 0;
  font-style: italic;
}

.loading-spinner-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100px;
}


.pdf-viewer-dialog-wrapper {
    height: 100%;
    overflow-y: auto;
    padding-right: 5px;
}

.pdf-details-layout {
    display: flex;
    height: 100%;
    gap: 20px;
    padding: 20px;
    box-sizing: border-box;
}

.attribute-panel {
    flex: 0 0 30%;
    padding-right: 20px;
    border-right: 1px solid #eee;
    overflow-y: auto;
}

.attribute-panel h3, .attribute-panel h4 {
    margin-top: 0;
    margin-bottom: 15px;
    text-align: left;
}

.attribute-item {
    margin-bottom: 15px;
}

.attribute-item label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
    font-size: 0.9em;
    color: #555;
}

.pdf-panel {
    flex: 1;
    height: 100%;
    overflow: hidden;
}


:deep(.p-dialog-content-scrollable) {
    height: calc(100% - 50px) !important;
    overflow: hidden !important;
    padding: 0 !important;
}

.p-button-sm {
    padding: 0.5rem 1rem;
    font-size: 0.875rem;
}
</style>
