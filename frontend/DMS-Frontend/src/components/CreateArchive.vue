<script setup lang="ts">
import {useArchiveStore} from "@/stores/archiveStore.ts";
import AddAttribute from "@/components/AddAttribute.vue";
import {ref} from "vue";

const showAddAttribute = ref(false);
const archivStore = useArchiveStore();
const addAttributeToArchive = () => {
  showAddAttribute.value = false;
  archivStore.archive.attributes.push(archivStore.attribute)
}
const emit = defineEmits(['after-create-archive']);
const storeArchive = async () => {
  await archivStore.saveArchive();
  if (archivStore.archiveSaveError) {
    alert(archivStore.archiveSaveErrorMessage)
  } else {
    emit('after-create-archive');
  }
}
</script>
<template>
  <div class="grid grid-cols-1 gap-y-2 p-2">
    <FloatLabel variant="on">
      <InputText id="name" v-model="archivStore.archive.name"/>
      <label for="name">Name</label>
    </FloatLabel>
    <Button @click="showAddAttribute=!showAddAttribute" class="w-50">Neues Attribut</Button>
    <Dialog v-model:visible="showAddAttribute">
      <template #header>
        <h1 class="text-2xl">Neues Attribut</h1>
      </template>
      <AddAttribute @after-add-attribute="addAttributeToArchive"/>
    </Dialog>
    <h2 class="text-2xl">Attribute</h2>
    <data-table :value="archivStore.archive.attributes">
      <Column field="label" header="Bezeichnung"></Column>
      <Column header="Typ">
        <template #body="slotProps">
          {{ slotProps.data.type.id }}
        </template>
      </Column>

    </data-table>
    <Button @click="storeArchive">Archiv Speichern</Button>
  </div>
</template>