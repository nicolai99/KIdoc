<script setup lang="ts">
import {useArchiveStore} from "@/stores/archiveStore.ts";

const archivStore = useArchiveStore();
archivStore.getTypes();

const emit = defineEmits(['afterAddAttribute'])
const addAttribute = () => {
  emit('afterAddAttribute');
}

</script>

<template>
  <div class="grid grid-cols-1 gap-y-2 p-2">
    <FloatLabel variant="on">
      <InputText id="label" v-model="archivStore.attribute.label"
                 @keyup="archivStore.attribute.name=archivStore.attribute.label.toLowerCase()"/>
      <label for="label">Label</label>
    </FloatLabel>
    <FloatLabel variant="on">
      <InputText id="name" v-model="archivStore.attribute.name"/>
      <label for="name">Name</label>
    </FloatLabel>
    <FloatLabel variant="on">
      <Select v-model="archivStore.attribute.type.id" inputId="over_label" :options="archivStore.types"
              optionLabel="name"
              optionValue="id"
              class="w-full"/>
      <label for="name">Feldart</label>
    </FloatLabel>
    <Button @click="addAttribute">Attribut hinzufügen</Button>
  </div>
</template>

<style scoped>

</style>