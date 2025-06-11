<script setup lang="ts">

import AttributesValueInput from "@/components/AttributesValueInput.vue";
import type {ArchiveSchema} from "@/types/output";
import {useArchiveStore} from "@/stores/archiveStore.ts";
import {ref, watch} from "vue";
import {usePdfStore} from "@/stores/pdfStore.ts";
import AttributesWithPdf from "@/components/AttributesWithPdf.vue";

const props = defineProps<{ archive: ArchiveSchema, lengthAttributes: number }>()
const archiveStore = useArchiveStore();
const showAttributesWithPdf = ref(false);
archiveStore.pdfsWithAttributeValues = [];
const pdfStore = usePdfStore();

const openAttributesWithPdf = async (pdfId) => {
  pdfStore.id = pdfId;
  await archiveStore.getAttributeValuesValue(pdfId)
  await pdfStore.getPdfContent(pdfId)
  showAttributesWithPdf.value = true;

}
watch(() => props.lengthAttributes, () => {
      archiveStore.initAttributeValues(props.lengthAttributes);
    },
    {immediate: true})
const search = async () => {
  await archiveStore.listPdfsWithAttributeValues();
}

const deletePdf = async (id) => {
  await pdfStore.deletePdf(id);
  await search();
}

const afterSuccessAttributes = () => {
  archiveStore.initAttributeValues(props.lengthAttributes);
  search();
  showAttributesWithPdf.value = false;
}

</script>

<template>
  <card>
    <template #header>
      {{ archive.name }}
    </template>
    <template #content>
      <div class="flex flex-col gap-y-20">
        <div class="flex flex-col gap-3">
          <AttributesValueInput v-for="(att,index) in archive.attributes" :id="att.id!" :label="att.label"
                                :type="att.type.name!" :index="index"></AttributesValueInput>
          <Button @click="search">Suchen</Button>
        </div>
        <div>
          <data-table :value="archiveStore.pdfsWithAttributeValues">
            <Column header="Dokumentenname">
              <template #body="slotProps">
                <p class="underline cursor-pointer"
                   @click="openAttributesWithPdf(slotProps.data.id)">
                  {{ slotProps.data.name }}</p>
              </template>
            </Column>
            <Column v-for="(att,index) in archive.attributes" :header="att.label">
              <template #body="slotProps">
                {{
                  slotProps.data.attribute_values?.[index]?.value ?? 'leer'
                }}
              </template>
            </Column>
            <Column>
              <template #body="slotProps">
                <Button severity="danger" @click="deletePdf(slotProps.data.id)">Löschen</Button>
              </template>
            </Column>
            <template #empty>keine Suchergebnisse.</template>
          </data-table>
        </div>
      </div>
    </template>
  </card>
  <Dialog v-model:visible="showAttributesWithPdf" modal>
    <AttributesWithPdf @after-success="afterSuccessAttributes">

    </AttributesWithPdf>
  </Dialog>
</template>

<style scoped>

</style>